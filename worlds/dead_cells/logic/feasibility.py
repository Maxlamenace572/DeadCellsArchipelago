"""Static pruning: drop locations whose rule can *never* be satisfied with the content of this seed.

Only things that are decidable from what exists are checked (no item reasoning):
    loc:X       X must exist          region:X   region must exist       depth:N  a biome of depth N must exist
    count:K:N   at least N existing locations of kind K (a location never counts itself)
    tier:T:N    at least N existing bosses of boss-rush tier T
Removing a location can make another one infeasible, so this runs to a fixed point.
"""
from ..data import GameData, LocationDef
from .requirements import parse_groups


def _feasible(raw, existing: dict[str, LocationDef], regions: set[str], data: GameData) -> bool:
    types_by_kind = {k: set(v) for k, v in data.count_kinds.items()}
    boss_locs = {t: {data.boss_location(b) for b in bosses} for t, bosses in data.boss_tiers.items()}

    def token_ok(tok: str) -> bool:
        if tok.startswith("@"):
            return _feasible(data.macros[tok[1:]], existing, regions, data)
        kind, _, rest = tok.partition(":")
        if kind == "loc":
            return rest in existing
        if kind == "region" or tok.startswith("B_"):
            return (rest if kind == "region" else tok[2:]) in regions
        if kind == "depth":
            return any(b.depth == int(rest) and b.id in regions for b in data.biomes.values())
        if kind == "count":
            k, n = rest.split(":")
            skip = data.count_excluded(k)
            return sum(1 for name, d in existing.items() if d.type in types_by_kind[k] and name not in skip) >= int(n)
        if kind == "tier":
            t, n = rest.split(":")
            return sum(1 for name in boss_locs[t] if name in existing) >= int(n)
        return True                 #item tokens: not decidable here

    return any(all(token_ok(t) for t in group) for group in parse_groups(raw))


def prune_infeasible(world, existing: dict[str, LocationDef]) -> list[str]:
    """Removes impossible locations from `existing` in place; returns their names."""
    data, regions = world.data, set(world.biome_regions)
    removed: list[str] = []
    changed = True
    while changed:
        changed = False
        for name in [n for n in existing if n in data.rules]:
            if not _feasible(data.rules[name], existing, regions, data):
                del existing[name]
                removed.append(name)
                changed = True
    return removed
