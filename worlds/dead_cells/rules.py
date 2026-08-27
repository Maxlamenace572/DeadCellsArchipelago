"""
Dead Cells - Archipelago World
rules.py

Location-level access rules that go beyond region entrance conditions.
These are applied after create_regions() in __init__.py via set_rules().

Rule categories:
  - BSC level requirements (based on ProgBossRune count)
  - Item requirements (runes, AP items in inventory)
  - Boss kill requirements (specific location checks completed)
  - Skin count requirements (number of Skin-category items received)
  - Biome exit requirements (one of several biome_exit checks reached)
  - Combined conditions (AND / OR)

Adding new rules:
  Append entries to LOCATION_RULES below. Each entry is a dict:
    {
        "location": "ExactLocationName",   # from LOCATION_TABLE
        "requires": { ... }                # see RuleType constants below
    }
  Then re-run set_rules() — no other file needs changing.
"""

from typing import TYPE_CHECKING, List
from worlds.dead_cells.items import ITEM_TABLE
from worlds.dead_cells.locations import LOCATION_TABLE
from worlds.generic.Rules import add_rule

if TYPE_CHECKING:
    from . import DeadCellsWorld


# ─────────────────────────────────────────────────────────────────────────────
# Skin item names (used for count-based rules)
# ─────────────────────────────────────────────────────────────────────────────
SKIN_ITEMS = [

    # base outfits
    "Golden Outfit", "Legendary Warrior's Outfit", "Ninja Outfit", "Ghost Outfit",
    "Donatello Outfit", "Santa Outfit", "Fisherman's Outfit", "Skeleton Outfit",
    "Carduus Outfit", "Aphrodite Outfit", "Shaman Outfit", "Cloud Outfit",
    "The Magician's Outfit", "A Thousand and One Nights Outfit", "Dictator Outfit", "Warrior Outfit",
    "Mage Outfit", "Neon Outfit", "Bobby Outfit", "Demon Outfit",
    "Robin Hood Outfit", "Desert Dweller Outfit", "Galaxy Outfit", "Baguette Outfit",
    "Festive Outfit", "Gardener's Outfit", "Mushroom Boi's Outfit", "Mushroom Outfit",
    "Banished's Outfit", "Blowgunner's Outfit", "Tick Trainer's Outfit", "The Royal Gardener's Outfit",
    "Retro Outfit", "HEV Outfit", "Lizard Outfit", "Apostate Outfit",
    "Almost-Yourself Outfit", "Kamikaze Outfit", "Arbalester's Outfit", "Blade Master's Outfit",

    # king
    "King Outfit", "White King Outfit",

    # concierge
    "Classic Concierge Outfit",
    "Piccolo Concierge Outfit",
    "Misunderstood Concierge Outfit",
    "Ascended Concierge Outfit",
    "Ultimate Concierge Outfit",

    # conjunctivius
    "Classic Conjunctivius Outfit",
    "Starved Conjunctivius Outfit",
    "Enraged Conjunctivius Outfit",
    "Revolted Conjunctivius Outfit",
    "Legendary Conjuctivius Outfit",

    # time keeper
    "Classic Temporal Outfit",
    "Desert Temporal Outfit",
    "Volcanic Temporal Outfit",
    "Hunter's Temporal Outfit",
    "Collector's Temporal Outfit",

    # giant
    "Classic Giant Outfit",
    "Disappointed Giant's Outfit",
    "Cursed Giant's Outfit",
    "Misunderstood Giant's Outfit",
    "Frustrated Giant's Outfit",

    # hand of the king
    "The Hand of the King Outfit",
    "Loyal Hand of the King Outfit",
    "Incorruptible Hand of the King Outfit",
    "Faithful Hand of the King Outfit",
    "Devoted Hand of the King Outfit",

    "Rocky Outfit",
    "Fallen Collector's Outfit",

    # mama tick
    "Giant Tick Outfit",
    "Annoyed Tick Outfit",
    "Irritated Tick Outfit",
    "Mad Tick Outfit",
    "Furious Mama Tick Outfit",
    "Sacrificial Tick Outfit",

    # scarecrow
    "Classic Scarecrow Outfit",
    "Green Thumb Scarecrow Outfit",
    "Wicked Scarecrow of the West Outfit",
    "Cutecrow Outfit",
    "Gothic Scarecrow Outfit",
    "Cultist Outfit",

    # flawless boss outfits
    "Flawless Concierge Outfit",
    "Flawless Conjunctivius Outfit",
    "Flawless Temporal Outfit",
    "Flawless Giant Outfit",
    "Flawless Hand of the King Outfit",
    "Flawless Tick Outfit",
    "Flawless Scarecrow Outfit",

    # misc
    "Winter Outfit",
    "Reverse Burglar's Outfit",

    # crossover outfits
    "Vessel's Outfit",
    "Pentinent's Outfit",
    "Luchador's Outfit",
    "Little Bone's Outfit",
    "The Magician's Outfit",
    "Explorer's Outfit",
    "Knight's Outfit",

    # pets / misc
    "Armored Shrimp Carcass Outfit",
    "Mutineer Outfit",

    # servants
    "Servant Outfit",
    "Toxic Servant Outfit",
    "Silver Servant Outfit",
    "Aurora Servant Outfit",
    "King's Servant Outfit",
    "Flawless Servant Outfit",

    # queen
    "Queen Outfit",
    "White Gold Queen Outfit",
    "Cherry Blossom Queen Outfit",
    "Frozen Queen Outfit",
    "Spicy Queen Outfit",
    "Flawless Queen Outfit",

    "Blue Erinaceus Outfit",

    # npcs
    "Gentleman's Outfit",
    "Robber Outfit",
    "Bobby Outfit",

    # indie crossovers
    "Shovel Knight Outfit",
    "Modernized Bomber Outfit",
    "ZERO Outfit",
    "Commando Outfit",
    "Familiar Outfit",
    "Ironclad Outfit",

    # boss rush
    "Boss Knight Outfit",
    "Barbarian Boss Knight Outfit",
    "Triumphant Boss Knight Outfit",
    "Luminous Boss Knight Outfit",

    "Triumph Outfit",
    "Bisonnica Triumph Outfit",
    "Mentoral Triumph Outfit",
    "Radiant Triumph Outfit",

    # castlevania
    "Simon Outfit",
    "Alucard Outfit",
    "Richter Outfit",
    "Sypha Outfit",
    "Trevor Outfit",
    "Maria Renard Outfit",
    "Hector Outfit",
    "Haunted Armor Outfit",

    # death
    "Death Outfit",
    "Sanguine Death Outfit",
    "Red Death Outfit",
    "Edgy Death Outfit",
    "Spectral Death Outfit",
    "Flawless Death Outfit",

    # dracula
    "Dracula Outfit",
    "Mathias Cronqvist Outfit",
    "Doctor Dracula Outfit",
    "Pompous Dracula Outfit",
    "Vigilante Dracula Outfit",
    "Flawless Dracula Outfit",
]
BOSS_RUSH_TIER_1 = [
    "Behemoth",
    "Beholder",
    "MamaTick",
    "Death",
]

