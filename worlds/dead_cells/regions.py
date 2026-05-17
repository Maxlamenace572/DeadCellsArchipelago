"""
Dead Cells - Archipelago World
regions.py

Defines all biome regions, their locations, and the connections between them.
"""

from typing import TYPE_CHECKING
from BaseClasses import Region, Entrance
from .locations import DeadCellsLocation, LOCATION_TABLE, location_id
from worlds.generic.Rules import set_rule
from .rules import get_bc_level

if TYPE_CHECKING:
    from . import DeadCellsWorld


ALL_REGIONS = [
    "Menu",
    "PrisonStart", "PrisonCourtyard", "SewerShort", "PrisonDepths",
    "PrisonCorrupt", "PrisonRoof", "Ossuary", "SewerDepths",
    "Bridge", "BeholderPit", "StiltVillage", "AncientTemple",
    "Cemetery", "ClockTower", "Crypt", "TopClockTower",
    "Castle", "Distillery", "Throne",
    "Bank", "Challenge",
    "Cavern", "Giant", "Astrolab", "Observatory",
    "Greenhouse", "Swamp", "SwampHeart",
    "Tumulus", "Cliff", "GardenerStage",
    "Shipwreck", "Lighthouse", "QueenArena",
    "PurpleGarden", "DookuCastle", "DookuCastleHard",
    "DeathArena", "DookuArena",
    "Checks",
    "End",
]

BOSS_LOCATION = {
    "Behemoth":       "The Concierge",
    "Beholder":       "Conjunctivius",
    "TimeKeeper":     "The Time Keeper",
    "KingsHand":      "The Hand of the King",
    "Giant":          "The Giant",
    "Collector":      "The Collector",
    "MamaTick":       "Mama Tick",
    "GardenerBoss":   "Scarecrow",
    "AmazonSurvival": "Calliope",
    "AmazonTactic":   "Euterpe",
    "AmazonBrutal":   "Kleio",
    "Queen":          "The Queen",
    "Death":          "Death",
    "DookuBeast":     "Dracula",
}

REGION_DLC = {
    "Cavern":          "RiseOfTheGiant",
    "Giant":           "RiseOfTheGiant",
    "Astrolab":        "RiseOfTheGiant",
    "Observatory":     "RiseOfTheGiant",
    "Greenhouse":      "TheBadSeed",
    "Swamp":           "TheBadSeed",
    "SwampHeart":      "TheBadSeed",
    "Tumulus":         "FatalFalls",
    "Cliff":           "FatalFalls",
    "GardenerStage":   "FatalFalls",
    "Shipwreck":       "TheQueenAndTheSea",
    "Lighthouse":      "TheQueenAndTheSea",
    "QueenArena":      "TheQueenAndTheSea",
    "PurpleGarden":    "Purple",
    "DookuCastle":     "Purple",
    "DookuCastleHard": "Purple",
    "DeathArena":      "Purple",
    "DookuArena":      "Purple",
}




