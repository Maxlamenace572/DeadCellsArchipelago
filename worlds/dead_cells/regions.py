"""
Dead Cells - Archipelago World
regions.py

Defines all biome regions, their locations, and the connections between them.
Connections encode access rules based on:
  - Runes (AP items in inventory)
  - Boss kills (AP location checks completed)
  - Biome visits (biome_enter check completed)
  - AP items (Cultist skin, LighthouseKey)
  - Boss Cell difficulty (world option)
"""

from typing import TYPE_CHECKING, List
from BaseClasses import Region, Entrance
from .locations import DeadCellsLocation, LOCATION_TABLE, location_id
from worlds.generic.Rules import set_rule
from .rules import get_bc_level

if TYPE_CHECKING:
    from . import DeadCellsWorld


# ─────────────────────────────────────────────────────────────────────────────
# All biome region names (including Menu and End as AP convention)
# ─────────────────────────────────────────────────────────────────────────────
ALL_REGIONS = [
    "Menu",
    # Base game
    "PrisonStart", "PrisonCourtyard", "SewerShort", "PrisonDepths",
    "PrisonCorrupt", "PrisonRoof", "Ossuary", "SewerDepths",
    "Bridge", "BeholderPit", "StiltVillage", "AncientTemple",
    "Cemetery", "ClockTower", "Crypt", "TopClockTower",
    "Castle", "Distillery", "Throne",
    "Bank", "Challenge",
    # Rise of the Giant
    "Cavern", "Giant", "Astrolab", "Observatory",
    # The Bad Seed
    "Greenhouse", "Swamp", "SwampHeart",
    # Fatal Falls
    "Tumulus", "Cliff", "GardenerStage",
    # The Queen and the Sea
    "Shipwreck", "Lighthouse", "QueenArena",
    # Return to Castlevania
    "PurpleGarden", "DookuCastle", "DookuCastleHard",
    "DeathArena", "DookuArena",
    # Virtual region for grouped blueprint checks
    "Checks",
    # Victory
    "End",
]

# ─────────────────────────────────────────────────────────────────────────────
# Boss -> location name mapping (for boss kill rules)
# ─────────────────────────────────────────────────────────────────────────────
BOSS_LOCATION = {
    "Behemoth":      "Boss_Behemoth",
    "Beholder":      "Boss_Beholder",
    "TimeKeeper":    "Boss_TimeKeeper",
    "KingsHand":     "Boss_KingsHand",
    "Giant":         "Boss_Giant",
    "Collector":     "Boss_Collector",
    "MamaTick":      "Boss_MamaTick",
    "GardenerBoss":  "Boss_GardenerBoss",
    "AmazonSurvival":"Boss_AmazonSurvival",
    "AmazonTactic":  "Boss_AmazonTactic",
    "AmazonBrutal":  "Boss_AmazonBrutal",
    "Queen":         "Boss_Queen",
    "Death":         "Boss_Death",
    "DookuBeast":    "Boss_DookuBeast",
}

# ─────────────────────────────────────────────────────────────────────────────
# BSC level string -> minimum boss_cells option value
# ─────────────────────────────────────────────────────────────────────────────
BSC_LEVEL = {
    "bsc1": 1, "bsc2": 2, "bsc3": 3, "bsc4": 4, "bsc5": 5,
}


# ─────────────────────────────────────────────────────────────────────────────
# Rule builder helpers
# ─────────────────────────────────────────────────────────────────────────────

def _has_item(state, player: int, item: str) -> bool:
    return state.has(item, player)

def _has_boss_kill(state, player: int, boss: str) -> bool:
    loc = BOSS_LOCATION[boss]
    return state.can_reach_location(loc, player)

def _has_biome_enter(state, player: int, biome: str) -> bool:
    loc = f"{biome}_Enter"
    return state.can_reach_location(loc, player)

def _has_bsc(state, player, level):
    return state.count("ProgBossRune", player) >= level


