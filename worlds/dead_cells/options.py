"""
Dead Cells - Archipelago World
options.py

All configurable options for a Dead Cells Archipelago session.
These appear in the player's YAML configuration file.
"""

from dataclasses import dataclass
from Options import (
    Choice,
    Toggle, DeathLink, Range, PerGameCommonOptions, FreeText, StartInventoryPool, OptionGroup
)


# ─────────────────────────────────────────────────────────────────────────────
# DLC Toggles
# ─────────────────────────────────────────────────────────────────────────────

class DLCRiseOfTheGiant(Toggle):
    """
    Include content from Rise of the Giant DLC.
    Adds biomes: Cavern, Giant, Astrolab, Observatory.
    Adds items: GiantKiller, SonicCrossbow, BleedAxe, GodAxe,
                ThrowingSpear, MagicSalve, ThunderShield, and more.
    Required to access 5BC route via Astrolab.
    """
    display_name = "DLC: Rise of the Giant"
    default = 0


class DLCTheBadSeed(Toggle):
    """
    Include content from The Bad Seed DLC.
    Adds biomes: Greenhouse, Swamp, SwampHeart.
    Adds items: SmokeBomb, ParryBlade, RhythmicBlade, Blowgun, and more.
    """
    display_name = "DLC: The Bad Seed"
    default = 0


class DLCFatalFalls(Toggle):
    """
    Include content from Fatal Falls DLC.
    Adds biomes: Tumulus, Cliff, GardenerStage.
    Adds items: SnakeFang, GiantStaff, Lantern, LightningRod, and more.
    """
    display_name = "DLC: Fatal Falls"
    default = 0


class DLCTheQueenAndTheSea(Toggle):
    """
    Include content from The Queen and the Sea DLC.
    Adds biomes: Shipwreck, Lighthouse, QueenArena.
    Adds items: Trident, HandHook, Shark, ElbowBlades, ThrowingCards, and more.
    """
    display_name = "DLC: The Queen and the Sea"
    default = 0


class DLCReturnToCastlevania(Toggle):
    """
    Include content from Return to Castlevania DLC.
    Adds biomes: PurpleGarden, DookuCastle, DookuCastleHard, DeathArena, DookuArena.
    Adds items: VampireKiller, AdeleScythe, Bible, Cross, BouncingStone, and more.
    """
    display_name = "DLC: Return to Castlevania"
    default = 0


# ─────────────────────────────────────────────────────────────────────────────
# Goal
# ─────────────────────────────────────────────────────────────────────────────

class BossCells(Range):
    """
    The Boss Cell difficulty required to complete the goal.
    The player must defeat the Hand of the King (or reach the End region)
    at this difficulty level or higher.

    0 = No Boss Cells (easiest)
    5 = 5 Boss Cells (hardest). The 5 Boss Cells ending is only reachable through the
        Astrolab and Observatory, so it REQUIRES the Rise of the Giant DLC:
        generation fails if you pick 5 without it.
    """
    display_name = "Boss Cells Goal"
    range_start = 0
    range_end = 5
    default = 2

class ScrewDistillery(Toggle):
    """
    Remove all "Derelict Distillery"-exclusive Locations from the pool, as well
    as its "Unlock" item (if your BSC goal is 0BSC this happens by default).
    """
    display_name = "Exclude Distillery"
    default = 0

# ─────────────────────────────────────────────────────────────────────────────
# Item pool options
# ─────────────────────────────────────────────────────────────────────────────