TRANSITIONS = {
    "Menu": [
        {"to": "PrisonStart", "require": None},
        {"to": "Challenge", "require": None},
    ],
    "PrisonStart": [
        {"to": "PrisonCourtyard", "require": None},
        {"to": "SewerShort", "require": "Vine Rune"},
        {"to": "Greenhouse", "require": ["Teleportation Rune", "Dilapidated Arboretum Unlock"]},
        {"to": "PurpleGarden", "require": "Castle Outskirts Unlock"}
    ],
    "Greenhouse": [
        {"to": "PrisonDepths", "require": ["Spider Rune", "Prison Depths Unlock"]},
        {"to": "Swamp",        "require": "Morass of the Banished Unlock"},
        {"to": "PrisonRoof",   "require": None}
    ],
    "PrisonCourtyard": [
        {"to": "Ossuary", "require": ["Vine Rune", "Teleportation Rune", "Ossuary Unlock"]},
        {"to": "PrisonRoof", "require": "Vine Rune"},
        {"to": "PrisonDepths", "require": ["Spider Rune", "Vine Rune", "Prison Depths Unlock"]},
    ],
    "SewerShort": [
        {"to": "PrisonCorrupt", "require": ["Spider Rune", "Corrupted Prison Unlock"]},
        {"to": "PrisonRoof", "require": None},
        {"to": "SewerDepths", "require": ["Ram Rune", "Ancient Sewers Unlock"]},
    ],
    "PrisonDepths": [
        {"to": "Ossuary", "require": "Ossuary Unlock"},
        {"to": "SewerDepths", "require": ["Progressive Stem Cell", "Ancient Sewers Unlock"]},
    ],
    "PrisonCorrupt": [
        {"to": "SewerDepths", "require": "Ancient Sewers Unlock"},
        {"to": "PrisonRoof", "require": "Progressive Stem Cell"},
    ],
    "PrisonRoof": [
        {"to": "Bridge", "require": None},
        {"to": "BeholderPit", "require": ["Progressive Stem Cell:3", "Insufferable Crypt Unlock"]},
    ],
    "Ossuary": [
        {"to": "Bridge", "require": None}
    ],
    "SewerDepths": [
        {"to": "BeholderPit", "require": "Insufferable Crypt Unlock"}
    ],
    "Bridge": [
        {"to": "Tumulus", "require": "Fractured Shrines Unlock"},
        {"to": "StiltVillage", "require": "Stilt Village Unlock"},
        {"to": "AncientTemple", "require": ["Spider Rune", "Slumbering Sanctuary Unlock"]}
    ],
    "BeholderPit": [
        {"to": "AncientTemple", "require": "Slumbering Sanctuary Unlock"},
        {"to": "Cemetery", "require": ["Spider Rune", "Graveyard Unlock"]}
    ],
    "StiltVillage": [
        {"to": "ClockTower", "require": "Clock Tower Unlock"},
        {"to": "Crypt", "require": ["Teleportation Rune", "Forgotten Sepulcher Unlock"]}
    ],
    "AncientTemple": [
        {"to": "ClockTower", "require": "Clock Tower Unlock"},
        {"to": "Crypt", "require": ["Teleportation Rune", "Forgotten Sepulcher Unlock"]}
    ],
    "Cemetery": [
        {"to": "Crypt", "require": ["Teleportation Rune", "Forgotten Sepulcher Unlock"]},
        {"to": "Cavern", "require": ["Homunculus Rune", "Cavern Unlock", "Hand of the King Defeated"]} #So damn close to just mapping every individual Cavern/Giant location to it's own logic
    ],
    "ClockTower": [
        {"to": "TopClockTower", "require": "Clock Room Unlock"},
    ],
    "Crypt": [
        {"to": "TopClockTower", "require": "Clock Room Unlock"},
    ],
    "TopClockTower": [
        {"to": "Shipwreck", "require": ["Crowned Key", "Infested Shipwreck Unlock"]},
        {"to": "Castle", "require": "High Peak Castle Unlock"},
        {"to": "DookuCastleHard", "require": [["Death Defeated", "Vine Rune"], ["Death Defeated", "Teleportation Rune", "Dilapidated Arboretum Unlock"]]}, ###Flag for future proper Event### #Technically cannot be done if routed exclusively from Castlevania biomes?
    ],
    "Cavern": [
        {"to": "Giant", "require": "Guardian's Haven Unlock"},
    ],
    "Giant": [
        {"to": "Shipwreck", "require": ["Crowned Key", "Infested Shipwreck Unlock"]},
        {"to": "Castle", "require": "High Peak Castle Unlock"},
        {"to": "Throne", "require": "Throne Room Unlock"},
    ],
    "Castle": [
        {"to": "Throne", "require": "Throne Room Unlock"},
    ],
    "Distillery": [
        {"to": "Throne", "require": "Throne Room Unlock"},
    ],
    "Throne": [
        {"to": "Astrolab", "require": ["Progressive Stem Cell:5", "Astrolab Unlock"]},
        {"to": "Bank", "require": None},
        {"to": "End", "require": "Homunculus Rune"},
        {"to": "Distillery", "require": "Derelict Distillery Unlock"},
    ],
    "Astrolab": [
        {"to": "Observatory", "require": "Observatory Unlock"},
    ],
    "Observatory": [
        {"to": "End", "require": None},
    ],
    "Swamp": [
        {"to": "SwampHeart", "require": "Nest Unlock"},
    ],
    "SwampHeart": [
        {"to": "StiltVillage", "require": "Stilt Village Unlock"},
        {"to": "Cemetery", "require": ["Spider Rune", "Graveyard Unlock"]},
        {"to": "Tumulus", "require": "Fractured Shrines Unlock"},
    ],
    "Tumulus": [
        {"to": "ClockTower", "require": "Clock Tower Unlock"},
        {"to": "Crypt", "require": ["Teleportation Rune", "Forgotten Sepulcher Unlock"]},
        {"to": "Cliff", "require": [["Cultist Outfit", "Undying Shores Unlock"], ["Undying Shores Unlock", "Homunculus Rune"]]},
    ],
    "Cliff": [
        {"to": "GardenerStage", "require": "Mausoleum Unlock"},
    ],
    "GardenerStage": [
        {"to": "Shipwreck", "require": ["Crowned Key", "Infested Shipwreck Unlock"]},
        {"to": "Castle", "require": "High Peak Castle Unlock"},
    ],
    "Shipwreck": [
        {"to": "Lighthouse", "require": "Lighthouse Unlock"},
    ],
    "Lighthouse": [
        {"to": "QueenArena", "require": "Crown Unlock"},
    ],
    "QueenArena": [
        {"to": "End", "require": None},
        {"to": "Bank", "require": None},
    ],
    "PurpleGarden": [
        {"to": "DookuCastle", "require": "Dracula's Castle Unlock"},
        {"to": "Ossuary", "require": ["Teleportation Rune", "Ossuary Unlock", "Dracula Defeated"]}
    ],
    "DookuCastle": [
        {"to": "Bridge", "require": "Dracula Defeated"},
        {"to": "DeathArena", "require": "Defiled Necropolis Unlock"},
    ],
    "DookuCastleHard": [
        {"to": "DookuArena", "require": "Master's Keep Unlock"},
    ],
    "DeathArena": [
        {"to": "Cemetery", "require": ["Spider Rune", "Graveyard Unlock"]},
        {"to": "StiltVillage", "require": "Stilt Village Unlock"},
        {"to": "AncientTemple", "require": ["Spider Rune", "Slumbering Sanctuary Unlock"]},
    ],
    "DookuArena": [
        {"to": "End", "require": None},
    ],
    "Bank": [],
    "Challenge": [],
}