BOSS_RUSH_TIER_2 = [
    "TimeKeeper",
    "Giant",
    "GardenerBoss",
    "DookuBeast",
]

BOSS_RUSH_TIER_3 = [
    "KingsHand",
    "Queen",
    "AmazonSurvival",
    "AmazonTactic",
    "AmazonBrutal",
    "Collector",
]
HEAD_ITEMS = [

    # boss flames
    "Bobby Head",
    "Concierge Flame",
    "Giant Flame",
    "Queen Flame",
    "Hand of the King Flame",

    # boss themed heads
    "Conjunctivius Tentacles",
    "Mama Tick Eye",
    "Time Keeper Mask",
    "Scarecrow Hat",
    "Servant Mask",
    "Collector Hood",

    # black hole variants
    "Black Hole",
    "White Hole",
##    "Violet Hole", already unlocked
#    "Red Hole", #to avoid recursion error on head count rule, thoses are removed too
    "Green Hole",
    "Blue Hole",

    # vortex heads
##    "Vortex",
    "Sanguine Vortex",
    "Abyssal Vortex",
#    "Dark Vortex",

    # misc
    "Guillain Head",
#    "Fisherman Hood",
    "Leghugger Head",
    "Flawless Torch",
    "Cell Head",
    "Evil Minion Head",

    # blob heads
    "Toxic Blob",
    "Magma Blob",
    "Shadow Blob",
    "Sweet Blob",

    # glitch heads
    "Glitch Head",
#    "Spatial Anomaly",
    "Menacing Anomaly",

    # mushroom
    "Mushroom Boi Cap",

    # torch heads
    "Dark Blowtorch",
##    "Blowtorch",
    "Golden Blowtorch",
    "Bright Red Blowtorch",

    # misc uniques
    "Biter Head",
    "Horde Zero Hood",
    "Boss Cell Head",
]

