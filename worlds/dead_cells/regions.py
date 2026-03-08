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

def _has_bsc(world: "DeadCellsWorld", level: int) -> bool:
    return world.options.boss_cells.value >= level


def build_rule(requires, world: "DeadCellsWorld"):
    """
    Build an Archipelago access rule lambda from a requires value.
    requires can be:
      - None          -> always accessible
      - str           -> single condition
      - list[str]     -> AND of all conditions
    """
    if requires is None:
        return lambda state: True

    if isinstance(requires, str):
        requires = [requires]

    player = world.player
    runes = {
        "LadderKey", "TeleportKey", "ScoringKey", "CustomKey",
        "BreakableGroundKey", "WallJumpKey", "HomKey", "ExploKey",
        "BossRune1", "BossRune2", "BossRune3", "BossRune4", "BossRune5",
    }
    boss_kills = set(BOSS_LOCATION.keys())
    biome_visits = {"Swamp", "Cliff"}
    bsc_levels = set(BSC_LEVEL.keys())
    # AP items that behave like inventory items
    ap_items = {"Cultist", "LighthouseKey"}

    # Pre-resolve BSC conditions (static, based on option)
    bsc_conditions = []
    for req in requires:
        if req in bsc_levels:
            bsc_conditions.append(BSC_LEVEL[req])

    # If any BSC condition fails at world gen time, rule is always False
    for level in bsc_conditions:
        if not _has_bsc(world, level):
            return lambda state: False

    # Build dynamic conditions (checked at runtime)
    dynamic = []
    for req in requires:
        if req in runes or req in ap_items:
            dynamic.append(("item", req))
        elif req in boss_kills:
            dynamic.append(("boss", req))
        elif req in biome_visits:
            dynamic.append(("biome", req))
        elif req in bsc_levels:
            pass  # Already handled statically above

    if not dynamic:
        return lambda state: True

    def rule(state):
        for kind, value in dynamic:
            if kind == "item":
                if not _has_item(state, player, value):
                    return False
            elif kind == "boss":
                if not _has_boss_kill(state, player, value):
                    return False
            elif kind == "biome":
                if not _has_biome_enter(state, player, value):
                    return False
        return True

    return rule


