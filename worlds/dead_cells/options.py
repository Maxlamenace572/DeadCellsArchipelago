"""
Dead Cells - Archipelago World
options.py

All configurable options for a Dead Cells Archipelago session.
These appear in the player's YAML configuration file.
"""

from dataclasses import dataclass
from Options import (
    Toggle, DeathLink, Range, PerGameCommonOptions,
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
    5 = 5 Boss Cells (hardest, requires Rise of the Giant DLC for Astrolab route)

    Note: Setting this to 5 without enabling Rise of the Giant DLC will
    restrict the 5BC Astrolab route, so the Throne -> End path will be used.
    """
    display_name = "Boss Cells Goal"
    range_start = 0
    range_end = 5
    default = 2


# ─────────────────────────────────────────────────────────────────────────────
# Item pool options
# ─────────────────────────────────────────────────────────────────────────────

class TrapPercentage(Range):
    """
    Percentage of filler item slots that will be replaced by trap items.
    Traps are sent to the Dead Cells player and trigger negative in-game effects
    such as curses, elite spawns, gold loss, or inverted controls.

    0  = No traps
    25 = 25% of fillers are traps (recommended)
    100 = All filler slots are traps (very punishing)
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 5


class IncludeCosmetics(Toggle):
    """
    Include cosmetic items (skins and head accessories) in the item pool.
    When enabled, skins and head items are added as filler items that can
    appear in other players' worlds.
    When disabled, only gameplay-relevant items are in the pool, and
    extra filler slots are filled with consumables and gems.
    """
    display_name = "Include Cosmetics in Pool"
    default = 1


class IncludeBaseWeapons(Toggle):
    """
    Include base-game weapons and skills that are available from the start
    without any blueprint (e.g. Quick Sword, Broad Sword, Dual Daggers).
    When disabled, these items are removed from the pool, making the
    randomizer more focused on blueprint unlocks.
    When enabled, they are added as useful filler items.
    """
    display_name = "Include Starting Weapons in Pool"
    default = 1


# ─────────────────────────────────────────────────────────────────────────────
# Multiplayer
# ─────────────────────────────────────────────────────────────────────────────

class DeadCellsDeathLink(Range):
    """
    When enabled, dying in Dead Cells sends a death signal to all other
    players with Death Link enabled in the multiworld session.
    Receiving a death signal will kill your current run when set to 0.
    With a positve value, give you that amount in curses instead of killing your run
    Negative values disable this option.
    """
    display_name = "Death/Curses Link"
    range_start = -1
    range_end = 500
    default = -1


# ─────────────────────────────────────────────────────────────────────────────
# Option set — referenced in __init__.py as DeadCellsWorld.options_dataclass
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class DeadCellsOptions(PerGameCommonOptions):
    # DLC toggles
    dlc_rise_of_the_giant:    DLCRiseOfTheGiant
    dlc_the_bad_seed:         DLCTheBadSeed
    dlc_fatal_falls:          DLCFatalFalls
    dlc_the_queen_and_the_sea: DLCTheQueenAndTheSea
    dlc_return_to_castlevania: DLCReturnToCastlevania

    # Goal
    boss_cells: BossCells

    # Item pool
    trap_percentage:       TrapPercentage
    include_cosmetics:     IncludeCosmetics
    include_base_weapons:  IncludeBaseWeapons

    # Multiplayer
    death_link: DeadCellsDeathLink