# ─────────────────────────────────────────────────────────────────────────────
# Location rules table
#
# Each entry: ("location_name", rule_lambda_factory)
# The factory receives (world) and returns a state -> bool lambda.
#
# Helpers at the bottom of this file build the lambdas cleanly.
# ─────────────────────────────────────────────────────────────────────────────

from worlds.generic.Rules import add_rule


def _has(item: str):
    """Rule: player has item in inventory."""
    return lambda world: (
        lambda state: state.has(item, world.player)
    )


def _has_all(*items: str):
    """Rule: player has ALL listed items."""
    return lambda world: (
        lambda state: state.has_all(items, world.player)
    )


def _has_any(*items: str):
    """Rule: player has ANY of the listed items."""
    return lambda world: (
        lambda state: any(state.has(i, world.player) for i in items)
    )


def _has_all_any(all_items, any_of=()):
    """
    Rule: player has ALL items in all_items AND at least one item in any_of.
    all_items may contain strings or nested lists/tuples.
    """
    flat_items = tuple(
        item
        for sub in all_items
        for item in (sub if isinstance(sub, (list, tuple)) else (sub,))
    )

    return lambda world: (
        lambda state:
            state.has_all(flat_items, world.player)
            and (not any_of or any(state.has(i, world.player) for i in any_of))
    )

def _has_any_of(*items: str):
    return lambda world: (
        lambda state: any(state.has(item, world.player) for item in items)
    )

def get_bc_level(state, player: int) -> int:
    """Count acquired Boss Stem Cells."""
    return state.count("Progressive Stem Cell", player)


def _bsc(level: int):
    """Rule: player has at least N Boss Stem Cells."""
    return lambda world: (
        lambda state: get_bc_level(state, world.player) >= level
    )


def _has_and_bsc(item: str, level: int):
    """Rule: player has item AND at least N Boss Stem Cells."""
    return lambda world: (
        lambda state:
            state.has(item, world.player)
            and get_bc_level(state, world.player) >= level
    )


def _reach_skin_count(count: int):
    """Rule: player has received at least `count` skin items."""
    return lambda world:  lambda state: sum(
            1 for skin in SKIN_ITEMS if _can_reach_location_if_exists(state, world, skin)
        ) >= count


def _boss_killed(location: str):
    """Rule: specific boss location has been checked/reached."""
    return lambda world: (
        lambda state: state.can_reach_location(location, world.player)
    )


def _any_biome_exit(*biomes: str):
    """Rule: player has completed the biome_exit check of at least one biome."""
    return lambda world: (
        lambda state: any(
            state.can_reach_location(f"{b}_Exit", world.player)
            for b in biomes
        )
    )


def _has_and_boss(item: str, boss_loc: str):
    """Rule: player has item AND boss kill completed."""
    return lambda world: (
        lambda state: (
            state.has(item, world.player)
            and state.can_reach_location(boss_loc, world.player)
        )
    )


def _count_cleared_bosses(state, player: int, boss_names) -> int:
    from .regions import BOSS_LOCATION

    count = 0
    for boss in boss_names:
        loc_name = BOSS_LOCATION.get(boss)
        if not loc_name:
            continue

        try:
            if state.can_reach_location(loc_name, player):
                count += 1
        except KeyError:
            # Boss location may not exist in this seed/world
            continue

    return count


def _boss_rush_trials_1_2():
    """
    Trials 1 and 2:
    at least 1 cleared Tier 1 boss,
    at least 1 cleared Tier 2 boss,
    at least 1 cleared Tier 3 boss,
    and the Boss Rush Unlock item.
    """
    return lambda world: (
        lambda state: (
            _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_1) >= 1
            and _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_2) >= 1
            and _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_3) >= 1
            and _has("Boss Rush Unlock")
        )
    )


def _boss_rush_trials_3_4():
    """
    Trials 3 and 4:
    at least 2 cleared Tier 1 bosses,
    at least 2 cleared Tier 2 bosses,
    at least 1 cleared Tier 3 boss,
    and the Boss Rush Unlock.
    """
    return lambda world: (
        lambda state: (
            _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_1) >= 2
            and _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_2) >= 2
            and _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_3) >= 1
            and _has("Boss Rush Unlock")
        )
    )

