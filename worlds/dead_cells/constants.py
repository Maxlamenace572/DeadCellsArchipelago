"""Constants shared by every module. No logic here."""
import json
import pkgutil

ITEM_BASE_ID = 0xDEAD_0000
LOCATION_BASE_ID = 0xDEAD_1000

#option attribute -> DLC id used in the JSON data files
DLC_OPTIONS = {
    "dlc_rise_of_the_giant": "RiseOfTheGiant",
    "dlc_the_bad_seed": "TheBadSeed",
    "dlc_fatal_falls": "FatalFalls",
    "dlc_the_queen_and_the_sea": "TheQueenAndTheSea",
    "dlc_return_to_castlevania": "Purple",
}

#option attribute -> trap item name (weights are relative, 0 disables a trap)
TRAP_WEIGHT_OPTIONS = {
    "trap_weight_curse": "Curse Trap",
    "trap_weight_elite": "Elite Trap",
    "trap_weight_gold": "Gold Trap",
    "trap_weight_weapon_break": "Weapon Break Trap",
    "trap_weight_reverse": "Reverse Trap",
    "trap_weight_challenge": "Challenge Trap",
}

HUB_REGION = "Checks"          #holds locations whose sources span several biomes
STEM_CELL = "Progressive Stem Cell"
SHOWROOM = "The Specialist's Showroom"
RARITY_NEEDS_SHOWROOM = {"ForceGrenade", "Uncommon", "Rare", "Legendary"}
COSMETIC_CATEGORIES = {"skin", "head"}
MAX_BC = 5


def world_version() -> str:
    """Single source of truth: archipelago.json."""
    return json.loads(pkgutil.get_data(__package__, "archipelago.json"))["world_version"]
