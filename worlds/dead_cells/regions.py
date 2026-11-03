"""Builds the region graph from regions.json (+ world_extra.json). Rules are attached in rules.py."""
from BaseClasses import Entrance, Region

from .constants import HUB_REGION, STEM_CELL
from .data import Biome, Transition
from .locations import create_locations
from .logic import room_rando
from .logic.requirements import parse_groups


def biome_enabled(world, b: Biome) -> bool:
    if b.dlc and b.dlc not in world.enabled_dlcs:
        return False
    if b.min_bc > world.options.boss_cells.value:
        return False
    if b.id == "Distillery" and world.options.exclude_distillery:
        return False
    return True


def _edges(world) -> list[Transition]:
    data, goal = world.data, world.options.boss_cells.value
    edges = list(data.menu_transitions) + room_rando.retargeted_graph(world, world.room_map)
    #at the top BC only the Observatory ending counts (generate_early guarantees Rise of the Giant is enabled).
    pruned = data.true_ending["sources_pruned"] if goal == data.true_ending["bc"] else []
    need = [f"{STEM_CELL}:{goal}"] if goal else []
    edges += [Transition(src, "End", [group + need for group in parse_groups(req)])
                for src, req in data.endings.items() if src not in pruned]
    return edges


def create_regions(world) -> None:
    mw, player = world.multiworld, world.player
    plain = {name: Region(name, player, mw) for name in ("Menu", HUB_REGION, "End")}
    world.biome_regions = {b.id: Region(b.id, player, mw)
                           for b in world.data.biomes.values() if biome_enabled(world, b)}
    world.room_map = room_rando.make_mapping(world)    #identity unless the room randomizer is on
    #depth -> biomes met at that depth of a run. The Bank replaces the biome of the current depth, so what counts is
    #the *position* (original destination) and the content found there is room_map[position].
    world.depth_regions = {}
    for b in world.data.biomes.values():
        if b.id in world.biome_regions and b.depth is not None:
            world.depth_regions.setdefault(b.depth, []).append(world.room_map[b.id])
    regions = {**plain, **world.biome_regions}
    mw.regions += regions.values()

    plain["Menu"].connect(plain[HUB_REGION], "Menu -> Checks")
    world.entrance_requirements = []
    for t in _edges(world):
        if t.src in regions and t.dst in regions:
            entrance = regions[t.src].connect(regions[t.dst], f"{t.src} -> {t.dst}")
            world.entrance_requirements.append((entrance, t.require))

    create_locations(world)