# ─────────────────────────────────────────────────────────────────────────────
# Transition table
# Encoded directly from transition.json
# ─────────────────────────────────────────────────────────────────────────────
TRANSITIONS = {
    "Menu": [
        {"to": "PrisonStart", "require": None},
        {"to": "Bank",        "require": None},
        {"to": "Challenge",   "require": None},
    ],
    "PrisonStart": [
        {"to": "PrisonCourtyard", "require": None},
        {"to": "SewerShort",      "require": "LadderKey"},
        {"to": "Greenhouse",      "require": "TeleportKey"},
        {"to": "PurpleGarden",    "require": None},
    ],
    "PrisonCourtyard": [
        {"to": "Ossuary",      "require": "TeleportKey"},
        {"to": "PrisonRoof",   "require": None},
        {"to": "PrisonDepths", "require": "WallJumpKey"},
        {"to": "Swamp",        "require": None},
    ],
    "SewerShort": [
        {"to": "PrisonCorrupt", "require": "WallJumpKey"},
        {"to": "PrisonRoof",    "require": None},
        {"to": "SewerDepths",   "require": "BreakableGroundKey"},
        {"to": "DookuCastle",   "require": "DookuBeast"},
    ],
    "PrisonDepths": [
        {"to": "Ossuary",    "require": None},
        {"to": "SewerDepths","require": "bsc1"},
        {"to": "Swamp",      "require": None},
    ],
    "PrisonCorrupt": [
        {"to": "SewerDepths", "require": None},
        {"to": "PrisonRoof",  "require": "bsc1"},
        {"to": "DookuCastle", "require": "DookuBeast"},
    ],
    "PrisonRoof": [
        {"to": "Bridge",     "require": None},
        {"to": "BeholderPit","require": "bsc3"},
    ],
    "Ossuary": [
        {"to": "Bridge",    "require": None},
        {"to": "DeathArena","require": "DookuBeast"},
    ],
    "SewerDepths": [
        {"to": "BeholderPit", "require": None},
    ],
    "Bridge": [
        {"to": "Tumulus",      "require": None},
        {"to": "StiltVillage", "require": None},
        {"to": "AncientTemple","require": "WallJumpKey"},
    ],
    "BeholderPit": [
        {"to": "AncientTemple","require": None},
        {"to": "Cemetery",     "require": "WallJumpKey"},
    ],
    "StiltVillage": [
        {"to": "Cliff",      "require": None},
        {"to": "ClockTower", "require": None},
        {"to": "Crypt",      "require": "TeleportKey"},
    ],
    "AncientTemple": [
        {"to": "Cavern",     "require": ["Giant", "bsc2"]},
        {"to": "ClockTower", "require": None},
        {"to": "Crypt",      "require": "TeleportKey"},
    ],
    "Cemetery": [
        {"to": "Cliff",   "require": None},
        {"to": "Cavern",  "require": "KingsHand"},
        {"to": "Crypt",   "require": "TeleportKey"},
    ],
    "ClockTower": [
        {"to": "TopClockTower", "require": None},
    ],
    "Crypt": [
        {"to": "TopClockTower", "require": None},
        {"to": "Giant",         "require": ["Giant", "bsc2"]},
    ],
    "TopClockTower": [
        {"to": "Shipwreck",      "require": "LighthouseKey"},
        {"to": "Distillery",     "require": None},
        {"to": "Castle",         "require": None},
        {"to": "DookuCastleHard","require": "Death"},
    ],
    "Cavern": [
        {"to": "GardenerStage", "require": "GardenerBoss"},
        {"to": "Giant",         "require": None},
    ],
    "Giant": [
        {"to": "Shipwreck",      "require": "LighthouseKey"},
        {"to": "Distillery",     "require": None},
        {"to": "Castle",         "require": None},
        {"to": "DookuCastleHard","require": "DookuBeast"},
        {"to": "Throne",         "require": None},
    ],
    "Castle": [
        {"to": "DookuArena", "require": "DookuBeast"},
        {"to": "Throne",     "require": None},
    ],
    "Distillery": [
        {"to": "Lighthouse", "require": ["AmazonSurvival", "AmazonTactic", "AmazonBrutal"]},
        {"to": "Throne",     "require": None},
    ],
    "Throne": [
        {"to": "Astrolab", "require": "bsc5"},
        {"to": "End",      "require": None},
    ],
    "Astrolab": [
        {"to": "Observatory", "require": None},
    ],
    "Observatory": [
        {"to": "End", "require": None},
    ],
    "Swamp": [
        {"to": "SwampHeart", "require": None},
    ],
    "SwampHeart": [
        {"to": "StiltVillage", "require": None},
        {"to": "Cemetery",     "require": "WallJumpKey"},
        {"to": "Tumulus",      "require": None},
    ],
    "Tumulus": [
        {"to": "Cliff",      "require": "Cultist"},
        {"to": "ClockTower", "require": None},
        {"to": "Crypt",      "require": "TeleportKey"},
    ],
    "Cliff": [
        {"to": "GardenerStage", "require": None},
    ],
    "GardenerStage": [
        {"to": "Shipwreck",      "require": "LighthouseKey"},
        {"to": "Distillery",     "require": None},
        {"to": "Castle",         "require": None},
        {"to": "DookuCastleHard","require": "DookuBeast"},
    ],
    "Shipwreck": [
        {"to": "Lighthouse", "require": None},
    ],
    "Lighthouse": [
        {"to": "QueenArena", "require": None},
    ],
    "QueenArena": [
        {"to": "End", "require": None},
    ],
    "PurpleGarden": [
        {"to": "PrisonCorrupt","require": ["WallJumpKey", "DookuBeast"]},
        {"to": "DookuCastle",  "require": None},
        {"to": "Ossuary",      "require": ["TeleportKey", "DookuBeast"]},
    ],
    "DookuCastle": [
        {"to": "Bridge",    "require": "DookuBeast"},
        {"to": "DeathArena","require": None},
    ],
    "DookuCastleHard": [
        {"to": "DookuArena", "require": None},
    ],
    "DeathArena": [
        {"to": "Cemetery",     "require": "WallJumpKey"},
        {"to": "StiltVillage", "require": None},
        {"to": "AncientTemple","require": "WallJumpKey"},
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
            continue  # DLC region disabled or virtual region not yet created

        # Skip locations whose DLC is not enabled
        loc_dlc = loc_data["dlc"]
        if loc_dlc and loc_dlc not in enabled_dlcs:
            continue
        
        if loc_data.get("min_bc", 0) > bc_level:
            continue

        # For grouped checks in "Checks" region: skip if no source accessible
        if region_name == "Checks":
            sources = loc_data.get("sources", [])
            accessible = any(
                (s["dlc"] == "" or s["dlc"] in enabled_dlcs)
                and s["min_bc"] <= bc_level <= s["max_bc"]
                for s in sources
            )
            if not accessible:
                continue

        loc = DeadCellsLocation(
            player,
            loc_name,
            location_id(loc_name),
            regions[region_name],
        )
        regions[region_name].locations.append(loc)

    # ── 3. Wire entrances ─────────────────────────────────────────────────────
    for from_name, transitions in TRANSITIONS.items():
        if from_name not in regions:
            continue

        from_region = regions[from_name]
        for t in transitions:
            to_name = t["to"]
            if to_name not in regions:
                continue  # target region disabled or not yet reached

            entrance = Entrance(player, f"{from_name} -> {to_name}", from_region)
            entrance.access_rule = build_rule(t.get("require"), world)
            from_region.exits.append(entrance)
            entrance.connect(regions[to_name])

    # ── 4. Wire biome -> Checks entrances ────────────────────────────────────
    # Each biome has an unconditional entrance to the virtual Checks region.
    # Per-check OR access rules are applied in rules.py set_rules().
    checks_region = regions.get("Checks")
    if checks_region:
        for biome_name in list(regions.keys()):
            if biome_name in ("Menu", "End", "Checks"):
                continue
            entrance = Entrance(player, f"{biome_name} -> Checks", regions[biome_name])
            entrance.access_rule = lambda state: True
            regions[biome_name].exits.append(entrance)
            entrance.connect(checks_region)

    # ── 5. Set the start region ───────────────────────────────────────────────
    multiworld.get_region("Menu", player).exits[0].connect(regions["PrisonStart"])