def _reach_head_count(count: int):
    """
    Rule: player has received at least `count` head cosmetics.
    """
    return lambda world:  lambda state: sum(
            1 for head in HEAD_ITEMS if _can_reach_location_if_exists(state, world, head)
        ) >= count
    
def _can_reach_depth(depth: int):
    """Rule: player can enter any biome of this depth."""
    biomesDepth = [
        ["Prisoners' Quarters Enter"],
        ["Promenade of the Condemned Enter", "Toxic Sewers Enter", "Prison Depths Enter", "Corrupted Prison Enter",
            "Dilapidated Arboretum Enter", "Castle Outskirts Enter"],
        ["Ramparts Enter", "Ossuary Enter", "Ancient Sewers Enter", "Morass of the Banished Enter", "Dracula's Castle Enter"],
        ["Black Bridge Enter", "Insufferable Crypt Enter", "Nest Enter", "Defiled Necropolis Enter"],
        ["Stilt Village Enter", "Slumbering Sanctuary Enter", "Graveyard Enter", "Fractured Shrines Enter"],
        ["Clock Tower Enter", "Forgotten Sepulcher Enter", "Cavern Enter", "Undying Shores Enter"],
        ["Clock Room Enter", "Guardian's Haven Enter", "Mausoleum Enter"],
        ["High Peak Castle Enter", "Derelict Distillery Enter", "Infested Shipwreck Enter", "2nd Dracula's Castle Enter"],
        ["Throne Room Enter", "Lighthouse Enter", "Master's Keep Enter"],
        ["Astrolab Enter"],
        ["Observatory Enter", "Crown Enter"]
    ]
    return lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in biomesDepth[depth]
        )

def _can_reach_location_if_exists(state, world, loc_name: str) -> bool:
    try:
        world.multiworld.get_location(loc_name, world.player)
    except KeyError:
        return False
    return state.can_reach_location(loc_name, world.player)

def _can_reach_nb_item_locations(nb: int):
    return lambda world:  lambda state: sum(
            1 for loc_name, loc_data in LOCATION_TABLE.items()
                if loc_data["type"] in ("skin", "item_no_blueprint", "blueprint_floor", "blueprint_enemy") and
                    _can_reach_location_if_exists(state, world, loc_name)
        ) >= nb

def set_rules(world):
    """
    Apply source-based access rules from LOCATION_TABLE.
    A location is reachable if ANY source is valid:
    - source biome is reachable
    - player's BSC count is within source min/max
    - source DLC is enabled (if specified)
    """
    player = world.player
    enabled_dlcs = getattr(world, "enabled_dlcs", set())

    for loc_name, loc_data in LOCATION_TABLE.items():
        try:
            location = world.multiworld.get_location(loc_name, player)
        except KeyError:
            # Location does not exist in this world (DLC off, filtered out, etc.)
            continue

        sources = loc_data.get("sources", [])

        # If no sources are defined, do not attach a source rule here.
        # Other explicit rules can still apply elsewhere.
        if not sources:
            continue

        def rule(state, sources=sources, enabled_dlcs=enabled_dlcs):
            bc = get_bc_level(state, player)

            for s in sources:
                biome = s.get("biome")
                min_bc = s.get("min_bc", 0)
                max_bc = s.get("max_bc", 5)
                dlc = s.get("dlc", "")

                # DLC gate
                if dlc and dlc not in enabled_dlcs:
                    continue

                # Region/biome reachability + BC gate
                if biome and state.can_reach(biome, "Region", player) and min_bc <= bc <= max_bc:
                    return True

            return False

        add_rule(location, rule)