def build_rule(requires, world: "DeadCellsWorld"):
    """
    Enhanced rule builder.

    Supports:
      - "ItemName" → has item
      - ["A", "B"] → AND
      - {"or": [...]} → OR
      - "ItemName:3" → progressive count (state.count >= 3)
      - "Boss:Name" → boss kill
      - "Biome:Name" → biome enter
      - "BSC:level" → boss cell requirement
    """

    if requires is None:
        return lambda state: True

    if isinstance(requires, str):
        requires = [requires]

    player = world.player

    def parse(req):
        # ── Progressive item (ItemName:count) ──
        if ":" in req:
            key, value = req.split(":", 1)

            # Boss Cell requirement
            if key == "BSC":
                level = int(value)
                return lambda state: state.count("ProgBossRune", player) >= level

            # Boss kill
            if key == "Boss":
                return lambda state: _has_boss_kill(state, player, value)

            # Biome enter
            if key == "Biome":
                return lambda state: _has_biome_enter(state, player, value)

            # Progressive item count
            count = int(value)
            return lambda state: state.count(key, player) >= count

        # ── Simple item ──
        return lambda state: state.has(req, player)

    # ── OR support ──
    if isinstance(requires, dict) and "or" in requires:
        rules = [parse(r) for r in requires["or"]]
        return lambda state: any(rule(state) for rule in rules)

    # ── AND (default) ──
    rules = [parse(r) for r in requires]
    return lambda state: all(rule(state) for rule in rules)

def build_transition_rule(requirement, world, player):

    def parse(req, state):
        # Handle "Item:count"
        if isinstance(req, str) and ":" in req:
            name, count = req.split(":")
            return state.has(name, player, int(count))

        # Handle single item
        if isinstance(req, str):
            return state.has(req, player)

        return False

    def rule(state):
        # List = AND logic
        if isinstance(requirement, list):
            return all(parse(r, state) for r in requirement)

        return parse(requirement, state)

    return rule


