"""Compiles the JSON requirement grammar into AP access rules.

Grammar (shared by regions.json, world_extra.json and rules.json):
    None / [] / [[]]        always true
    "token"                 one condition
    ["a", "b"]              a AND b
    [["a", "b"], ["c"]]     (a AND b) OR c

Tokens:
    Item name or game id    state.has           e.g. "Vine Rune", "LadderKey", "Boss_Death"
    "<item>:N"              state.has(item, N)  e.g. "Progressive Stem Cell:3"
    "region:<biome id>"     biome reachable     ("B_<biome id>" is accepted too)
    "loc:<Location Name>"   location reachable  (false when it does not exist in this seed)
    "depth:N"               some biome of depth N is reachable
    "count:<kind>:N"        N reachable locations of a kind (kinds live in rules.json)
    "tier:T:N"              N bosses of tier T beaten
    "@macro"                reusable requirement from rules.json
"""
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable

from ..constants import STEM_CELL
from ..data import GameData

Rule = Callable[[Any], bool]


@dataclass
class Compiled:
    rule: Rule | None                               #None == always true
    regions: set[str] = field(default_factory=set)  #regions the rule depends on (indirect conditions)
    impossible: bool = False


def _always_false(state) -> bool:
    return False


def parse_groups(raw: Any) -> list[list[str]]:
    """Normalise the grammar into a list of AND-groups (the requirement is their OR). [[]] = always true."""
    if raw is None or raw == "" or raw == [] or raw == [[]]:
        return [[]]
    if isinstance(raw, str):
        raw = [raw]
    if any(isinstance(x, list) for x in raw):
        return [list(g) if isinstance(g, list) else [g] for g in raw]
    return [list(raw)]


class Compiler:
    """`world` must already have its regions and locations created."""

    def __init__(self, world, data: GameData):
        self.player = world.player
        self.world = world
        self.data = data
        self.mw = world.multiworld
        self.regions = {r.name for r in self.mw.get_regions(self.player)}
        self._locations = {l.name: l for l in self.mw.get_locations(self.player)}

    # ── public ───────────────────────────────────────────────────────────────
    def compile(self, raw: Any) -> Compiled:
        groups = parse_groups(raw)
        if groups == [[]]:
            return Compiled(None)
        regions: set[str] = set()
        group_rules: list[Rule] = []
        for group in groups:
            preds = []
            for tok in group:
                p, r = self._token(tok)
                preds.append(p)
                regions |= r
            group_rules.append(self._and(preds))
        if len(group_rules) == 1:
            rule = group_rules[0]
        else:
            rule = lambda state, rs=tuple(group_rules): any(r(state) for r in rs)
        return Compiled(rule, regions)

    # ── grammar ──────────────────────────────────────────────────────────────
    def _and(self, preds: list[Rule]) -> Rule:
        if len(preds) == 1:
            return preds[0]
        return lambda state, ps=tuple(preds): all(p(state) for p in ps)

    # ── tokens ───────────────────────────────────────────────────────────────
    def _token(self, tok: str) -> tuple[Rule, set[str]]:
        player = self.player
        if tok.startswith("@"):
            sub = self.compile(self.data.macros[tok[1:]])
            return (sub.rule or (lambda s: True)), sub.regions
        kind, _, rest = tok.partition(":")
        if kind == "region" or tok.startswith("B_"):
            return self._region(rest if kind == "region" else tok[2:])
        if kind == "loc":
            return self._location(rest)
        if kind == "depth":
            ids = [b.id for b in self.data.biomes.values() if b.depth == int(rest)]
            return self._any_region(ids)
        if kind == "count":
            return self._count(*rest.split(":"))
        if kind == "tier":
            return self._tier(*rest.split(":"))
        return self._item(tok)

    def _item(self, tok: str):
        name, _, n = tok.rpartition(":")
        if not n.isdigit():
            name, n = tok, "1"
        item = self.data.resolve_item(name)
        player, need = self.player, int(n)
        if need == 1:
            return (lambda state: state.has(item, player)), set()
        return (lambda state: state.has(item, player, need)), set()

    def _region(self, biome_id: str):
        if biome_id not in self.regions:
            return _always_false, set()
        player = self.player
        return (lambda state: state.can_reach_region(biome_id, player)), {biome_id}

    def _any_region(self, ids: Iterable[str]):
        ids = [i for i in ids if i in self.regions]
        player = self.player
        return (lambda state: any(state.can_reach_region(i, player) for i in ids)), set(ids)

    def _location(self, name: str):
        loc = self._locations.get(name)
        if loc is None:
            return _always_false, set()
        return (lambda state: loc.can_reach(state)), set()

    def _reach_count(self, locs: list, need: int):
        def rule(state):
            n = 0
            for loc in locs:
                if loc.can_reach(state):
                    n += 1
                    if n >= need:
                        return True
            return False
        return rule, set()

    def _count(self, kind: str, n: str):
        types = set(self.data.count_kinds[kind])
        gated = self.data.count_excluded(kind)
        locs = [l for name, l in self._locations.items()
                if self.data.locations[name].type in types and name not in gated]
        return self._reach_count(locs, int(n))

    def _tier(self, tier: str, n: str):
        names = [self.data.boss_location(b) for b in self.data.boss_tiers[tier]]
        return self._reach_count([self._locations[x] for x in names if x in self._locations], int(n))