# ─────────────────────────────────────────────────────────────────────────────
# The main rules table
# Format: (location_name, rule_factory)
# ─────────────────────────────────────────────────────────────────────────────
LOCATION_RULES = [

    # ── Gameplay items ────────────────────────────────────────────────────────
    ("Disengagement", _has("Homunculus Rune")),
    ("Gold Reserves V",  _has("Homunculus Rune")),
    ("Ripper", _has("Spider Rune")),

    ("Swift Sword",    _has("Challenger's Rune")),
    ("Lacerating Aura",    _has("Challenger's Rune")),
    ("Meat Skewer",     _has("Challenger's Rune")),


    # ── Crowned Key logic ─────────────────────────────────────────────────
    ("Crowned Key", lambda world: (
        lambda state: state.can_reach("SewerShort", "Region", world.player)
    )),

    
    ("Abyssal Trident", _has("Ram Rune")),



    # Cursed Biome drops
    (
        "Anathema", 
        lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in [
                "Toxic Sewers Enter",
                "Castle's Outskirts Enter",
                "Dilapidated Arboretum Enter",
            ]
        )
    ),
    (
        "Cursed Flask", 
        lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in [
                "Toxic Sewers Enter",
                "Castle's Outskirts Enter",
                "Dilapidated Arboretum Enter",
            ]
        )
    ),
    (
        "Demon Strength", 
        lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in [
                "Toxic Sewers Enter",
                "Castle's Outskirts Enter",
                "Dilapidated Arboretum Enter",
            ]
        )
    ),
    (
        "Misericorde", 
        lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in [
                "Toxic Sewers Enter",
                "Castle's Outskirts Enter",
                "Dilapidated Arboretum Enter",
            ]
        )
    ),
    (
        "Damned Vigor", 
        lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in [
                "Toxic Sewers Enter",
                "Castle's Outskirts Enter",
                "Dilapidated Arboretum Enter",
            ]
        )
    ),
    (
        "Indulgence", 
        lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in [
                "Toxic Sewers Enter",
                "Castle's Outskirts Enter",
                "Dilapidated Arboretum Enter",
            ]
        )
    ),

    (
        "Acceptance",
        _has_all(
            "Vine Rune", 
            "Ram Rune", 
            "Insufferable Crypt Unlock", 
            "Graveyard Unlock", 
            "Spider Rune", 
            "Teleportation Rune", 
            "Forgotten Sepulcher Unlock",
        )
    ),


    # ── PrisonCourtyard mid-biome gate (Vine Rune) ────────────────────────────
    ("Phaser", _has("Vine Rune")),
    ("Spartan Sandals", _has("Vine Rune")),
    ("Corrupted Power", _has("Vine Rune")),
    ("Explosive Decoy", _has("Vine Rune")),
    ("Powerful Grenade", _has("Vine Rune")),
    ("Cleaver", _has("Vine Rune")),
    ("Knife Dance", _has("Vine Rune")),
    ("Execution", _has("Vine Rune")),
    ("Repeater Crossbow", _has("Vine Rune")),
    ("Hayabusa Boots", _has("Vine Rune")),
    ("Oiled Sword", _has("Vine Rune")),
    ("Berserker", _has("Vine Rune")),
    ("Aphrodite Outfit", _has("Vine Rune")),
    ("Ninja Outfit", _has("Vine Rune")),
    ("Kamikaze Outfit", _has("Vine Rune")),
    ("Neon Outfit", _has("Vine Rune")),
    ("Warrior Outfit", _has("Vine Rune")),
    ("Wave of Denial", _has("Vine Rune")),
    ("Marksman's Bow", _has("Vine Rune")),

    (
        "Explosive Crossbow",
        _has_all_any(
            ["Vine Rune", "Ram Rune"],
            any_of=["Spider Rune", "Homunculus Rune"]
        )
    ),

    ("Promenade of the Condemned Exit", _has("Vine Rune")),


    # ── Dilapidated Arboretum Entrance ───────────────────────────────────────
    ("The Royal Gardener's Outfit", _has("Teleportation Rune")),

    # Parting Gift Graveyard secret
    ("Parting Gift", _has("Ram Rune")),

    # Parry Shield Stilt Village secret
    ("Parry Shield", _has_all("Spider Rune", "Ram Rune")),

    # Extended Healing Ossuary secret
    ("Extended Healing", _has("Teleportation Rune")),

    # War Javelin Cavern secret
    ("War Javelin", _has("Spider Rune") and _has("Homunculus Rune")),

    # Sanguine Vortex head
    (
        "Sanguine Vortex", 
        lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in [
                "Toxic Sewers Enter",
                "Dracula's Castle Enter",
                "Dilapidated Arboretum Enter",
            ]
        )
    ),

    (
        "Magma Blob", 
        lambda world: lambda state: any(
            _can_reach_location_if_exists(state, world, loc)
            for loc in [
                "Cavern Key",
                "Cavern Enter",
                "Graveyard Enter"
            ]
        )
    ),

    # ── Boss Rush Items ──────────────────────────────────────────────────────
    ("Boss Knight Outfit", _boss_rush_trials_1_2()),
    ("Barbarian Boss Knight Outfit", _boss_rush_trials_3_4() and _bsc(3)),
    ("Triumphant Boss Knight Outfit", _boss_rush_trials_1_2() and _bsc(3)),
    ("Luminous Boss Knight Outfit", _boss_rush_trials_1_2() and _bsc(5)),
    
    ("Triumph Outfit", _boss_rush_trials_3_4()),
    ("Bisonnica Triumph Outfit", _boss_rush_trials_3_4() and _bsc(3)),
    ("Mentoral Triumph Outfit", _boss_rush_trials_3_4() and _bsc(5)),
    ("Radiant Triumph Outfit", _boss_rush_trials_3_4() and _bsc(5)),
    
    ("Peril Glyphs", _boss_rush_trials_1_2()),
    ("Taunt", _boss_rush_trials_1_2()), 
    ("Wish", _boss_rush_trials_3_4()),
    
    
    # ── Bank Items with depth ────────────────────────────────────────────────
    ("Spite Sword", _can_reach_depth(2)),
    ("Frostbite", _can_reach_depth(2)),
    ("Cluster Grenade", _can_reach_depth(2)),
    ("Heavy Turret", _can_reach_depth(2)),
    ("Demon Outfit", _can_reach_depth(2)),
    ("No Mercy", _can_reach_depth(2)),
    ("Barbed Tips", _can_reach_depth(2)),
    ("Hattori's Katana", _can_reach_depth(2)),
    ("Blade Master's Outfit", _can_reach_depth(2)),
    ("Spiked Boots", _can_reach_depth(2)),
    ("Barnacle", _can_reach_depth(2)),
    ("Armadillopack", _can_reach_depth(2)),
    ("Seismic Strike", _can_reach_depth(2)),
    ("A Thousand and One Nights Outfit", _can_reach_depth(2)),
    ("Lightning Bolt", _can_reach_depth(4)),
    ("Vampirism", _can_reach_depth(4)),
    ("Wrenching Whip", _can_reach_depth(4)),
    ("Heart of Ice", _can_reach_depth(4)),
    ("Scavenged Bombard", _can_reach_depth(4)),
    ("Ranger's Gear", _can_reach_depth(4)),
    ("Hokuto's Bow", _can_reach_depth(4)),
    ("Dictator Outfit", _can_reach_depth(4)),
    ("Grappling Hook", _can_reach_depth(4)),
    ("Knockback Shield", _can_reach_depth(4)),
    ("Robin Hood Outfit", _can_reach_depth(4)),
    ("Hayabusa Boots", _can_reach_depth(5)),
    ("Repeater Crossbow", _can_reach_depth(5)),
    ("Shrapnel Axes", _can_reach_depth(5)),
    ("Drifter Outfit", _can_reach_depth(5)),
    ("Point Blank", _can_reach_depth(5)),
    ("Death Orb", _can_reach_depth(5)),
    ("Spiked Shield", _can_reach_depth(5)),
    ("Magic Missiles", _can_reach_depth(5)),
    ("Shaman Outfit", _can_reach_depth(5)),
    ("Wave of Denial", _can_reach_depth(7)),
    ("Powerful Grenade", _can_reach_depth(7)),
    ("Crusher", _can_reach_depth(7)),
    ("Open Wounds", _can_reach_depth(7)),
    ("Carduus Outfit", _can_reach_depth(7)),
    ("Tornado", _can_reach_depth(7)),
    ("Soldier's Resistance", _can_reach_depth(7)),
    ("Hayabusa Gauntlets", _can_reach_depth(7)),
    ("Dead Inside", _can_reach_depth(7)),
    ("Barrel Launcher", _can_reach_depth(7)),


    # ── Half life lore room ──────────────────────────────────────────────────
    ("Crowbar", _has("Teleportation Rune")),
    ("HEV Outfit", _has("Teleportation Rune")),

    # ── Collab skins ─────────────────────────────────────────────────────────
    ("Vessel's Outfit", _has("Pure Nail")),
    ("Pentinent's Outfit", _has("Face Flask")),

    (
    "Luchador's Outfit",
    lambda world: (
        lambda state:
            state.can_reach("Crypt", "Region", world.player)
            and _has_any_of(
                "Spartan Sandals",
                "Spiked Boots",
                "Hayabusa Boots",
                "Hayabusa Gauntlets",
            )(world)(state)
    )
),
    (
        "The Magician's Outfit",
        _has_all("Hard Light Sword", "Drifter Outfit")
    ),

    (
    "Explorer's Outfit",
    lambda world: lambda state: any(
        _can_reach_location_if_exists(state, world, loc)
        for loc in [
            "Throne Room Exit",
            "Crown Exit",
            "Master's Keep Exit",
        ]
        )
    ),

    (
        "Familiar Outfit",
        lambda world: (
            lambda state:
                state.has("Backpack", world.player)
                and state.can_reach_location("The Hand of the King", world.player)
        )
    ),

    ("Modernized Bomber Outfit", _has("Baseball Bat")),
    ("ZERO Outfit", _has("Hattori's Katana")),
    ("Shovel Knight Outfit", _has("Shovel")),


    # ── Scissor / Comb skin count gates ──────────────────────────────────────
    (
        "Sewing Scissors",
        lambda world: lambda state:
            _reach_skin_count(16)(world)(state)
    ),

    (
        "Giant Comb",
        lambda world: lambda state:
            _reach_skin_count(51)(world)(state)
    ),

    # ── King outfit chain ────────────────────────────────────────────────────
    ("King Outfit", _boss_killed("The Collector")),
    ("White King Outfit", _has("King Outfit")),


    # ── TickSacrifice ─────────────────────────────────────────────────────────
    ("Sacrificial Tick Outfit", _has("Mushroom Boi!")),


    # ── Specialist showroom unlock ───────────────────────────────────────────
    ("Golden Outfit", _has("The Specialist's Showroom")),

    # ── Heads ────────────────────────────────────────────────────────────────
    ("Flawless Torch",
        lambda world: lambda state:
            _can_reach_location_if_exists(state, world, "Kleio") and
            _can_reach_location_if_exists(state, world, "The Concierge") and
            _can_reach_location_if_exists(state, world, "Conjunctivius") and
            _can_reach_location_if_exists(state, world, "The Collector") and
            _can_reach_location_if_exists(state, world, "Scarecrow") and
            _can_reach_location_if_exists(state, world, "The Giant") and
            _can_reach_location_if_exists(state, world, "The Hand of the King") and
            _can_reach_location_if_exists(state, world, "Mama Tick") and
            _can_reach_location_if_exists(state, world, "The Queen") and
            _can_reach_location_if_exists(state, world, "The Time Keeper")),
    
    ("Leghugger Head", _has("Leghugger")),

    ("Mushroom Boi Cap", _has("Mushroom Boi!")),

    ("Bright Red Blowtorch", _has("Fire Blast")),

    ("Boss Cell Head", _bsc(5)),

    ("Guillain Head", _has("Boss Rush Unlock") and _has("Boss Rush Statue")),

    ("Concierge Flame", _boss_rush_trials_1_2()),
    ("Conjunctivius Tentacles", _boss_rush_trials_1_2()),
    ("Mama Tick Eye", _boss_rush_trials_1_2()),
    ("Time Keeper Mask", _boss_rush_trials_1_2()),
    ("Giant Flame", _boss_rush_trials_1_2()),
    ("Scarecrow Hat", _boss_rush_trials_1_2()),
    ("Hand of the King Flame", _boss_rush_trials_1_2()),
    ("Servant Mask", _boss_rush_trials_1_2()),
    ("Queen Flame", _boss_rush_trials_1_2()),
    ("Collector Hood", _boss_rush_trials_1_2()),

    ("Horde Zero Hood", _has_any_of(
        "Double Crossb-o-matic",
        "Sinew Slicer",
        "Heavy Turret",
        "Barnacle",
        "Cleaver",
        "Crusher",
        "Explosive Decoy",
        "Tesla Coil",
        "Scavenged Bombard"
    )), 

    ("Spatial Anomaly",
     lambda world: lambda state:
        _reach_head_count(31)(world)(state)),

    ("Red Hole",
    lambda world: lambda state: 
        _reach_head_count(7)(world)(state)),

    ("Fisherman Hood",
    lambda world: lambda state: 
        _reach_head_count(35)(world)(state)),
    
    ("Dark Vortex",
    lambda world: lambda state: 
        _reach_head_count(14)(world)(state)),

    ("Blue Hole",
    lambda world: (
        lambda state:
            state.has("Vine Rune", world.player)
            and state.has("Teleportation Rune", world.player)
            and state.has("Challenger's Rune", world.player)
            and state.has("Customization Rune", world.player)
            and state.has("Ram Rune", world.player)
            and state.has("Spider Rune", world.player)
            and state.has("Homunculus Rune", world.player)
            and state.has("Explorer's Rune", world.player)
            and state.has("Backpack", world.player)
            and state.has("Advanced Forge 1", world.player)
            and state.has("Recycling Tubes", world.player)
            and state.has("Hunter's Mirror", world.player)
            and state.has("The Specialist's Showroom", world.player)
            and state.has("Restock", world.player)
            and state.has("Merchandise Categories", world.player)
            and state.count("Progressive Flask", world.player) >= 4
            and state.count("Progressive Recycling", world.player) >= 2
            and state.count("Progressive Gold Reserves", world.player) >= 5
    )),
    
    ("Green Hole", _can_reach_nb_item_locations(75)),
    ("White Hole", _has("Cursed Flask")),
    
    ("Boss Rush Statue", _boss_rush_trials_1_2()),
    ("Cavern Key", _has("Homunculus Rune") and _has("Hand of the King Defeated")),
    ("High Jump", _has("Dash") or _has("High Jump")),
    ("Alucard's Sword", _has("High Jump")),
    ("Richter Mode Exit", _has("High Jump"))
]



