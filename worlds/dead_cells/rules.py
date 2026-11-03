"""Attaches every access rule: entrances, then locations (source gate + rarity + rules.json)."""
from worlds.generic.Rules import set_rule

from .constants import RARITY_NEEDS_SHOWROOM, SHOWROOM, STEM_CELL
from .logic.requirements import Compiler


def _source_rule(world, name: str, in_hub: bool):
    """'Reach a drop biome with enough Boss Cells' - one alternative per gate (min_bc, depth, biomes).
    Bank gates additionally need a biome of the depth the Bank replaces; other gates never do.
    Logic only uses min_bc (monotonic): max_bc is informational."""
    player, depth_regions = world.player, world.depth_regions
    gates = world.location_gates[name]
    if not in_hub and len(gates) == 1 and gates[0].min_bc == 0 and not gates[0].depths:
        return None                                         #the region itself is the whole condition

    def reach_depth(state, depths):
        return any(state.can_reach_region(r, player) for d in depths for r in depth_regions.get(d, ()))

    def gate_ok(state, g, bc):
        return (bc >= g.min_bc
                and (not in_hub or any(state.can_reach_region(b, player) for b in g.biomes))
                and (not g.depths or reach_depth(state, g.depths)))

    def rule(state):
        bc = state.count(STEM_CELL, player)
        return any(gate_ok(state, g, bc) for g in gates)
    return rule


def _all(preds):
    preds = [p for p in preds if p]
    if not preds:
        return None
    if len(preds) == 1:
        return preds[0]
    return lambda state: all(p(state) for p in preds)


def set_rules(world) -> None:
    mw, player, data = world.multiworld, world.player, world.data
    compiler = Compiler(world, data)

    for entrance, raw in world.entrance_requirements:
        c = compiler.compile(raw)
        if c.rule:
            set_rule(entrance, c.rule)
        for region in c.regions:                            #entrance depends on another region's reachability
            mw.register_indirect_condition(mw.get_region(region, player), entrance)

    hub = world.get_region("Checks")
    for loc in mw.get_locations(player):
        d = data.locations[loc.name]
        parts = [_source_rule(world, loc.name, loc.parent_region is hub)]
        if d.rarity in RARITY_NEEDS_SHOWROOM:
            parts.append(lambda state: state.has(SHOWROOM, player))
        if loc.name in data.rules:
            parts.append(compiler.compile(data.rules[loc.name]).rule)
        rule = _all(parts)
        if rule:
            set_rule(loc, rule)

    mw.completion_condition[player] = lambda state: state.can_reach_region("End", player)