class TrapPercentage(Range):
    """
    Percentage of the item pool slots that will hold a trap instead of a useful/filler item.
    Traps are sent to the Dead Cells player and trigger negative in-game effects
    such as curses, elite spawns, gold loss, or inverted controls.
    Which traps are used is controlled by the individual trap weights below.
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 5

class _TrapWeight(Range):
    range_start = 0
    range_end = 10
    default = 1


class CurseTrapWeight(_TrapWeight):
    """
    Relative weight of the "Curse Trap" among the traps (0 = never, 10 = most likely).
    If every trap weight is 0, no trap is added to the pool.
    """
    display_name = "Curse Trap Weight"


class EliteTrapWeight(_TrapWeight):
    """
    Relative weight of the "Elite Trap" among the traps (0 = never, 10 = most likely).
    If every trap weight is 0, no trap is added to the pool.
    """
    display_name = "Elite Trap Weight"


class GoldTrapWeight(_TrapWeight):
    """
    Relative weight of the "Gold Trap" among the traps (0 = never, 10 = most likely).
    If every trap weight is 0, no trap is added to the pool.
    """
    display_name = "Gold Trap Weight"


class WeaponBreakTrapWeight(_TrapWeight):
    """
    Relative weight of the "Weapon Break Trap" among the traps (0 = never, 10 = most likely).
    If every trap weight is 0, no trap is added to the pool.
    """
    display_name = "Weapon Break Trap Weight"


class ReverseTrapWeight(_TrapWeight):
    """
    Relative weight of the "Reverse Trap" among the traps (0 = never, 10 = most likely).
    If every trap weight is 0, no trap is added to the pool.
    """
    display_name = "Reverse Trap Weight"


class ChallengeTrapWeight(_TrapWeight):
    """
    Relative weight of the "Challenge Trap" among the traps (0 = never, 10 = most likely).
    If every trap weight is 0, no trap is added to the pool.
    """
    display_name = "Challenge Trap Weight"


class EnemySanity(Toggle):
    """
    Adds a "Kill <enemy>" location for every enemy type: the first time you kill each one sends a check.
    Only enemies that can appear in your seed (enabled DLCs, reachable biomes, Boss Cells goal) get a location.
    Bosses are not included: they are already checks.
    """
    display_name = "Enemy Sanity"
    default = 0


class RoomRandomizer(Choice):
    """
    WIP, DO NOT BRING IN MULTIPLAYER
    Shuffles which biome each door leads to. A biome keeps its own exits and content; only destinations change.

    Off:     vanilla layout.
    Depth:   biomes of the same depth are shuffled together.
    Tier:    biomes are shuffled inside 3 groups (before the first bosses, between the first and second boss tiers,
             between the second and third), and the bosses of each tier are shuffled together, so every group
             still ends with a random boss of its tier.
    Chaotic: every biome and boss is shuffled with no constraint.
    """
    display_name = "Room Randomizer"
    option_off = 0
    option_depth = 1
    option_tier = 2
    option_chaotic = 3
    default = 0


class IncludeCosmetics(Toggle):
    """
    Include cosmetic items (skins and head accessories) in the item pool.
    When enabled, skins and head items are added as filler items that can
    appear in other players' worlds.
    When disabled, only gameplay-relevant items are in the pool, and
    extra filler slots are filled with consumables and gems.
    
    Noteably, disabling this will also disable the "Giant Comb" and 
    "Sewing Scissors" locations as they depend on cosmetic checks sent, but 
    they will still be in the item pool
    """
    display_name = "Include Cosmetics in Pool"
    default = 1


class IncludeAspects(Toggle):
    """
    Include the 13 Aspects as locations and items in the pool. 
    When enabled, your first 13 deaths will send an AP Item. 
    When disabled, you will start with all Aspects as items, and no 
    locations will exist for unlocking them.
    """
    display_name = "Include Aspects in Pool"
    default = 1


class IncludeBaseWeapons(Toggle):
    """
    Include base-game weapons that are available from the start
    without any blueprint (e.g. Quick Sword, Broad Sword, Dual Daggers).
    When disabled, these items are removed from the pool, making the
    randomizer more focused on blueprint unlocks.
    When enabled, they are added as useful filler items.
    """
    display_name = "Include Starting Weapons in Pool"
    default = 1


class IncludeBaseMutations(Toggle):
    """
    Include base-game mutations that are available from the start
    without any blueprint (e.g. Combo, Support, Necromancy).
    When disabled, these items are removed from the pool, making the
    randomizer more focused on blueprint unlocks.
    When enabled, they are added as useful filler items.
    """
    display_name = "Include Starting Mutations in Pool"
    default = 1


# ─────────────────────────────────────────────────────────────────────────────
# Multiplayer
# ─────────────────────────────────────────────────────────────────────────────

class DeadCellsDeathLink(Range):
    """
    When enabled, dying in Dead Cells sends a death signal to all other
    players with Death Link enabled in the multiworld session.
    Receiving a death signal will kill your current run when set to 0.
    With a positive value, give you that amount in curses instead of killing your run
    Negative values disable this option.
    """
    display_name = "Death/Curses Link"
    range_start = -1
    range_end = 500
    default = -1


class DeathLinkGroupName(FreeText):
    """
    You join a group, sending and receiving death links only to people in the
    same group (case sensitive). Leaving it blank will put you in the general group.
    """
    display_name = "Death Link Group"
    default = ""


class DisableDeathLinkForAspects(Toggle):
    """
    At the start of your game you have 13 aspects to find, and you'll have to die
    a lot on purpose. That's a little incompatible with Death Link, so with this
    option enabled you won't send Death Link while you still have aspects to check.
    """
    display_name = "Disable Death Link for Aspects"
    default = 1

    
class DeathTrap(Toggle):
    """
    Override Death/Curses Link. When enabled, it will send a death link upon death
    and will give you a random trap upon receiving a death link.
    """
    display_name = "Death Trap"
    default = 0


class DeathTrapLinkTrigger(Toggle):
    """
    Sub-option for Death Trap. When enabled, it will send a trap link upon
    receiving a death trap.
    """
    display_name = "Death Trap Link Trigger"
    default = 0


class DeadCellsDamageLink(Toggle):
    """
    When enabled, taking damage in Dead Cells sends damage points to all
    other players with Damage Link enabled in the multiworld session.
    The rate is 16 damage points for 1% health.
    """
    display_name = "Damage Link"
    default = 0


class DamageLinkGroupName(FreeText):
    """
    You join a group, sending and receiving damage links only to people in the
    same group (case sensitive). Leaving it blank will put you in the general group.
    """
    display_name = "Damage Link Group"
    default = ""


class DeadCellsHealthLink(Toggle):
    """
    When enabled, life is shared between all other Dead Cells players with Health
    Link enabled in the multiworld session. Taking damage, healing, and recovery are
    shared based on percentage. Dying will kill other players.
    """
    display_name = "Health Link"
    default = 0


class HealthLinkGroupName(FreeText):
    """
    You join a group, sending and receiving health links only to people in the
    same group (case sensitive). Leaving it blank will put you in the general group.
    """
    display_name = "Health Link Group"
    default = ""


class DeadCellsHealthCurseLink(Toggle):
    """
    Sub-option for Health Link. When enabled, curses too are shared between players.
    """
    display_name = "Health Curse Link"
    default = 0


class DeadCellsTrapLink(Toggle):
    """
    When enabled, traps are shared with all other Dead Cells players who have Trap
    Link enabled in the multiworld session. The same kind of trap is sent to every
    other player upon receiving one.
    """
    display_name = "Trap Link"
    default = 0


class TrapLinkGroupName(FreeText):
    """
    You join a group, sending and receiving trap links only to people in the
    same group (case sensitive). Leaving it blank will put you in the general group.
    """
    display_name = "Trap Link Group"
    default = ""



# ─────────────────────────────────────────────────────────────────────────────
# Gameplay
# ─────────────────────────────────────────────────────────────────────────────

class RespawnUpScroll(Toggle):
    """
    At the start of each run, every filler stat up scroll will be given again.
    """
    display_name = "Respawn Stat Up Scroll"
    default = 1
    
class GiveScrollOnFlawlessBoss(Toggle):
    """
    Gives you Epic Scrolls of Power the first time you beat a boss without taking
    a hit. It's best to use it with the Respawn Stat Up Scroll option enabled.
    """
    display_name = "Flawless Boss Scroll"
    default = 0

# ─────────────────────────────────────────────────────────────────────────────
# Option set — referenced in __init__.py as DeadCellsWorld.options_dataclass
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class DeadCellsOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool

    # DLC toggles
    dlc_rise_of_the_giant:      DLCRiseOfTheGiant
    dlc_the_bad_seed:           DLCTheBadSeed
    dlc_fatal_falls:            DLCFatalFalls
    dlc_the_queen_and_the_sea:  DLCTheQueenAndTheSea
    dlc_return_to_castlevania:  DLCReturnToCastlevania

    # Misc Randomization

    # Goal
    boss_cells:         BossCells
    enemy_sanity:       EnemySanity
    room_randomizer:    RoomRandomizer
    exclude_distillery: ScrewDistillery

    # Item pool
    trap_percentage:            TrapPercentage
    trap_weight_curse:          CurseTrapWeight
    trap_weight_elite:          EliteTrapWeight
    trap_weight_gold:           GoldTrapWeight
    trap_weight_weapon_break:   WeaponBreakTrapWeight
    trap_weight_reverse:        ReverseTrapWeight
    trap_weight_challenge:      ChallengeTrapWeight
    include_cosmetics:          IncludeCosmetics
    include_aspects:            IncludeAspects
    include_base_weapons:       IncludeBaseWeapons
    include_base_mutations:     IncludeBaseMutations

    # Multiplayer
    death_link:         DeadCellsDeathLink
    death_link_group:   DeathLinkGroupName
    death_link_aspect:  DisableDeathLinkForAspects
    death_trap:         DeathTrap
    death_trap_link:    DeathTrapLinkTrigger
    
    damage_link:        DeadCellsDamageLink
    damage_link_group:  DamageLinkGroupName
    
    health_link:        DeadCellsHealthLink
    health_link_group:  HealthLinkGroupName
    health_curse_link:  DeadCellsHealthCurseLink
    
    trap_link:          DeadCellsTrapLink
    trap_link_group:    TrapLinkGroupName
    
    # Gameplay
    respawn_up:         RespawnUpScroll
    flawless_scroll:    GiveScrollOnFlawlessBoss

dead_cells_option_groups = [
    OptionGroup(
        "DLC Settings",
        [DLCRiseOfTheGiant, DLCTheBadSeed, DLCFatalFalls, DLCTheQueenAndTheSea, DLCReturnToCastlevania]
    ),
    OptionGroup(
        "Goal Settings",
        [BossCells, ScrewDistillery]
    ),
    OptionGroup(
        "Extra Locations",
        [EnemySanity]
    ),
    OptionGroup(
        "Room Randomizer",
        [RoomRandomizer]
    ),
    OptionGroup(
        "Item Pool Settings",
        [IncludeCosmetics, IncludeAspects, IncludeBaseWeapons, IncludeBaseMutations, TrapPercentage]
    ),
    OptionGroup(
        "Trap Weights",
        [CurseTrapWeight, EliteTrapWeight, GoldTrapWeight, WeaponBreakTrapWeight, ReverseTrapWeight, ChallengeTrapWeight]
    ),
    OptionGroup(
        "Multiplayer Link Settings",
        [
            DeadCellsDeathLink, 
            DeathLinkGroupName, 
            DisableDeathLinkForAspects, 
            DeathTrap, 
            DeathTrapLinkTrigger, 
            DeadCellsDamageLink, 
            DamageLinkGroupName,
            DeadCellsHealthLink,
            HealthLinkGroupName,
            DeadCellsHealthCurseLink,
            DeadCellsTrapLink,
            TrapLinkGroupName,
         ]
    ),
    OptionGroup(
        "Gameplay Settings",
        [RespawnUpScroll, GiveScrollOnFlawlessBoss]
    )
    
]
