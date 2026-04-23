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
from worlds.generic.Rules import add_rule

if TYPE_CHECKING:
    from . import DeadCellsWorld


# ─────────────────────────────────────────────────────────────────────────────
# Skin item names (used for count-based rules)
# ─────────────────────────────────────────────────────────────────────────────
SKIN_ITEMS = [

    # base outfits
    "Golden Outfit", "Son Goku Outfit", "Black Outfit", "Ghost Outfit",
    "Sewers Outfit", "Santa Outfit", "Stilt Outfit", "Skeleton Outfit",
    "Carduus Outfit", "Aphrodite Outfit", "Shaman Outfit", "Cloud Outfit",
    "Hyper Light Drifter Outfit", "Aladdin Outfit", "Bison Outfit", "Warrior Outfit",
    "Mage Outfit", "Neon Outfit", "Bobby Outfit", "Demon Outfit",
    "Sylvanian Outfit", "Sand Outfit", "GOG Outfit", "French Outfit",
    "Festive Outfit", "Gardener Outfit", "Friendly Hardy Outfit", "Mushroom Outfit",
    "Fugitive Outfit", "Blowgunner Outfit", "Tick Outfit", "Royal Gardener Outfit",
    "Retro Outfit", "Gordon Freeman Outfit", "Javelin Snake Outfit", "Necromancer Outfit",
    "Bootleg Outfit", "Kamikaze Outfit", "Crossbowman Outfit", "Kill Bill Outfit",

    # king
    "King Outfit", "White King Outfit",

    # concierge
    "Concierge Outfit",
    "Piccolo Concierge Outfit",
    "Misunderstood Concierge Outfit",
    "Blacksmith Concierge Outfit",
    "Golden Concierge Outfit",

    # conjunctivius
    "Classic Conjunctivius Outfit",
    "Starved Conjunctivius Outfit",
    "Enraged Conjunctivius Outfit",
    "Tentacled Conjunctivius Outfit",
    "Aurora Borealis Conjunctivius Outfit",

    # time keeper
    "Classic Temporal Outfit",
    "Apex Temporal Outfit",
    "Red Temporal Outfit",
    "White Shadow Temporal Outfit",
    "Devilish Temporal Outfit",

    # giant
    "Classic Giant Outfit",
    "Mutineer Giant Outfit",
    "Royal Giant Outfit",
    "Frustrated Giant's Outfit",
    "Cavern Dweller Giant Outfit",

    # hand of the king
    "The Hand of the King Outfit",
    "Loyal Hand of the King Outfit",
    "Majestic Hand of the King Outfit",
    "Red Hand of the King Outfit",
    "The Leeching Hand of the King Outfit",

    "Statue Outfit",
    "Collector Outfit",

    # mama tick
    "Classic Mama Tick Outfit",
    "Sharp Mama Tick Outfit",
    "Wigged Mama Tick Outfit",
    "Scarlet Mama Tick Outfit",
    "Vibrant Mama Tick Outfit",
    "Sacrificial Tick Outfit",

    # scarecrow
    "Classic Scarecrow Outfit",
    "Rusted Scarecrow Outfit",
    "Cardinal Scarecrow Outfit",
    "Festering Scarecrow Outfit",
    "Murderous Scarecrow Outfit",
    "Cultist Outfit",

    # flawless boss outfits
    "Flawless Concierge Outfit",
    "Flawless Conjunctivius Outfit",
    "Flawless Time Keeper Outfit",
    "Flawless Giant Outfit",
    "Flawless Hand of the King Outfit",
    "Flawless Mama Tick Outfit",
    "Flawless Scarecrow Outfit",

    # misc
    "Snowman Outfit",
    "Santa Outfit",

    # crossover outfits
    "Hollow Knight Outfit",
    "Blasphemous Outfit",
    "Guacamelee Outfit",
    "Skul Outfit",
    "Hyper Light Drifter Outfit",
    "Curse of the Dead Gods Outfit",
    "Soul Knight Outfit",

    # pets / misc
    "Staphy Outfit",
    "Anchor Guy Outfit",

    # servants
    "Servants Outfit",
    "Burnished Servants Outfit",
    "Indigo Servants Outfit",
    "Shining Servants Outfit",
    "Luminous Servants Outfit",
    "Flawless Servants Outfit",

    # queen
    "Queen Outfit",
    "White Gold Queen Outfit",
    "Cherry Blossom Queen Outfit",
    "Spicy Queen Outfit",
    "Stinging Queen Outfit",
    "Flawless Queen Outfit",

    "Blue Erinaceus Outfit",

    # npcs
    "Banker Outfit",
    "Guillain Outfit",
    "Bobby Outfit",

    # indie crossovers
    "Shovel Knight Outfit",
    "Hotline Miami Outfit",
    "Katana ZERO Outfit",
    "Risk of Rain Outfit",
    "Terraria Outfit",
    "Slay the Spire Outfit",

    # boss rush
    "Mentor Outfit",
    "Mentor Outfit 1",
    "Mentor Outfit 2",
    "Mentor Outfit 3",

    "Victorious Outfit",
    "Victorious Outfit 1",
    "Victorious Outfit 2",
    "Victorious Outfit 3",

    # castlevania
    "Simon Outfit",
    "Alucard Outfit",
    "Richter Outfit",
    "Sypha Outfit",
    "Trevor Outfit",
    "Maria Outfit",
    "Hector Outfit",
    "Haunted Armor Outfit",

    # death
    "Death Outfit",
    "Sanguine Death Outfit",
    "Twilight Death Outfit",
    "Regal Death Outfit",
    "Pale Death Outfit",
    "Flawless Death Outfit",

    # dracula
    "Dracula Outfit",
    "Moonlit Dracula Outfit",
    "Grand Dracula Outfit",
    "Vampiric Dracula Outfit",
    "Dark Lord Dracula Outfit",
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
    "Bobby Flame",
    "Concierge Flame",
    "Giant Flame",
    "Queen Flame",
    "Hand of the King Flame",

    # boss themed heads
    "Conjunctivius Head",
    "Mama Tick Eye",
    "Time Keeper Hat",
    "Scarecrow Hat",
    "Servants Mask",
    "Collector Hood",

    # black hole variants
    "Black Hole",
    "White Black Hole",
    "Violet Black Hole",
    "Red Black Hole",
    "Green Black Hole",
    "Blue Black Hole",

    # vortex heads
    "Hello Darkness Vortex",
    "Bad Seed Vortex",
    "Queen and the Sea Vortex",
    "Foundry Vortex",

    # misc
    "Guillain Head",
    "Pecheur Head",
    "Staphy Head",
    "Flawless Head",
    "Cell Head",
    "Evil Empire Head",

    # blob heads
    "Blobby Flame",
    "Magma Blobby Flame",
    "Malaise Blobby Flame",
    "Gum Blobby Flame",

    # glitch heads
    "Glitchy Head",
    "Deep Space Glitchy Head",
    "Red Glitchy Head",

    # mushroom
    "Mushroom Boi Head",

    # torch heads
    "Black Blowtorch",
    "Blowtorch",
    "Gold Blowtorch",
    "Red Blowtorch",

    # misc uniques
    "Bitter",
    "Hordes Zero Hood",
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


def _skin_count(count: int):
    """Rule: player has received at least `count` skin items."""
    return lambda world: (
        lambda state: sum(
            1 for skin in SKIN_ITEMS
            if state.has(skin, world.player)
        ) >= count
    )


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
    at least 1 cleared Tier 3 boss.
    """
    return lambda world: (
        lambda state: (
            _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_1) >= 1
            and _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_2) >= 1
            and _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_3) >= 1
        )
    )


def _boss_rush_trials_3_4():
    """
    Trials 3 and 4:
    at least 2 cleared Tier 1 bosses,
    at least 2 cleared Tier 2 bosses,
    at least 1 cleared Tier 3 boss.
    """
    return lambda world: (
        lambda state: (
            _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_1) >= 2
            and _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_2) >= 2
            and _count_cleared_bosses(state, world.player, BOSS_RUSH_TIER_3) >= 1
        )
    )

def _head_count(count: int):
    """
    Rule: player has received at least `count` head cosmetics.
    """
    return lambda world: (
        lambda state: sum(
            1 for head in HEAD_ITEMS
            if state.has(head, world.player)
        ) >= count
    )

def _can_reach_location_if_exists(state, world, loc_name: str) -> bool:
    try:
        world.multiworld.get_location(loc_name, world.player)
    except KeyError:
        return False
    return state.can_reach_location(loc_name, world.player)

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
    ("Blueprint_P_Disengage", _has("Homunculus Rune")),
    ("Money5",  _has("Homunculus Rune")),
    ("Blueprint_P_AmmoOnHit", _has("Spider Rune")),

    ("Blueprint_SpeedBlade",    _has("Challenger's Rune")),
    ("Blueprint_DamageAura",    _has("Challenger's Rune")),
    ("Blueprint_DashSword",     _has("Challenger's Rune")),


    # ── Lighthouse Key logic ─────────────────────────────────────────────────
    ("Blueprint_LighthouseKey", lambda world: (
        lambda state: state.can_reach("SewerShort", "Region", world.player)
    )),


    # ── PrisonCourtyard mid-biome gate (Vine Rune) ────────────────────────────
    ("Blueprint_BackBlink", _has("Vine Rune")),
    ("Blueprint_BumpBoots", _has("Vine Rune")),
    ("Blueprint_DamageBuff", _has("Vine Rune")),
    ("Blueprint_Decoy", _has("Vine Rune")),
    ("Blueprint_ExplosiveGrenade", _has("Vine Rune")),
    ("Blueprint_GroundSaw", _has("Vine Rune")),
    ("Blueprint_KnivesCircle", _has("Vine Rune")),
    ("Blueprint_LowHealth", _has("Vine Rune")),
    ("Blueprint_MultiCrossBow", _has("Vine Rune")),
    ("Blueprint_MultiKickBoots", _has("Vine Rune")),
    ("Blueprint_OilSword", _has("Vine Rune")),
    ("Blueprint_P_DeathShield", _has("Vine Rune")),
    ("Blueprint_PrisonerAphrodite", _has("Vine Rune")),
    ("Blueprint_PrisonerBlack", _has("Vine Rune")),
    ("Blueprint_PrisonerKamikaze", _has("Vine Rune")),
    ("Blueprint_PrisonerNeon", _has("Vine Rune")),
    ("Blueprint_PrisonerWarrior", _has("Vine Rune")),
    ("Blueprint_Shockwave", _has("Vine Rune")),
    ("Blueprint_LongBow", _has("Vine Rune")),

    (
        "Blueprint_ExplosiveCrossBow",
        _has_all_any(
            ["Vine Rune", "Ram Rune"],
            any_of=["Spider Rune", "Homunculus Rune"]
        )
    ),

    ("PrisonCourtyard_Exit", _has("Vine Rune")),


    # ── Collab skins ─────────────────────────────────────────────────────────
    ("Blueprint_HollowKnight", _has("Pure Nail")),
    ("Blueprint_Blasphemous", _has("Face Flask")),

    (
    "Blueprint_Guacamelee",
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
        "Blueprint_HyperLightDrifter",
        _has_all("Hard Light Sword", "Hyper Light Drifter Outfit")
    ),

    (
<<<<<<< Updated upstream
        "Blueprint_CurseofTheDeadGods",
        lambda world: (
            lambda state: any(
                state.can_reach_location(loc, world.player)
                for loc in [
                    "Throne_Exit",
                    "QueenArena_Exit",
                    "DookuArena_Exit"
                ]
            )
=======
    "Curse of the Dead Gods Outfit",
    lambda world: lambda state: any(
        _can_reach_location_if_exists(state, world, loc)
        for loc in [
            "Throne Room Exit",
            "Crown Exit",
            "Master's Keep Exit",
        ]
>>>>>>> Stashed changes
        )
    ),

    (
        "Blueprint_Terraria",
        lambda world: (
            lambda state:
                state.has("Backpack", world.player)
                and state.can_reach_location("Boss_KingsHand", world.player)
        )
    ),

    ("Blueprint_HotlineMiamiChicken", _has("Baseball Bat")),
    ("Blueprint_KatanaZero", _has("Hattori's Katana")),
    ("Blueprint_ShovelKnight", _has("Shovel")),


    # ── Scissor / Comb skin count gates ──────────────────────────────────────
    (
        "Blueprint_Scissor",
        lambda world: lambda state:
            _skin_count(16)(world)(state)
            or state.can_reach("Throne", "Region", world.player)
    ),

    (
    "Blueprint_Comb",
    lambda world: (
        lambda state:
            _skin_count(51)(world)(state)
            or (
                state.can_reach("Throne", "Region", world.player)
                and get_bc_level(state, world.player) >= 5
            )
    )
),

    # ── King outfit chain ────────────────────────────────────────────────────
    ("Blueprint_KingDefault", _boss_killed("Boss_Collector")),
    ("Blueprint_KingWhite", _has("King Outfit")),


    # ── TickSacrifice ─────────────────────────────────────────────────────────
    ("Blueprint_TickSacrifice", _has("Mushroom Boi!")),


    # ── Specialist showroom unlock ───────────────────────────────────────────
    ("Blueprint_PrisonerGold", _has("Specialist's Showroom")),

    ("Blueprint_P_Wishes", _boss_rush_trials_3_4()),


    # ── Heads ────────────────────────────────────────────────────────────────
<<<<<<< Updated upstream
    ("Item_StaphyHead", _has("Leghugger")),

    ("Item_MushroomBoi", _has("Mushroom Boi!")),

    ("Item_BlobbyFlameMagma",
        _boss_killed("Boss_KingsHand")
    ),

    ("Item_BlowTorchRed", _has("Pyrotechnics")),
=======
    ("Leghugger Head", _has("Leghugger")),

    ("Mushroom Boi Cap", _has("Mushroom Boi!")),

    ("Magma Blob",
        _boss_killed("The Hand of the King")
    ),

    ("Bright Red Blowtorch", _has("Pyrotechnics")),
>>>>>>> Stashed changes

    ("Item_BossCellHead", _bsc(5)),

    ("Item_Guillain", _boss_rush_trials_1_2()),

<<<<<<< Updated upstream
    ("Blueprint_Bobby", _has("Progressive Stem Cell")),

    ("Item_GlitchyHeadDeepSpace",
=======
    ("Spatial Anomaly",
>>>>>>> Stashed changes
     lambda world: lambda state:
        _head_count(35)(world)(state) 
        or (state.can_reach("Throne", "Region", world.player)
        and get_bc_level(state, world.player) >= 5)),

    ("Item_BlackHoleRed",
    lambda world: lambda state: 
        _head_count(7)(world)(state)
        or (
                state.can_reach("Throne", "Region", world.player)
            )
    ),
<<<<<<< Updated upstream
    ("Item_Pecheur",
=======
    ("Fisherman's Hood",
>>>>>>> Stashed changes
    lambda world: lambda state: 
        _head_count(40)(world)(state)
        or (
                state.can_reach("Throne", "Region", world.player)
                and get_bc_level(state, world.player) >= 5
            )),
    
    ("Dark Vortex",
    lambda world: lambda state: 
        _head_count(15)(world)(state)
        or (
                state.can_reach("Throne", "Region", world.player)
                and get_bc_level(state, world.player) >= 5
            )),

    (
    "Item_BlackHoleBlue",
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
            and state.has("Specialist's Showroom", world.player)
            and state.has("Restock", world.player)
            and state.has("Merchandise Categories", world.player)
            and state.count("Progressive Flask", world.player) >= 4
            and state.count("Progressive Recycling", world.player) >= 2
            and state.count("Progressive Gold Reserves", world.player) >= 5
    )
    ),
    (
    "Item_BlackHoleGreen",
    lambda world: (
        lambda state:
            sum(
                state.count(item, world.player)
                for item, data in ITEM_TABLE.items()
                if 0x0200 <= data[0] <= 0x07FF
            ) >= 75
    )
    ),
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