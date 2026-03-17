"""
Dead Cells - Archipelago World
rules.py

Location-level access rules that go beyond region entrance conditions.
These are applied after create_regions() in __init__.py via set_rules().

Rule categories:
  - BSC level requirements (static, based on world option)
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

if TYPE_CHECKING:
    from . import DeadCellsWorld


# ─────────────────────────────────────────────────────────────────────────────
# Skin item names (used for count-based rules)
# ─────────────────────────────────────────────────────────────────────────────
SKIN_ITEMS = [
    "PrisonerGold", "PrisonerSonGoku", "PrisonerBlack", "PrisonerGhost",
    "PrisonerSewers", "PrisonerSanta", "PrisonerStilt", "PrisonerSkeleton",
    "PrisonerCarduus", "PrisonerAphrodite", "PrisonerShaman", "PrisonerCloud",
    "PrisonerHyperlight", "PrisonerAladdin", "PrisonerBison", "PrisonerWarrior",
    "PrisonerMage", "PrisonerNeon", "PrisonerBobby", "PrisonerDemon",
    "PrisonerSylvanian", "PrisonerSand", "PrisonerGOG", "PrisonerFrench",
    "PrisonerXmas", "PrisonerGardener", "PrisonerFriendlyHardy", "PrisonerMushroom",
    "PrisonerFugitive", "PrisonerBlowgunner", "PrisonerTick", "RoyalGardener",
    "PrisonerRetro", "FreemanSkin", "PrisonerJavelinSnake", "PrisonerNecromant",
    "PrisonerBootleg", "PrisonerKamikaze", "PrisonerCrossbowMan", "PrisonerKillBill",
    "KingDefault", "KingWhite",
    "BehemothDefault", "Behemoth1", "Behemoth2", "Behemoth3", "Behemoth4",
    "BeholderDefault", "Beholder1", "Beholder2", "Beholder3", "Beholder4",
    "AssassinDefault", "Assassin1", "Assassin2", "Assassin3", "Assassin4",
    "GiantDefault", "Giant1", "Giant2", "Giant3", "Giant4",
    "HotkDefault", "Hotk1", "Hotk2", "Hotk3", "Hotk4",
    "Statue", "CollectorDefault",
    "TickDefault", "Tick1", "Tick2", "Tick3", "Tick4", "TickSacrifice",
    "GardenerDefault", "Gardener1", "Gardener2", "Gardener3", "Gardener4", "Cultist",
    "FlawlessBehemoth", "FlawlessBeholder", "FlawlessAssassin", "FlawlessGiant",
    "FlawlessHotk", "FlawlessTick", "FlawlessGardener",
    "Snowman", "SantaKLOS",
    "HollowKnight", "Blasphemous", "Guacamelee", "Skul", "HyperLightDrifter",
    "CurseofTheDeadGods", "SoulKnight",
    "Staphy", "ANCHORGUY",
    "ServanteDefault", "Servante1", "Servante2", "Servante3", "Servante4",
    "FlawlessServante", "QueenDefault", "Queen1", "Queen2", "Queen3", "Queen4",
    "FlawlessQueen", "BlueErinaceus",
    "Banker", "GuillainThief", "Bobby",
    "ShovelKnight", "HotlineMiamiChicken", "KatanaZero", "RiskOfRain",
    "Terraria", "SlayTheSpire",
    "Mentor", "Mentor1", "Mentor2", "Mentor3",
    "VictoriusBeheaded", "VictoriusBeheaded1", "VictoriusBeheaded2", "VictoriusBeheaded3",
    "Simon", "Alucard", "RichterROB", "Sypha", "Trevor", "Maria", "Hector",
    "HauntedArmor",
    "AdeleDefault", "Adele1", "Adele2", "Adele3", "Adele4", "FlawlessAdele",
    "DookuDefault", "Dooku1", "Dooku2", "Dooku3", "Dooku4", "FlawlessDooku",
]



# ─────────────────────────────────────────────────────────────────────────────
# Location rules table
#
# Each entry: ("location_name", rule_lambda_factory)
# The factory receives (world) and returns a state -> bool lambda.
#
# Helpers at the bottom of this file build the lambdas cleanly.
# ─────────────────────────────────────────────────────────────────────────────

def _has(item):
    """Rule: player has item in inventory."""
    return lambda world: (
        lambda state: state.has(item, world.player)
    )

def _has_all(*items):
    """Rule: player has ALL listed items."""
    return lambda world: (
        lambda state: all(state.has(i, world.player) for i in items)
    )

def _has_any(*items):
    """Rule: player has ANY of the listed items."""
    return lambda world: (
        lambda state: any(state.has(i, world.player) for i in items)
    )

def _has_all_any(*required_items, any_of):
    """Rule: player has all required_items AND at least one of any_of."""
    return lambda world: (
        lambda state: (
            all(state.has(i, world.player) for i in required_items)
            and any(state.has(i, world.player) for i in any_of)
        )
    )

def _bsc(level: int):
    """Rule: world boss_cells option >= level (static)."""
    return lambda world: (
        (lambda state: True) if world.options.boss_cells.value >= level
        else (lambda state: False)
    )

def _has_and_bsc(item: str, level: int):
    """Rule: has item AND boss_cells >= level."""
    return lambda world: (
        lambda state: state.has(item, world.player)
    ) if world.options.boss_cells.value >= level else (
        lambda world: lambda state: False
    )

def _skin_count(count: int):
    """Rule: player has received at least `count` Skin-category items."""
    return lambda world: (
        lambda state: sum(
            1 for skin in SKIN_ITEMS
            if state.has(skin, world.player)
        ) >= count
    )

def _boss_killed(location: str):
    """Rule: specific boss location has been checked."""
    return lambda world: (
        lambda state: state.can_reach_location(location, world.player)
    )

def _any_biome_exit(*biomes):
    """Rule: player has completed the biome_exit check of at least one biome."""
    return lambda world: (
        lambda state: any(
            state.can_reach_location(f"{b}_Exit", world.player)
            for b in biomes
        )
    )

def _has_and_boss(item: str, boss_loc: str):
    """Rule: has item AND boss kill completed."""
    return lambda world: (
        lambda state: (
            state.has(item, world.player)
            and state.can_reach_location(boss_loc, world.player)
        )
    )


# ─────────────────────────────────────────────────────────────────────────────
# The main rules table
# Format: (location_name, rule_factory)
# ─────────────────────────────────────────────────────────────────────────────
LOCATION_RULES = [

    # ── Gameplay items ────────────────────────────────────────────────────────
    ("Blueprint_P_Disengage", _has("HomKey")),
    ("Money5",  _has("HomKey")),
    
    # P_Health rule is applied on the enemy check below, not on P_Wishes
    # P_Health is a Perk dropped by Lancer (Castle biome), not a floor blueprint
    # Rule applied via enemy check: Castle_Blueprint_P_Health_from_Lancer

    ("Blueprint_SpeedBlade",    _has("ScoringKey")),
    ("Blueprint_DamageAura",    _has("ScoringKey")),
    ("Blueprint_DashSword",     _has("ScoringKey")),

    # MultiKickBoots requires 1+ BSC (dropped by Ninja in PrisonCourtyard)


    # ── LighthouseKey ─────────────────────────────────────────────────────────
    # LighthouseKey only appears in StiltVillage if player visited SewerShort
    ("Blueprint_LighthouseKey", lambda world: (
        lambda state: state.can_reach("SewerShort", "Region", world.player)
    )),
    # ── PrisonCourtyard mid-biome gate (LadderKey) ────────────────────────────
    # These items only drop from enemies in the locked zone of PrisonCourtyard
    ("Blueprint_BackBlink", _has("LadderKey")),
    ("Blueprint_BumpBoots", _has("LadderKey")),
    ("Blueprint_DamageBuff", _has("LadderKey")),
    ("Blueprint_Decoy", _has("LadderKey")),
    ("Blueprint_ExplosiveGrenade", _has("LadderKey")),
    ("Blueprint_GroundSaw", _has("LadderKey")),
    ("Blueprint_KnivesCircle", _has("LadderKey")),
    ("Blueprint_LowHealth", _has("LadderKey")),
    ("Blueprint_MultiCrossBow", _has("LadderKey")),
    ("Blueprint_MultiKickBoots", _has("LadderKey")),
    ("Blueprint_OilSword", _has("LadderKey")),
    ("Blueprint_P_DeathShield", _has("LadderKey")),
    ("Blueprint_PrisonerAphrodite", _has("LadderKey")),
    ("Blueprint_PrisonerBlack", _has("LadderKey")),
    ("Blueprint_PrisonerKamikaze", _has("LadderKey")),
    ("Blueprint_PrisonerNeon", _has("LadderKey")),
    ("Blueprint_PrisonerWarrior", _has("LadderKey")),
    ("Blueprint_Shockwave", _has("LadderKey")),
    
    ("Blueprint_LongBow", _has("LadderKey")),
    ("Blueprint_ExplosiveCrossBow", _has("LadderKey") and _has("BreakableGroundKey") and (_has("WallJumpKey") or _has("HomKey"))),

    # ── Lighthouse access (no LighthouseKey item yet) ─────────────────────────
    # Requires having visited SewerShort AND StiltVillage
    # More precise: SewerShort biome_enter AND StiltVillage biome_enter

    # ── Boss skin series (BSC gates) ──────────────────────────────────────────

    # ── Prisoner skin BSC gates ───────────────────────────────────────────────

    # ── Collab skins (item requirements) ─────────────────────────────────────
    ("Blueprint_HollowKnight", _has("PureNail")),
    ("Blueprint_Blasphemous", _has("FaceFlask")),
    # Guacamelee: requires visiting Crypt + having a kick-type boot
    # Boots (MultiKickBoots etc.) are useful items — promote MultiKickBoots to PROG
    # and simplify rule to just require Crypt + MultiKickBoots
    ("Blueprint_Guacamelee", lambda world: (
        lambda state: (
            state.can_reach("Crypt", "Region", world.player)
            and state.has("MultiKickBoots", world.player)
        )
    )),
    ("Blueprint_HyperLightDrifter",
        _has_all("HardLightSword", "PrisonerHyperlight")),
    ("Blueprint_CurseofTheDeadGods", lambda world: (
        lambda state: any(
            state.can_reach_location(loc, world.player)
            for loc in ["Throne_Exit", "QueenArena_Exit", "DookuArena_Exit"]
        )
    )),
    # Terraria: requires BackpackUnlock — rule disabled for now to avoid fill errors
    # TODO: re-enable once BackpackUnlock is confirmed as progression item
    ("Blueprint_Terraria", _has("BackpackUnlock") and _boss_killed("Boss_KingsHand")),
    ("Blueprint_HotlineMiamiChicken", _has("BaseballBat")),
    ("Blueprint_KatanaZero", _has("Katana")),
    ("Blueprint_ShovelKnight", _has("Shovel")),

    # ── Scissor / Comb (skin count gates) ────────────────────────────────────
    # Scissor/Comb: skin count gates disabled for now
    # AP cannot guarantee enough skins are reachable before these locations
    # TODO: re-enable with a more sophisticated count that respects BC/DLC filters
    # ("Blueprint_Scissor",   _skin_count(16)),
    # ("Blueprint_Comb",      _skin_count(51)),

    # ── KingDefault / KingWhite (boss kill chain) ─────────────────────────────
    ("Blueprint_KingDefault", _boss_killed("Boss_Collector")),
    ("Blueprint_KingWhite", _has("KingDefault")),

    # ── TickSacrifice ─────────────────────────────────────────────────────────
    ("Blueprint_TickSacrifice", _has("SpawnFriendlyHardy")),
    
    # ── PokebombUnlock ────────────────────────────────────────────────────────
    ("Blueprint_PrisonerGold", _has("PokebombUnlock")),

    # ── TODO: Cemetery -> Cavern rule (KingsHand vs bsc1 + HomKey) ────────────
    # Currently KingsHand boss kill is used in transition.json.
    # Needs in-game testing to confirm if HomKey is also required.
    # Uncomment and adjust once confirmed:
    # TODO: Cemetery->Cavern may also require HomKey — needs in-game testing
    
    # ── Heads ────────────────────────────────────────────────────────────────
    # TODO: (red/blue/green black hole heads) && (VortexFoundry, Pecheur, GlitchyHeadDeepSpace) && Flawless
    ("Item_StaphyHead", _has("SpawnLilStaphy")),
    ("Item_MushroomBoi", _has("SpawnFriendlyHardy")),
    ("Item_BlobbyFlameMagma", _boss_killed("Boss_KingsHand")),
    ("Item_BlowTorchRed", _has("FlameThrower")),
    ("Item_BossCellHead", _has("BossRune5")),
]



# ─────────────────────────────────────────────────────────────────────────────
# Grouped check OR rules
# Applied in set_rules() — each Blueprint_X check is accessible if the player
# can reach ANY of the biomes where that item drops, at the right BC level.
# ─────────────────────────────────────────────────────────────────────────────

def _build_grouped_rules(world: "DeadCellsWorld") -> None:
    """
    For every grouped check (region="Checks"), build an OR access rule:
    accessible if the player can reach ANY source biome at the right BC.
    """
    from .locations import LOCATION_TABLE, location_id
    multiworld = world.multiworld
    player = world.player
    bc_level = world.options.boss_cells.value
    enabled_dlcs = world.enabled_dlcs

    # Build set of region names that actually exist in this world
    existing_regions = {r.name for r in multiworld.regions if r.player == player}

    for loc_name, loc_data in LOCATION_TABLE.items():
        if loc_data["region"] != "Checks":
            continue
        try:
            location = multiworld.get_location(loc_name, player)
        except KeyError:
            continue

        sources = loc_data.get("sources", [])
        # Filter sources valid for this DLC + BC config AND whose region exists
        valid_sources = [
            s for s in sources
            if (s["dlc"] == "" or s["dlc"] in enabled_dlcs)
            and s["min_bc"] <= bc_level <= s["max_bc"]
            and s["biome"] in existing_regions
        ]
        if not valid_sources:
            location.access_rule = lambda state: False
            continue

        biomes = [s["biome"] for s in valid_sources]

        def make_rule(source_biomes):
            def rule(state):
                return any(
                    state.can_reach(b, "Region", player)
                    for b in source_biomes
                )
            return rule

        location.access_rule = make_rule(biomes)
        
        # Rare/Legendary blueprints require PokebombUnlock
        if loc_data.get("rarity") in ("Rare", "Legendary"):
            base_rule = location.access_rule
            def make_rarity_rule(existing_rule, p=player):
                def rule(state):
                    return existing_rule(state) and state.has("PokebombUnlock", p)
                return rule
            location.access_rule = make_rarity_rule(location.access_rule)

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
            # Location not in this world (DLC off, BC filtered, etc.)
            continue

        if len(rules) == 1:
            location.access_rule = rules[0]
        else:
            # AND all rules together
            def combined(state, _rules=rules):
                return all(r(state) for r in _rules)
            location.access_rule = combined