# ─────────────────────────────────────────────────────────────────────────────
# Transition table
# Encoded directly from transition.json
# ─────────────────────────────────────────────────────────────────────────────
TRANSITIONS = {
    "Menu": [
        {"to": "PrisonStart", "require": None},
        {"to": "Challenge",   "require": None},
    ],
    "PrisonStart": [
        {"to": "PrisonCourtyard", "require": None},
        {"to": "SewerShort",      "require": "LadderKey"},
        {"to": "Greenhouse",      "require": ["TeleportKey","Dilapidated Arboretum"]},
        {"to": "PurpleGarden",    "require": "Castle Outskirts"},
    ],
    "PrisonCourtyard": [
        {"to": "Ossuary",      "require": ["TeleportKey", "Ossuary"]},
        {"to": "PrisonRoof",   "require": "LadderKey"},
        {"to": "PrisonDepths", "require": ["WallJumpKey", "Prison Depths"]},
        {"to": "Swamp",        "require": ["TeleportKey", "Morass of the Condemned"]},
    ],
    "SewerShort": [
        {"to": "PrisonCorrupt", "require": ["WallJumpKey", "Corrupted Prison"]},
        {"to": "PrisonRoof",    "require": None},
        {"to": "SewerDepths",   "require": ["BreakableGroundKey", "Ancient Sewers"]},
        {"to": "DookuCastle",   "require": ["DookuBeast", "Draclua's Castle"]},
    ],
    "PrisonDepths": [
        {"to": "Ossuary",    "require": "Ossuary"},
        {"to": "SewerDepths","require": ["ProgBossRune", "Ancient Sewers"]},
        {"to": "Swamp",      "require": ["TeleportKey","Morass of the Condemned"]},
    ],
    "PrisonCorrupt": [
        {"to": "SewerDepths", "require": "Ancient Sewers"},
        {"to": "PrisonRoof",  "require": "ProgBossRune"},
        {"to": "DookuCastle", "require": ["DookuBeast", "Draclua's Castle"]},
    ],
    "PrisonRoof": [
        {"to": "Bridge",     "require": None},
        {"to": "BeholderPit","require": ["ProgBossRune:3", "Insufferable Crypt"]},
    ],
    "Ossuary": [
        {"to": "Bridge",    "require": None},
        {"to": "DeathArena","require": ["DookuBeast","Defiled Necropolis"]},
    ],
    "SewerDepths": [
        {"to": "BeholderPit", "require": "Insufferable Crypt"},
    ],
    "Bridge": [
        {"to": "Tumulus",      "require": "Fractured Shrines"},
        {"to": "StiltVillage", "require": "Stilt Village"},
        {"to": "AncientTemple","require": ["WallJumpKey", "Slumbering Sanctuary"]},
    ],
    "BeholderPit": [
        {"to": "AncientTemple","require": "Slumbering Sanctuary"},
        {"to": "Cemetery",     "require": ["WallJumpKey", "Graveyard"]},
    ],
    "StiltVillage": [
        {"to": "Cliff",      "require": ["Cultist", "Undying Shores"]},
        {"to": "ClockTower", "require": "Clock Tower"},
        {"to": "Crypt",      "require": ["TeleportKey", "Forgotten Sepulcher"]},
    ],
    "AncientTemple": [
        {"to": "Cavern",     "require": ["Giant", "ProgBossRune:2", "Cavern"]},
        {"to": "ClockTower", "require": "Clock Tower"},
        {"to": "Crypt",      "require": ["TeleportKey", "Forgotten Sepulcher"]},
    ],
    "Cemetery": [
        {"to": "Cliff",   "require": ["Cultist", "Undying Shores"]},
        {"to": "Cavern",  "require": ["HomKey", "Cavern"]},
        {"to": "Crypt",   "require": ["TeleportKey", "Forgotten Sepulcher"]},
    ],
    "ClockTower": [
        {"to": "TopClockTower", "require": "Clock Room"},
    ],
    "Crypt": [
        {"to": "TopClockTower", "require": "Clock Room"},
        {"to": "Giant",         "require": ["Giant", "ProgBossRune:2", "Guardian's Haven"]},
    ],
    "TopClockTower": [
        {"to": "Shipwreck",      "require": ["LighthouseKey", "Infested Shipwreck"]},
        {"to": "Distillery",     "require": "Derelict Distillery"},
        {"to": "Castle",         "require": "High Peak Castle"},
        {"to": "DookuCastleHard","require": ["Death", "Draclua's Castle"]},
    ],
    "Cavern": [
        {"to": "GardenerStage", "require": ["GardenerBoss", "Mausoleum"]},
        {"to": "Giant",         "require": "Guardian's Haven"},
    ],
    "Giant": [
        {"to": "Shipwreck",      "require": ["LighthouseKey", "Infested Shipwreck"]},
        {"to": "Distillery",     "require": "Derelict Distillery"},
        {"to": "Castle",         "require": "High Peak Castle"},
        {"to": "DookuCastleHard","require": ["DookuBeast", "Draclua's Castle"]},
        {"to": "Throne",         "require": "Throne Room"},
    ],
    "Castle": [
        {"to": "DookuArena", "require": ["DookuBeast","Draclua's Castle"]},
        {"to": "Throne",     "require": "Throne Room"},
    ],
    "Distillery": [
        {"to": "Lighthouse", "require": ["AmazonSurvival", "AmazonTactic", "AmazonBrutal", "Lighthouse"]},
        {"to": "Throne",     "require": "Throne Room"},
    ],
    "Throne": [
        {"to": "Astrolab", "require": ["ProgBossRune:5", "Astrolab"]},
        {"to": "Bank",     "require": None},
        {"to": "End",      "require": None},
    ],
    "Astrolab": [
        {"to": "Observatory", "require": "Observatory"},
    ],
    "Observatory": [
        {"to": "End", "require": None},
    ],
    "Swamp": [
        {"to": "SwampHeart", "require": "Nest"},
    ],
    "SwampHeart": [
        {"to": "StiltVillage", "require": "Stilt Village"},
        {"to": "Cemetery",     "require": ["WallJumpKey", "Graveyard"]},
        {"to": "Tumulus",      "require": "Fractured Shrines"},
    ],
    "Tumulus": [
        {"to": "Cliff",      "require": ["Cultist", "Undying Shores"]},
        {"to": "ClockTower", "require": "Clock Tower"},
        {"to": "Crypt",      "require": ["TeleportKey", "Forgotten Sepulcher"]},
    ],
    "Cliff": [
        {"to": "GardenerStage", "require": "Mausoleum"},
    ],
    "GardenerStage": [
        {"to": "Shipwreck",      "require": ["LighthouseKey", "Infested Shipwreck"]},
        {"to": "Distillery",     "require": "Derelict Distillery"},
        {"to": "Castle",         "require": "High Peak Castle"},
        {"to": "DookuCastleHard","require": ["DookuBeast", "Draclua's Castle"]},
    ],
    "Shipwreck": [
        {"to": "Lighthouse", "require": "Lighthouse"},
    ],
    "Lighthouse": [
        {"to": "QueenArena", "require": "Crown"},
    ],
    "QueenArena": [
        {"to": "End", "require": None},
    ],
    "PurpleGarden": [
        {"to": "PrisonCorrupt","require": ["WallJumpKey", "DookuBeast", "Corrupted Prison"]},
        {"to": "DookuCastle",  "require": "Draclua's Castle"},
        {"to": "Ossuary",      "require": ["TeleportKey", "DookuBeast", "Ossuary"]},
    ],
    "DookuCastle": [
        {"to": "Bridge",    "require": "DookuBeast"},
        {"to": "DeathArena","require": "Defiled Necropolis"},
    ],
    "DookuCastleHard": [
        {"to": "DookuArena", "require": "Master's Keep"},
    ],
    "DeathArena": [
        {"to": "Cemetery",     "require": ["WallJumpKey", "Graveyard"]},
        {"to": "StiltVillage", "require": "Stilt Village"},
        {"to": "AncientTemple","require": ["WallJumpKey", "Slumbering Sanctuary"]},
    ],
    "DookuArena": [
        {"to": "End", "require": None},
    ],
    "Bank":      [],
    "Challenge": [],
}