def _has_boss_kill(state, player: int, boss: str) -> bool:
    return state.can_reach_location(BOSS_LOCATION[boss], player)


def _has_biome_enter(state, player: int, biome: str) -> bool:
    return state.can_reach_location(f"{biome}_Enter", player)


def _check_name(state, player: int, name: str) -> bool:
    if name in BOSS_LOCATION:
        return _has_boss_kill(state, player, name)

    return state.has(name, player)


def build_rule(requirements, world: "DeadCellsWorld"):
    player = world.player

    def get_stem_cells(state):
        return (
            state.count("Progressive Stem Cell", player)
            + state.count("ProgBossRune", player)
        )

    def check_req(req, state):
        if req is None:
            return True

        if isinstance(req, str):
            if ":" in req:
                key, value = req.split(":", 1)

                if key == "BSC":
                    return get_stem_cells(state) >= int(value)

                if key == "Boss":
                    return _has_boss_kill(state, player, value)

                if key == "Biome":
                    return _has_biome_enter(state, player, value)

                if key == "Region":
                    return state.can_reach(value, "Region", player)

                return state.count(key, player) >= int(value)

            return _check_name(state, player, req)

        if isinstance(req, dict) and "or" in req:
            return any(check_req(option, state) for option in req["or"])

        if isinstance(req, list):
            if any(isinstance(x, list) for x in req):
                return any(check_req(group, state) for group in req)
            return all(check_req(part, state) for part in req)

        return True

    return lambda state: check_req(requirements, state)


RARITY_BC_REQUIREMENTS = {
    "Rare": 2,
    "Legendary": 3,
}


def _inject_rarity_into_sources(loc_data):
    """
    Copy location-level rarity into each source entry, since source data
    is what this world uses for logic.
    """
    rarity = loc_data.get("rarity")
    sources = loc_data.get("sources", [])

    if not rarity:
        return [dict(s) for s in sources]

    return [{**dict(s), "rarity": s.get("rarity", rarity)} for s in sources]


