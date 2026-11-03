"""Room randomizer: which biome each door really leads to.

The result is `map`: {original destination: actual biome}. Every door that the base game sends to D
sends the player to map[D] instead. A biome keeps its own exits (its doors, and the ability each door
needs); only their destinations change. Modes:

    depth    biomes of the same depth are shuffled together
    tier     3 groups of normal biomes (delimited by the boss tiers) + the boss arenas of each tier, shuffled per tier
    chaotic  every movable biome and boss in a single pool

Requirements live on the doors and never move; the only thing that follows the biome is its unlock item
(added by the mod on the destination biome). See `retarget`.
"""
from Options import OptionError

from ..data import GameData, Transition
from .requirements import parse_groups

MAX_TRIES = 500


# ── classification ───────────────────────────────────────────────────────────
def boss_biome_tiers(data: GameData) -> dict[str, int]:
    """{boss arena biome: tier} for the Tier mode, from room_rando.json (not the boss rush tiers)."""
    return {b: int(t) for t, biomes in data.room_rando["boss_tiers"].items() for b in biomes}


def normal_group(data: GameData, biome: str, tiers: dict[str, int]) -> int:
    """1 = before the tier 1 bosses, 2 = between tier 1 and 2, 3 = between tier 2 and 3."""
    override = data.room_rando["groups"].get(biome)
    if override:
        return int(override)
    first_depth = {t: min(data.biomes[b].depth for b, tt in tiers.items() if tt == t) for t in set(tiers.values())}
    return 1 + sum(1 for fd in first_depth.values() if fd < data.biomes[biome].depth)


def movable(world) -> list[str]:
    data = world.data
    fixed = set(data.room_rando["fixed"])
    return sorted(b for b in world.biome_regions if b not in fixed and data.biomes[b].depth is not None)


def pools(world, mode: str) -> list[list[str]]:
    data, biomes = world.data, movable(world)
    if mode == "chaotic":
        return [biomes]
    if mode == "depth":
        key = lambda b: data.biomes[b].depth
    else:
        tiers = boss_biome_tiers(data)
        key = lambda b: ("boss", tiers[b]) if b in tiers else ("group", normal_group(data, b, tiers))
    out: dict = {}
    for b in biomes:
        out.setdefault(key(b), []).append(b)
    return [v for _, v in sorted(out.items(), key=lambda kv: str(kv[0]))]


# ── logic follows the content ────────────────────────────────────────────────
def retarget(raw, old: str, new: str, data: GameData):
    """Requirement of a door that used to lead to `old` and now leads to `new`.
    Everything on the door is a physical obstacle of that exit (abilities, Boss Cells, boss defeated...) and stays.
    The only thing that follows the destination is the biome unlock item, a constraint added by the mod on the
    biome it loads: the unlock token of `old` becomes the unlock of `new`, if `new` has one."""
    if old == new:
        return raw
    has_unlock = any(it.unlock_for == new for it in data.items.values())
    out = []
    for group in parse_groups(raw):
        g = [tok for tok in group if tok != old]
        if has_unlock and new not in g:
            g.append(new)
        out.append(g)
    return out


def retargeted_graph(world, room_map: dict[str, str]) -> list[Transition]:
    """The biome graph (without Menu / endings) after applying the mapping."""
    present = world.biome_regions
    out = []
    for t in world.data.transitions:
        if t.src not in present or t.dst not in present:
            continue
        new = room_map.get(t.dst, t.dst)
        if new != t.src:                                           #a door back into its own biome is useless
            out.append(Transition(t.src, new, retarget(t.require, t.dst, new, world.data)))
    return out


# ── validity: nothing may become unreachable ─────────────────────────────────
def _unreachable(world, edges: list[Transition]) -> set[str]:
    """Biomes that cannot be reached even with every item (abilities/unlocks are assumed available;
    boss and region tokens, and Boss Cells, are still enforced)."""
    data, goal = world.data, world.options.boss_cells.value
    boss_at = {tok: data.locations[data.boss_location(tok)].sources[0].biome
               for toks in data.boss_tiers.values() for tok in toks}
    reached = {"PrisonStart", "Challenge", "BossRush"} & set(world.biome_regions)

    def token_ok(tok: str) -> bool:
        if tok.startswith("region:"):
            return tok[7:] in reached
        if tok.startswith("B_"):
            return tok[2:] in reached
        if tok.startswith("Boss_"):
            return boss_at.get(tok) in reached
        name, _, n = tok.rpartition(":")
        if name == "Progressive Stem Cell" or tok == "Progressive Stem Cell":
            return int(n) <= goal if n.isdigit() else goal >= 1
        return True

    changed = True
    while changed:
        changed = False
        for t in edges:
            if t.src in reached and t.dst not in reached and any(all(token_ok(k) for k in g) for g in parse_groups(t.require)):
                reached.add(t.dst)
                changed = True
    return set(world.biome_regions) - reached


def make_mapping(world) -> dict[str, str]:
    mode = world.options.room_randomizer.current_key
    identity = {b: b for b in world.biome_regions}
    if mode == "off":
        return identity
    baseline = _unreachable(world, retargeted_graph(world, identity))      #quirks of the base graph, not ours
    groups = pools(world, mode)
    for _ in range(MAX_TRIES):
        mapping = dict(identity)
        for pool in groups:
            shuffled = pool[:]
            world.random.shuffle(shuffled)
            mapping.update(zip(pool, shuffled))
        if _unreachable(world, retargeted_graph(world, mapping)) <= baseline:
            return mapping
    raise OptionError(f"Dead Cells ({world.player_name}): could not build a valid '{mode}' room randomization "
                      f"in {MAX_TRIES} tries with the current options.")