# ─────────────────────────────────────────────────────────────────────────────
# DLC membership for region filtering
# ─────────────────────────────────────────────────────────────────────────────
REGION_DLC = {
    "Cavern":         "RiseOfTheGiant",
    "Giant":          "RiseOfTheGiant",
    "Astrolab":       "RiseOfTheGiant",
    "Observatory":    "RiseOfTheGiant",
    "Greenhouse":     "TheBadSeed",
    "Swamp":          "TheBadSeed",
    "SwampHeart":     "TheBadSeed",
    "Tumulus":        "FatalFalls",
    "Cliff":          "FatalFalls",
    "GardenerStage":  "FatalFalls",
    "Shipwreck":      "TheQueenAndTheSea",
    "Lighthouse":     "TheQueenAndTheSea",
    "QueenArena":     "TheQueenAndTheSea",
    "PurpleGarden":   "Purple",
    "DookuCastle":    "Purple",
    "DookuCastleHard":"Purple",
    "DeathArena":     "Purple",
    "DookuArena":     "Purple",
}


# ─────────────────────────────────────────────────────────────────────────────
# Main region creation function — called from __init__.py
# ─────────────────────────────────────────────────────────────────────────────
def create_regions(world: "DeadCellsWorld") -> None:
    """
    Create all regions, populate them with their locations,
    and wire up entrances with access rules.
    """
    world.created_locations = set()
    enabled_dlcs: set = world.enabled_dlcs  # set of DLC strings, e.g. {"TheBadSeed"}
    bc_level: int     = world.options.boss_cells.value
    player: int       = world.player
    multiworld        = world.multiworld

    # ── 1. Create region objects ──────────────────────────────────────────────
    # Biomes only accessible at specific BC levels
    BC_GATED_REGIONS = {
        "Astrolab":    5,
        "Observatory": 5,
    }

    regions = {}
    for name in ALL_REGIONS:
        dlc = REGION_DLC.get(name, "")
        # Skip DLC regions whose DLC is not enabled
        if dlc and dlc not in enabled_dlcs:
            continue
        # Skip BC-gated regions if current BC level is too low
        min_bc_required = BC_GATED_REGIONS.get(name, 0)
        if bc_level < min_bc_required:
            continue
        region = Region(name, player, multiworld)
        regions[name] = region
        multiworld.regions.append(region)

    # ── 2. Populate regions with their locations ──────────────────────────────
    for loc_name, loc_data in LOCATION_TABLE.items():
        region_name = loc_data["region"]
        if region_name not in regions:
            continue

        loc_dlc = loc_data["dlc"]
        if loc_dlc and loc_dlc not in enabled_dlcs:
            continue

        loc_id = location_id(loc_name)
        sources = loc_data.get("sources", [])

        if hasattr(world, "grouped_location_sources") and loc_id in world.grouped_location_sources:
            sources = world.grouped_location_sources[loc_id]
            min_bc = min(s["min_bc"] for s in sources)
            max_bc = max(s["max_bc"] for s in sources)
        else:
            min_bc = loc_data.get("min_bc", 0)
            max_bc = world.options.boss_cells.value

        if (loc_data["type"] in ("skin", "head")) and world.options.include_cosmetics.value == 0:
            continue

        if min_bc > bc_level:
            continue

        if region_name == "Checks":
            sources = loc_data.get("sources", [])

            valid_sources = [
                s for s in sources
                if (s["dlc"] == "" or s["dlc"] in enabled_dlcs)
                and s["biome"] in regions
            ]

            if not valid_sources:
                valid_sources = [{"biome": "PrisonStart", "dlc": "", "min_bc": 0, "max_bc": 5}]

            loc = DeadCellsLocation(
                player,
                loc_name,
                location_id(loc_name),
                regions["Checks"],
            )

            world.created_locations.add(loc_name)
            regions["Checks"].locations.append(loc)

            extra_rule = build_rule(loc_data["requires"], world) if loc_data.get("requires") else None

            # ── NON-"Checks" LOCATIONS (source-based, like your data) ────────
            sources = loc_data.get("sources", [])

