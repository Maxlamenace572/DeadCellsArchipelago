from Options import Choice, Toggle, PerGameCommonOptions

class MaxBossCells(Choice):
    display_name = "Maximum Boss Stem Cells"
    option_0bc = 0
    option_1bc = 1
    option_2bc = 2
    option_3bc = 3
    option_4bc = 4
    option_5bc = 5
    default = 0

class RiseOfTheGiant(Toggle):
    display_name = "Rise of the Giant DLC"

class BadSeed(Toggle):
    display_name = "The Bad Seed DLC"

class FatalFalls(Toggle):
    display_name = "Fatal Falls DLC"

class QueenAndTheSea(Toggle):
    display_name = "The Queen and the Sea DLC"

class ReturnToCastlevania(Toggle):
    display_name = "Return to Castlevania DLC"

class DeadCellsOptions(PerGameCommonOptions):
    max_boss_cells: MaxBossCells
    rise_of_the_giant: RiseOfTheGiant
    bad_seed: BadSeed
    fatal_falls: FatalFalls
    queen_and_the_sea: QueenAndTheSea
    return_to_castlevania: ReturnToCastlevania