def _source_meets_rarity(state, player, source):
    """
    Only Rare and Legendary require Specialist's Showroom.
    """
    return (
        source.get("rarity") not in ("Rare", "Legendary")
        or state.has("The Specialist's Showroom", player)
    )

def create_regions(world: "DeadCellsWorld") -> None:
    world.created_locations = set()
    enabled_dlcs: set = world.enabled_dlcs
    max_seed_bc: int = world.options.boss_cells.value
    player: int = world.player
    multiworld = world.multiworld

    bc_gated_regions = {
        "Astrolab": 5,
        "Observatory": 5,
    }

    regions = {}
    for name in ALL_REGIONS:
        dlc = REGION_DLC.get(name, "")
        if dlc and dlc not in enabled_dlcs:
            continue

        # Only skip regions that can never exist in this seed
        min_bc_required = bc_gated_regions.get(name, 0)
        if min_bc_required > max_seed_bc:
            continue

        region = Region(name, player, multiworld)
        regions[name] = region
        multiworld.regions.append(region)

    for loc_name, loc_data in LOCATION_TABLE.items():
        region_name = loc_data["region"]

        if region_name not in regions:
            continue

        loc_dlc = loc_data.get("dlc", "")
        if loc_dlc and loc_dlc not in enabled_dlcs:
            continue

        if loc_data["type"] in ("skin", "head") and not world.options.include_cosmetics.value:
            continue

        loc_id = location_id(loc_name)

        base_sources = _inject_rarity_into_sources(loc_data)

        if hasattr(world, "grouped_location_sources") and loc_id in world.grouped_location_sources:
            grouped_sources = world.grouped_location_sources[loc_id]
            rarity = loc_data.get("rarity")

            if rarity:
                sources = []
                for s in grouped_sources:
                    s2 = dict(s)
                    s2.setdefault("rarity", rarity)
                    sources.append(s2)
            else:
                sources = [dict(s) for s in grouped_sources]
        else:
            sources = base_sources

        # IMPORTANT:
        # Do NOT filter by current BC progression here.
        # Only keep sources that are structurally possible in this seed.
        valid_sources = [
            s for s in sources
            if (s.get("dlc", "") == "" or s.get("dlc", "") in enabled_dlcs)
            and s.get("biome") in regions
            and s.get("min_bc", 0) <= max_seed_bc
        ]

        if not valid_sources:
            continue

        loc = DeadCellsLocation(
            player,
            loc_name,
            loc_id,
            regions[region_name],
        )
        regions[region_name].locations.append(loc)
        world.created_locations.add(loc_name)

        extra_rule = build_rule(loc_data.get("requires"), world) if loc_data.get("requires") else None

        def make_rule(source_data, extra_rule):
            def rule(state):
                bc = get_bc_level(state, player)

                source_ok = any(
                    (s.get("dlc", "") == "" or s.get("dlc", "") in enabled_dlcs)
                    and s.get("biome") in regions
                    and state.can_reach(s["biome"], "Region", player)
                    and s.get("min_bc", 0) <= bc <= s.get("max_bc", 5)
                    and _source_meets_rarity(state, player, s)
                    for s in source_data
                )

                return source_ok and extra_rule(state) if extra_rule else source_ok

            return rule

        set_rule(loc, make_rule(valid_sources, extra_rule))

    for from_region, exits in TRANSITIONS.items():
        if from_region not in regions:
            continue

        for exit_data in exits:
            to_region = exit_data["to"]
            requirement = exit_data.get("require")

            if to_region not in regions:
                continue

            entrance = Entrance(player, f"{from_region} -> {to_region}", regions[from_region])
            regions[from_region].exits.append(entrance)
            entrance.connect(regions[to_region])

            if requirement is not None:
                set_rule(entrance, build_rule(requirement, world))

    checks_region = regions.get("Checks")
    if checks_region:
        for biome_name in list(regions.keys()):
            if biome_name in ("Menu", "End", "Checks"):
                continue

            entrance = Entrance(player, f"{biome_name} -> Checks", regions[biome_name])
            entrance.access_rule = lambda state, b=biome_name: state.can_reach(b, "Region", player)
            regions[biome_name].exits.append(entrance)
            entrance.connect(checks_region)