# Filter valid sources (same logic style as Checks)
        valid_sources = [
            s for s in sources
            if (s["dlc"] == "" or s["dlc"] in enabled_dlcs)
        and s["biome"] in regions
]

# Fallback to prevent dead locations
        if not valid_sources:
            valid_sources = [{"biome": region_name, "dlc": "", "min_bc": 0, "max_bc": 5}]

        loc = DeadCellsLocation(
            player,
            loc_name,
            loc_id,
            regions[region_name],
        )

        world.created_locations.add(loc_name)
        regions[region_name].locations.append(loc)

        extra_rule = build_rule(loc_data["requires"], world) if loc_data.get("requires") else None

        def make_rule(source_data, extra_rule):
            def rule(state, source_data=source_data):
                bc = get_bc_level(state, player)

                source_ok = any(
                    (s["dlc"] == "" or s["dlc"] in enabled_dlcs)
                    and state.can_reach(s["biome"], "Region", player)
                    and s["min_bc"] <= bc <= s["max_bc"]
                    for s in source_data
                    )

                if extra_rule:
                 return source_ok and extra_rule(state)
                return source_ok

            return rule

        set_rule(loc, make_rule(valid_sources, extra_rule))
        

    # ── 3. Wire entrances ─────────────────────────────────────────────────────
    for from_region, exits in TRANSITIONS.items():
        if from_region not in regions:
            continue

        for exit_data in exits:
            to_region = exit_data["to"]
            requirement = exit_data["require"]

            if to_region not in regions:
                continue

            entrance = regions[from_region].connect(regions[to_region])
            if requirement is not None:
                set_rule(
                    entrance,
                    build_transition_rule(requirement, world, player)
                )

    # ── 4. Wire biome -> Checks entrances ────────────────────────────────────
    # Each biome has an unconditional entrance to the virtual Checks region.
    # Per-check OR access rules are applied in rules.py set_rules().
    checks_region = regions.get("Checks")
    if checks_region:
        for biome_name in list(regions.keys()):
            if biome_name in ("Menu", "End", "Checks"):
                continue
            entrance = Entrance(player, f"{biome_name} -> Checks", regions[biome_name])
            entrance.access_rule = lambda state, b=biome_name: state.can_reach(b, "Region", player)
            regions[biome_name].exits.append(entrance)
            entrance.connect(checks_region)

    # ── 5. Set the start region ───────────────────────────────────────────────
    multiworld.get_region("Menu", player).exits[0].connect(regions["PrisonStart"])