# ─────────────────────────────────────────────────────────────────────────────
# Grouped check OR rules
# Applied in set_rules() — each Blueprint_X check is accessible if the player
# can reach ANY of the biomes where that item drops, at the right BC level.
# ─────────────────────────────────────────────────────────────────────────────

def _build_grouped_rules(world):
    if not hasattr(world, "grouped_location_sources"):
        return
    player = world.player
    multiworld = world.multiworld

    enabled_dlcs = set()

    if world.options.dlc_rise_of_the_giant.value:
        enabled_dlcs.add("RiseOfTheGiant")

    if world.options.dlc_the_bad_seed.value:
        enabled_dlcs.add("TheBadSeed")

    if world.options.dlc_fatal_falls.value:
        enabled_dlcs.add("FatalFalls")

    if world.options.dlc_the_queen_and_the_sea.value:
        enabled_dlcs.add("TheQueenAndTheSea")

    if world.options.dlc_return_to_castlevania.value:
        enabled_dlcs.add("Purple")

    existing_regions = {r.name for r in multiworld.regions if r.player == player}

    for location, sources in world.grouped_location_sources.items():
        # Filter valid sources once
        valid_sources = [
            s for s in sources
            if s["biome"] in existing_regions
        ]

        def make_rule(source_data):
            def rule(state):
                bc = get_bc_level(state, player)

                return any(
                    (s["dlc"] == "" or s["dlc"] in enabled_dlcs)
                    and s["min_bc"] <= bc <= s["max_bc"]
                    and state.can_reach(s["biome"], "Region", player)
                    for s in source_data
                )
            return rule
        try:
            loc_obj = multiworld.get_location(location, player)
        except KeyError:
            print(f"[GroupedRules] Missing location: {location}")
            continue

        biomes = {s["biome"] for s in valid_sources}

# ─────────────────────────────────────────────────────────────────────────────
# Main entry point — called from __init__.py set_rules()
# ─────────────────────────────────────────────────────────────────────────────
def set_rules(world: "DeadCellsWorld") -> None:
    """
    Apply all location-level rules to the multiworld.
    Skips rules for locations that don't exist in this world
    (e.g. DLC disabled, BC out of range).
    """
    multiworld = world.multiworld
    player = world.player

    # Build OR access rules for all grouped checks
    _build_grouped_rules(world)

    # Deduplicate: if a location appears multiple times, AND the rules together
    from collections import defaultdict
    rule_map: dict = defaultdict(list)
    for loc_name, rule_factory in LOCATION_RULES:
        rule_map[loc_name].append(rule_factory(world))

    for loc_name, rules in rule_map.items():
        try:
            location = multiworld.get_location(loc_name, player)
        except KeyError:
            continue

        add_rule(location, lambda state, rs=rules: all(r(state) for r in rs))