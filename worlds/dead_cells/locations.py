"""Which locations exist in this seed, and where they live in the region graph."""
from .base_classes import DeadCellsLocation
from .constants import HUB_REGION, LOCATION_BASE_ID
from .data import LocationDef, Source, gates_of
from .logic.feasibility import prune_infeasible

COSMETIC_LOCATION_TYPES = {"skin", "head", "cos_dependant"}


def valid_sources(world, loc: LocationDef) -> list[Source]:
    """Sources that can actually happen in this seed: DLC on, biome exists, BC within the goal,
    and (Bank only) a biome of the required depth exists."""
    goal = world.options.boss_cells.value
    return [s for s in loc.sources
            if (not s.dlc or s.dlc in world.enabled_dlcs)
            and s.biome in world.biome_regions
            and s.min_bc <= goal
            and (not s.depths or any(d in world.depth_regions for d in s.depths))]


def location_enabled(world, loc: LocationDef) -> bool:
    o = world.options
    if loc.dlc and loc.dlc not in world.enabled_dlcs:
        return False
    if loc.type == "aspect" and not o.include_aspects:
        return False
    if loc.type == "enemy" and not o.enemy_sanity:
        return False
    if loc.type in COSMETIC_LOCATION_TYPES and not o.include_cosmetics:
        return False
    return bool(valid_sources(world, loc))


def create_locations(world) -> None:
    """1) keep what is enabled, 2) drop what can never be reached (boss-rush tiers, counters...),
    3) place each location in its biome when it has a single one, otherwise in the hub.
    The BC / depth / multi-biome condition is attached later in rules.py (world.location_gates)."""
    existing = {l.name: l for l in world.data.locations.values() if location_enabled(world, l)}
    world.pruned_locations = prune_infeasible(world, existing)

    hub = world.get_region(HUB_REGION)
    world.location_gates = {}
    for loc in existing.values():
        sources = valid_sources(world, loc)
        biomes = {s.biome for s in sources}
        region = world.biome_regions[next(iter(biomes))] if len(biomes) == 1 else hub
        region.locations.append(DeadCellsLocation(world.player, loc.name, LOCATION_BASE_ID + loc.id, region))
        world.location_gates[loc.name] = gates_of(sources)
