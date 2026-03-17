from typing import Dict, Set
from BaseClasses import Location

BASE_ID = 0xDEAD_1000

class DeadCellsLocation(Location):
    game: str = "Dead Cells"

class CheckType:
    BIOME_ENTER          = "biome_enter"
    BIOME_EXIT           = "biome_exit"
    BLUEPRINT_FLOOR      = "blueprint_floor"
    BLUEPRINT_ENEMY      = "blueprint_enemy"
    ITEM_NO_BLUEPRINT    = "item_no_blueprint"
    RUNE                 = "rune"
    BOSS                 = "boss"

LOCATION_TABLE: Dict[str, dict] = {
    "PrisonStart_Enter": {"id": 0x0000, "region": "PrisonStart", "type": "biome_enter", "dlc": "", "item": None},
    "PrisonStart_Exit": {"id": 0x0001, "region": "PrisonStart", "type": "biome_exit", "dlc": "", "item": None},
    "PrisonCourtyard_Enter": {"id": 0x0002, "region": "PrisonCourtyard", "type": "biome_enter", "dlc": "", "item": None},
    "PrisonCourtyard_Exit": {"id": 0x0003, "region": "PrisonCourtyard", "type": "biome_exit", "dlc": "", "item": None},
    "SewerShort_Enter": {"id": 0x0004, "region": "SewerShort", "type": "biome_enter", "dlc": "", "item": None},
    "SewerShort_Exit": {"id": 0x0005, "region": "SewerShort", "type": "biome_exit", "dlc": "", "item": None},
    "PrisonDepths_Enter": {"id": 0x0006, "region": "PrisonDepths", "type": "biome_enter", "dlc": "", "item": None},
    "PrisonDepths_Exit": {"id": 0x0007, "region": "PrisonDepths", "type": "biome_exit", "dlc": "", "item": None},
    "PrisonCorrupt_Enter": {"id": 0x0008, "region": "PrisonCorrupt", "type": "biome_enter", "dlc": "", "item": None},
    "PrisonCorrupt_Exit": {"id": 0x0009, "region": "PrisonCorrupt", "type": "biome_exit", "dlc": "", "item": None},
    "PrisonRoof_Enter": {"id": 0x000A, "region": "PrisonRoof", "type": "biome_enter", "dlc": "", "item": None},
    "PrisonRoof_Exit": {"id": 0x000B, "region": "PrisonRoof", "type": "biome_exit", "dlc": "", "item": None},
    "Ossuary_Enter": {"id": 0x000C, "region": "Ossuary", "type": "biome_enter", "dlc": "", "item": None},
    "Ossuary_Exit": {"id": 0x000D, "region": "Ossuary", "type": "biome_exit", "dlc": "", "item": None},
    "SewerDepths_Enter": {"id": 0x000E, "region": "SewerDepths", "type": "biome_enter", "dlc": "", "item": None},
    "SewerDepths_Exit": {"id": 0x000F, "region": "SewerDepths", "type": "biome_exit", "dlc": "", "item": None},
    "Bridge_Enter": {"id": 0x0010, "region": "Bridge", "type": "biome_enter", "dlc": "", "item": None},
    "Bridge_Exit": {"id": 0x0011, "region": "Bridge", "type": "biome_exit", "dlc": "", "item": None},
    "BeholderPit_Enter": {"id": 0x0012, "region": "BeholderPit", "type": "biome_enter", "dlc": "", "item": None},
    "BeholderPit_Exit": {"id": 0x0013, "region": "BeholderPit", "type": "biome_exit", "dlc": "", "item": None},
    "StiltVillage_Enter": {"id": 0x0014, "region": "StiltVillage", "type": "biome_enter", "dlc": "", "item": None},
    "StiltVillage_Exit": {"id": 0x0015, "region": "StiltVillage", "type": "biome_exit", "dlc": "", "item": None},
    "AncientTemple_Enter": {"id": 0x0016, "region": "AncientTemple", "type": "biome_enter", "dlc": "", "item": None},
    "AncientTemple_Exit": {"id": 0x0017, "region": "AncientTemple", "type": "biome_exit", "dlc": "", "item": None},
    "Cemetery_Enter": {"id": 0x0018, "region": "Cemetery", "type": "biome_enter", "dlc": "", "item": None},
    "Cemetery_Exit": {"id": 0x0019, "region": "Cemetery", "type": "biome_exit", "dlc": "", "item": None},
    "ClockTower_Enter": {"id": 0x001A, "region": "ClockTower", "type": "biome_enter", "dlc": "", "item": None},
    "ClockTower_Exit": {"id": 0x001B, "region": "ClockTower", "type": "biome_exit", "dlc": "", "item": None},
    "Crypt_Enter": {"id": 0x001C, "region": "Crypt", "type": "biome_enter", "dlc": "", "item": None},
    "Crypt_Exit": {"id": 0x001D, "region": "Crypt", "type": "biome_exit", "dlc": "", "item": None},
    "TopClockTower_Enter": {"id": 0x001E, "region": "TopClockTower", "type": "biome_enter", "dlc": "", "item": None},
    "TopClockTower_Exit": {"id": 0x001F, "region": "TopClockTower", "type": "biome_exit", "dlc": "", "item": None},
    "Cavern_Enter": {"id": 0x0020, "region": "Cavern", "type": "biome_enter", "dlc": "RiseOfTheGiant", "item": None},
    "Cavern_Exit": {"id": 0x0021, "region": "Cavern", "type": "biome_exit", "dlc": "RiseOfTheGiant", "item": None},
    "Giant_Enter": {"id": 0x0022, "region": "Giant", "type": "biome_enter", "dlc": "RiseOfTheGiant", "item": None},
    "Giant_Exit": {"id": 0x0023, "region": "Giant", "type": "biome_exit", "dlc": "RiseOfTheGiant", "item": None},
    "Castle_Enter": {"id": 0x0024, "region": "Castle", "type": "biome_enter", "dlc": "", "item": None},
    "Castle_Exit": {"id": 0x0025, "region": "Castle", "type": "biome_exit", "dlc": "", "item": None},
    "Distillery_Enter": {"id": 0x0026, "region": "Distillery", "type": "biome_enter", "dlc": "", "item": None},
    "Distillery_Exit": {"id": 0x0027, "region": "Distillery", "type": "biome_exit", "dlc": "", "item": None},
    "Throne_Enter": {"id": 0x0028, "region": "Throne", "type": "biome_enter", "dlc": "", "item": None},
    "Throne_Exit": {"id": 0x0029, "region": "Throne", "type": "biome_exit", "dlc": "", "item": None},
    "Astrolab_Enter": {"id": 0x002A, "region": "Astrolab", "type": "biome_enter", "dlc": "RiseOfTheGiant", "item": None, "min_bc": 5},
    "Astrolab_Exit": {"id": 0x002B, "region": "Astrolab", "type": "biome_exit", "dlc": "RiseOfTheGiant", "item": None, "min_bc": 5},
    "Observatory_Enter": {"id": 0x002C, "region": "Observatory", "type": "biome_enter", "dlc": "RiseOfTheGiant", "item": None, "min_bc": 5},
    "Observatory_Exit": {"id": 0x002D, "region": "Observatory", "type": "biome_exit", "dlc": "RiseOfTheGiant", "item": None, "min_bc": 5},
    "Greenhouse_Enter": {"id": 0x002E, "region": "Greenhouse", "type": "biome_enter", "dlc": "TheBadSeed", "item": None},
    "Greenhouse_Exit": {"id": 0x002F, "region": "Greenhouse", "type": "biome_exit", "dlc": "TheBadSeed", "item": None},
    "Swamp_Enter": {"id": 0x0030, "region": "Swamp", "type": "biome_enter", "dlc": "TheBadSeed", "item": None},
    "Swamp_Exit": {"id": 0x0031, "region": "Swamp", "type": "biome_exit", "dlc": "TheBadSeed", "item": None},
    "SwampHeart_Enter": {"id": 0x0032, "region": "SwampHeart", "type": "biome_enter", "dlc": "TheBadSeed", "item": None},
    "SwampHeart_Exit": {"id": 0x0033, "region": "SwampHeart", "type": "biome_exit", "dlc": "TheBadSeed", "item": None},
    "Tumulus_Enter": {"id": 0x0034, "region": "Tumulus", "type": "biome_enter", "dlc": "FatalFalls", "item": None},
    "Tumulus_Exit": {"id": 0x0035, "region": "Tumulus", "type": "biome_exit", "dlc": "FatalFalls", "item": None},
    "Cliff_Enter": {"id": 0x0036, "region": "Cliff", "type": "biome_enter", "dlc": "FatalFalls", "item": None},
    "Cliff_Exit": {"id": 0x0037, "region": "Cliff", "type": "biome_exit", "dlc": "FatalFalls", "item": None},
    "GardenerStage_Enter": {"id": 0x0038, "region": "GardenerStage", "type": "biome_enter", "dlc": "FatalFalls", "item": None},
    "GardenerStage_Exit": {"id": 0x0039, "region": "GardenerStage", "type": "biome_exit", "dlc": "FatalFalls", "item": None},
    "Shipwreck_Enter": {"id": 0x003A, "region": "Shipwreck", "type": "biome_enter", "dlc": "TheQueenAndTheSea", "item": None},
    "Shipwreck_Exit": {"id": 0x003B, "region": "Shipwreck", "type": "biome_exit", "dlc": "TheQueenAndTheSea", "item": None},
    "Lighthouse_Enter": {"id": 0x003C, "region": "Lighthouse", "type": "biome_enter", "dlc": "TheQueenAndTheSea", "item": None},
    "Lighthouse_Exit": {"id": 0x003D, "region": "Lighthouse", "type": "biome_exit", "dlc": "TheQueenAndTheSea", "item": None},
    "QueenArena_Enter": {"id": 0x003E, "region": "QueenArena", "type": "biome_enter", "dlc": "TheQueenAndTheSea", "item": None},
    "QueenArena_Exit": {"id": 0x003F, "region": "QueenArena", "type": "biome_exit", "dlc": "TheQueenAndTheSea", "item": None},
    "Bank_Enter": {"id": 0x0040, "region": "Bank", "type": "biome_enter", "dlc": "", "item": None},
    "Bank_Exit": {"id": 0x0041, "region": "Bank", "type": "biome_exit", "dlc": "", "item": None},
    "PurpleGarden_Enter": {"id": 0x0042, "region": "PurpleGarden", "type": "biome_enter", "dlc": "Purple", "item": None},
    "PurpleGarden_Exit": {"id": 0x0043, "region": "PurpleGarden", "type": "biome_exit", "dlc": "Purple", "item": None},
    "DookuCastle_Enter": {"id": 0x0044, "region": "DookuCastle", "type": "biome_enter", "dlc": "Purple", "item": None},
    "DookuCastle_Exit": {"id": 0x0045, "region": "DookuCastle", "type": "biome_exit", "dlc": "Purple", "item": None},
    "DookuCastleHard_Enter": {"id": 0x0046, "region": "DookuCastleHard", "type": "biome_enter", "dlc": "Purple", "item": None},
    "DookuCastleHard_Exit": {"id": 0x0047, "region": "DookuCastleHard", "type": "biome_exit", "dlc": "Purple", "item": None},
    "DeathArena_Enter": {"id": 0x0048, "region": "DeathArena", "type": "biome_enter", "dlc": "Purple", "item": None},
    "DeathArena_Exit": {"id": 0x0049, "region": "DeathArena", "type": "biome_exit", "dlc": "Purple", "item": None},
    "DookuArena_Enter": {"id": 0x004A, "region": "DookuArena", "type": "biome_enter", "dlc": "Purple", "item": None},
    "DookuArena_Exit": {"id": 0x004B, "region": "DookuArena", "type": "biome_exit", "dlc": "Purple", "item": None},
    "Challenge_Enter": {"id": 0x004C, "region": "Challenge", "type": "biome_enter", "dlc": "", "item": None},
    "Challenge_Exit": {"id": 0x004D, "region": "Challenge", "type": "biome_exit", "dlc": "", "item": None},
    "Rune_LadderKey": {"id": 0x004E, "region": "PrisonCourtyard", "type": "rune", "dlc": "", "item": "LadderKey"},
    "Rune_TeleportKey": {"id": 0x004F, "region": "SewerShort", "type": "rune", "dlc": "", "item": "TeleportKey"},
    "Rune_CustomKey": {"id": 0x0050, "region": "PrisonRoof", "type": "rune", "dlc": "", "item": "CustomKey"},
    "Rune_BreakableGroundKey": {"id": 0x0051, "region": "Ossuary", "type": "rune", "dlc": "", "item": "BreakableGroundKey"},
    "Rune_WallJumpKey": {"id": 0x0052, "region": "AncientTemple", "type": "rune", "dlc": "", "item": "WallJumpKey"},
    "Rune_ExploKey": {"id": 0x0053, "region": "Crypt", "type": "rune", "dlc": "", "item": "ExploKey"},
    "Boss_Behemoth": {"id": 0x0054, "region": "Bridge", "type": "boss", "dlc": "", "item": None},
    "Boss_Beholder": {"id": 0x0055, "region": "BeholderPit", "type": "boss", "dlc": "", "item": None},
    "Boss_TimeKeeper": {"id": 0x0056, "region": "TopClockTower", "type": "boss", "dlc": "", "item": None},
    "Boss_Giant": {"id": 0x0057, "region": "Giant", "type": "boss", "dlc": "RiseOfTheGiant", "item": None},
    "Boss_KingsHand": {"id": 0x0058, "region": "Throne", "type": "boss", "dlc": "", "item": None},
    "Boss_Collector": {"id": 0x0059, "region": "Observatory", "type": "boss", "dlc": "RiseOfTheGiant", "item": None, "min_bc": 5},
    "Boss_MamaTick": {"id": 0x005A, "region": "SwampHeart", "type": "boss", "dlc": "TheBadSeed", "item": None},
    "Boss_GardenerBoss": {"id": 0x005B, "region": "GardenerStage", "type": "boss", "dlc": "FatalFalls", "item": None},
    "Boss_AmazonSurvival": {"id": 0x005C, "region": "Lighthouse", "type": "boss", "dlc": "TheQueenAndTheSea", "item": None},
    "Boss_AmazonTactic": {"id": 0x005D, "region": "Lighthouse", "type": "boss", "dlc": "TheQueenAndTheSea", "item": None},
    "Boss_AmazonBrutal": {"id": 0x005E, "region": "Lighthouse", "type": "boss", "dlc": "TheQueenAndTheSea", "item": None},
    "Boss_Queen": {"id": 0x005F, "region": "QueenArena", "type": "boss", "dlc": "TheQueenAndTheSea", "item": None},
    "Boss_Death": {"id": 0x0060, "region": "DeathArena", "type": "boss", "dlc": "Purple", "item": None},
    "Boss_DookuBeast": {"id": 0x0061, "region": "DookuArena", "type": "boss", "dlc": "Purple", "item": None},
    "Blueprint_FastBow": {
        "id": 0x0062, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "FastBow",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_MagicBow": {
        "id": 0x0063, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "MagicBow",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_P_Disengage": {
        "id": 0x0064, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Disengage",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_P_Wishes": {
        "id": 0x0065, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Wishes",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_RoyalGardener": {
        "id": 0x0066, "region": "Checks", "type": "blueprint_floor",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "RoyalGardener",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_floor'}],
    },
    "Blueprint_FreemanSkin": {
        "id": 0x0067, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "FreemanSkin",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_SoulKnight": {
        "id": 0x0068, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "SoulKnight",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Terraria": {
        "id": 0x0069, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Terraria",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Bobby": {
        "id": 0x006A, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Bobby",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Item_Crowbar": {
        "id": 0x006B, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Crowbar",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_MachetePistol": {
        "id": 0x006C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "MachetePistol",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_HardLightSword": {
        "id": 0x006D, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "HardLightSword",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_PureNail": {
        "id": 0x006E, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "PureNail",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_SkulBone": {
        "id": 0x006F, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "SkulBone",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_NunchuckPan": {
        "id": 0x0070, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "NunchuckPan",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BaseballBat": {
        "id": 0x0071, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BaseballBat",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_KingScepter": {
        "id": 0x0072, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "KingScepter",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_Starfury": {
        "id": 0x0073, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Starfury",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ThrowableStuff": {
        "id": 0x0074, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ThrowableStuff",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_LaserGlaive": {
        "id": 0x0075, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "LaserGlaive",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_DiverseDeckJuggernaut": {
        "id": 0x0076, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "DiverseDeckJuggernaut",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_FaceFlask": {
        "id": 0x0077, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "FaceFlask",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_PolloPower": {
        "id": 0x0078, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "PolloPower",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_SpeedBlade": {
        "id": 0x0079, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "SpeedBlade",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_DamageAura": {
        "id": 0x007A, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "DamageAura",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_DashSword": {
        "id": 0x007B, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "DashSword",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_HollowKnight": {
        "id": 0x007C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "HollowKnight",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_Blasphemous": {
        "id": 0x007D, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Blasphemous",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_Guacamelee": {
        "id": 0x007E, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Guacamelee",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_HyperLightDrifter": {
        "id": 0x007F, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "HyperLightDrifter",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_CurseofTheDeadGods": {
        "id": 0x0080, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "CurseofTheDeadGods",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_HotlineMiamiChicken": {
        "id": 0x0081, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "HotlineMiamiChicken",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_KatanaZero": {
        "id": 0x0082, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "KatanaZero",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_Scissor": {
        "id": 0x0083, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Scissor",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_Comb": {
        "id": 0x0084, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Comb",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_P_DeathShield": {
        "id": 0x0085, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DeathShield", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'PrisonCourtyard', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'SewerDepths', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'StiltVillage', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Crypt', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Cavern', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Distillery', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Astrolab', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Cliff', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Bank', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}],
    },
    "Blueprint_P_DodgeHeal": {
        "id": 0x0086, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "P_DodgeHeal",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'SewerShort', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'PrisonDepths', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'PrisonRoof', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'StiltVillage', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Castle', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Greenhouse', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Swamp', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Cliff', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Shipwreck', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'Rampager'}],
    },
    "Blueprint_HorizontalTurret": {
        "id": 0x0087, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HorizontalTurret", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 1, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Zombie'}],
    },
    "Blueprint_Bleeder": {
        "id": 0x0088, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Bleeder",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 1, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Zombie'}],
    },
    "Blueprint_PrisonerBobby": {
        "id": 0x0089, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "PrisonerBobby", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 1, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Zombie'}],
    },
    "Blueprint_P_AttackSpeed_Combo": {
        "id": 0x008A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "P_AttackSpeed_Combo", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'PrisonRoof', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'ClockTower', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Cavern', 'min_bc': 2, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Distillery', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}],
    },
    "Blueprint_HeavyAxe": {
        "id": 0x008B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "HeavyAxe",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'PrisonRoof', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'ClockTower', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Cavern', 'min_bc': 2, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Distillery', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}],
    },
    "Blueprint_CloseCombatBow": {
        "id": 0x008C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "CloseCombatBow",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 3, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}],
    },
    "Blueprint_FrostBow": {
        "id": 0x008D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FrostBow", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 3, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}],
    },
    "Blueprint_InfiniteBow": {
        "id": 0x008E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "InfiniteBow", "rarity": "Legendary",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 3, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}],
    },
    "Blueprint_PrisonerSkeleton": {
        "id": 0x008F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "PrisonerSkeleton", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 3, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}],
    },
    "Blueprint_Lightning": {
        "id": 0x0090, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Lightning",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Ossuary', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}],
    },
    "Blueprint_LeechBuff": {
        "id": 0x0091, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "LeechBuff", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Ossuary', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}],
    },
    "Blueprint_PrisonerMage": {
        "id": 0x0092, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "PrisonerMage", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonRoof', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Ossuary', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'AncientTemple', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Crypt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Tumulus', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}],
    },
    "Blueprint_Owl": {
        "id": 0x0093, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "Owl",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 1, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'PrisonDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Crypt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Castle', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Cliff', 'min_bc': 1, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'DookuCastle', 'min_bc': 1, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'DookuCastleHard', 'min_bc': 1, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}],
    },
    "Blueprint_PrisonerSonGoku": {
        "id": 0x0094, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "PrisonerSonGoku", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 3, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'PrisonDepths', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Crypt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Castle', 'min_bc': 3, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Cliff', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'DookuCastleHard', 'min_bc': 3, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}],
    },
    "Blueprint_P_Backpack_Ranged": {
        "id": 0x0095, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Backpack_Ranged",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'PrisonRoof', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'ClockTower', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}],
    },
    "Blueprint_PrisonerCrossbowMan": {
        "id": 0x0096, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "PrisonerCrossbowMan", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'PrisonRoof', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'ClockTower', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}],
    },
    "Blueprint_Rampart": {
        "id": 0x0097, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Rampart", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}],
    },
    "Blueprint_BloodShield": {
        "id": 0x0098, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BloodShield", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}],
    },
    "Blueprint_IceShield": {
        "id": 0x0099, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "IceShield",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}],
    },
    "Blueprint_PrisonerSand": {
        "id": 0x009A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 4, "item": "PrisonerSand", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 4, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'PrisonRoof', 'min_bc': 4, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'SewerDepths', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'Distillery', 'min_bc': 4, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}],
    },
    "Blueprint_P_Backpack_Melee": {
        "id": 0x009B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Backpack_Melee", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}],
    },
    "Blueprint_FireBomb": {
        "id": 0x009C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FireBomb",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'SewerShort', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 1, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}],
    },
    "Blueprint_MagnetGrenade": {
        "id": 0x009D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "MagnetGrenade", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'SewerShort', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 1, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}],
    },
    "Blueprint_BackStabber": {
        "id": 0x009E, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "BackStabber",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_P_AmmoOnHit": {
        "id": 0x009F, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_AmmoOnHit",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_DashShield": {
        "id": 0x00A0, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "DashShield",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_GroundSaw": {
        "id": 0x00A1, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "GroundSaw",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}],
    },
    "Blueprint_BumpBoots": {
        "id": 0x00A2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BumpBoots",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}],
    },
    "Blueprint_BackBlink": {
        "id": 0x00A3, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BackBlink", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}],
    },
    "Blueprint_DamageBuff": {
        "id": 0x00A4, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "DamageBuff", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'PrisonCorrupt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}],
    },
    "Blueprint_Decoy": {
        "id": 0x00A5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Decoy", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'PrisonCorrupt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}],
    },
    "Blueprint_PrisonerWarrior": {
        "id": 0x00A6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "PrisonerWarrior", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}],
    },
    "Blueprint_KnivesCircle": {
        "id": 0x00A7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "KnivesCircle", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 3, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}],
    },
    "Blueprint_OilSword": {
        "id": 0x00A8, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "OilSword",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 3, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}],
    },
    "Blueprint_Shockwave": {
        "id": 0x00A9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Shockwave", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Ossuary', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'AncientTemple', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Tumulus', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}],
    },
    "Blueprint_ExplosiveGrenade": {
        "id": 0x00AA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ExplosiveGrenade",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Ossuary', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'AncientTemple', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Tumulus', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}],
    },
    "Blueprint_PrisonerAphrodite": {
        "id": 0x00AB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "PrisonerAphrodite", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Ossuary', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'ClockTower', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Castle', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Shipwreck', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}],
    },
    "Blueprint_MultiCrossBow": {
        "id": 0x00AC, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "MultiCrossBow", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 2, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Swamp', 'min_bc': 1, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Ninja'}],
    },
    "Blueprint_MultiKickBoots": {
        "id": 0x00AD, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "MultiKickBoots",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 2, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'ClockTower', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Crypt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Swamp', 'min_bc': 1, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Ninja'}],
    },
    "Blueprint_PrisonerBlack": {
        "id": 0x00AE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "PrisonerBlack",  "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'ClockTower', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Crypt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Swamp', 'min_bc': 3, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'PurpleGarden', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Ninja'}],
    },
    "Blueprint_LowHealth": {
        "id": 0x00AF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "LowHealth", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}],
    },
    "Blueprint_PrisonerKamikaze": {
        "id": 0x00B0, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "PrisonerKamikaze",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}],
    },
    "Blueprint_PrisonerNeon": {
        "id": 0x00B1, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "PrisonerNeon", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerShort', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'PrisonDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'AncientTemple', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Cemetery', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Crypt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Distillery', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Shipwreck', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}],
    },
    "Blueprint_P_SpeedHeal": {
        "id": 0x00B2, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_SpeedHeal",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_P_SuperParry": {
        "id": 0x00B3, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_SuperParry",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_AdeleScythe": {
        "id": 0x00B4, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "AdeleScythe",
        "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Rapier": {
        "id": 0x00B5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Rapier", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Scorpio'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Scorpio'}],
    },
    "Blueprint_PrisonerSewers": {
        "id": 0x00B6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "PrisonerSewers", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Scorpio'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Scorpio'}],
    },
    "Blueprint_P_HealOnParry": {
        "id": 0x00B7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_HealOnParry",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}],
    },
    "Blueprint_SideBomb": {
        "id": 0x00B8, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SideBomb", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}],
    },
    "Blueprint_Whip": {
        "id": 0x00B9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Whip", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}],
    },
    "Blueprint_HoldShield": {
        "id": 0x00BA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HoldShield", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}],
    },
    "Blueprint_PrisonerStilt": {
        "id": 0x00BB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "PrisonerStilt", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'SewerDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'Cliff', 'min_bc': 1, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}],
    },
    "Blueprint_RevengeSword": {
        "id": 0x00BC, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "RevengeSword", "rarity": "Legendary",
        "sources": [{'biome': 'SewerShort', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Greenhouse', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}],
    },
    "Blueprint_P_ColdDmg": {
        "id": 0x00BD, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_ColdDmg",
        "sources": [{'biome': 'SewerShort', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Greenhouse', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}],
    },
    "Blueprint_FlameThrower": {
        "id": 0x00BE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FlameThrower",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'Swamp', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fogger'}],
    },
    "Blueprint_PrisonerGhost": {
        "id": 0x00BF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "PrisonerGhost", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'AncientTemple', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'Swamp', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fogger'}],
    },
    "Blueprint_Spear": {
        "id": 0x00C0, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Spear",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hammer'}, {'biome': 'Distillery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hammer'}],
    },
    "Blueprint_OilBomb": {
        "id": 0x00C1, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "OilBomb",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hammer'}, {'biome': 'Distillery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hammer'}],
    },
    "Blueprint_ClusterBomb": {
        "id": 0x00C2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ClusterBomb",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'PrisonRoof', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}],
    },
    "Blueprint_HeavyTurret": {
        "id": 0x00C3, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HeavyTurret", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'PrisonRoof', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}],
    },
    "Blueprint_PrisonerDemon": {
        "id": 0x00C4, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "PrisonerDemon", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'PrisonRoof', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cemetery', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Swamp', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cliff', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}],
    },
    "Blueprint_P_Execute_LowHealth": {
        "id": 0x00C5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Execute_LowHealth",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'PrisonRoof', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}],
    },
    "Blueprint_Crusher": {
        "id": 0x00C6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Crusher",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Cemetery', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}],
    },
    "Blueprint_P_Bleed": {
        "id": 0x00C7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Bleed", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Cemetery', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}],
    },
    "Blueprint_PrisonerCarduus": {
        "id": 0x00C8, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "PrisonerCarduus", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Cemetery', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Distillery', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}],
    },
    "Blueprint_P_DmgPlantedArrow": {
        "id": 0x00C9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgPlantedArrow",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Blobby'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Blobby'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Blobby'}],
    },
    "Blueprint_PerfectHalberd": {
        "id": 0x00CA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "PerfectHalberd", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Astrolab', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Cliff', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Stomper'}],
    },
    "Blueprint_P_DodgeSlow": {
        "id": 0x00CB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DodgeSlow",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Astrolab', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Cliff', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Stomper'}],
    },
    "Blueprint_FireTurret": {
        "id": 0x00CC, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FireTurret", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Tumulus', 'min_bc': 1, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Shocker'}],
    },
    "Blueprint_PrisonerCloud": {
        "id": 0x00CD, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "PrisonerCloud", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Crypt', 'min_bc': 3, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Shocker'}],
    },
    "Blueprint_Katana": {
        "id": 0x00CE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Katana",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'Crypt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}],
    },
    "Blueprint_PrisonerKillBill": {
        "id": 0x00CF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "PrisonerKillBill", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'Crypt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}],
    },
    "Blueprint_PreciseBow": {
        "id": 0x00D0, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "PreciseBow",
        "sources": [{'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_StunningGrenade": {
        "id": 0x00D1, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "StunningGrenade",
        "sources": [{'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Dash": {
        "id": 0x00D2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Dash",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_DmgSkl": {
        "id": 0x00D3, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgSkl",
        "sources": [{'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Minimoth'}],
    },
    "Blueprint_P_Hot": {
        "id": 0x00D4, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Hot",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_SeismicStomp": {
        "id": 0x00D5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SeismicStomp",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Burner": {
        "id": 0x00D6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Burner",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spawner'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spawner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Spawner'}],
    },
    "Blueprint_SpikedBoots": {
        "id": 0x00D7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SpikedBoots", "rarity": "Rare",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}],
    },
    "Blueprint_CeilTurret": {
        "id": 0x00D8, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "CeilTurret",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}],
    },
    "Blueprint_P_Backpack_Shield": {
        "id": 0x00D9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Backpack_Shield",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}],
    },
    "Blueprint_SismicBlade": {
        "id": 0x00DA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SismicBlade", "rarity": "Rare",
        "sources": [{'biome': 'Ossuary', 'min_bc': 2, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Astrolab', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Bomber'}],
    },
    "Blueprint_PrisonerAladdin": {
        "id": 0x00DB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "PrisonerAladdin", "rarity": "Rare",
        "sources": [{'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Astrolab', 'min_bc': 3, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Bomber'}],
    },
    "Blueprint_AlchemicGun": {
        "id": 0x00DC, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "AlchemicGun",
        "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_WarriorShield": {
        "id": 0x00DD, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "WarriorShield",
        "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_BleedCrit": {
        "id": 0x00DE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BleedCrit",
        "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spiker'}, {'biome': 'Greenhouse', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Spiker'}],
    },
    "Blueprint_Behemoth1": {
        "id": 0x00DF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "Behemoth1",
        "sources": [{'biome': 'Bridge', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Behemoth2": {
        "id": 0x00E0, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Behemoth2",
        "sources": [{'biome': 'Bridge', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Behemoth3": {
        "id": 0x00E1, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "Behemoth3",
        "sources": [{'biome': 'Bridge', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Behemoth4": {
        "id": 0x00E2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 4, "item": "Behemoth4",
        "sources": [{'biome': 'Bridge', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Beholder1": {
        "id": 0x00E3, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "Beholder1",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Beholder2": {
        "id": 0x00E4, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Beholder2",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Beholder3": {
        "id": 0x00E5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "Beholder3",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Beholder4": {
        "id": 0x00E6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 4, "item": "Beholder4",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_ParryShield": {
        "id": 0x00E7, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "ParryShield",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Item_SpawnLilStaphy": {
        "id": 0x00E8, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "SpawnLilStaphy",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_HookWhip": {
        "id": 0x00E9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HookWhip", "rarity": "Rare",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Shipwreck', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}],
    },
    "Blueprint_P_CDR_locked": {
        "id": 0x00EA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_CDR_locked",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Shipwreck', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}],
    },
    "Blueprint_Cannon": {
        "id": 0x00EB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "Cannon",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Shipwreck', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}],
    },
    "Blueprint_PortableDoor": {
        "id": 0x00EC, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "PortableDoor",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_P_Traps": {
        "id": 0x00ED, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Traps",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Item_SpawnCat": {
        "id": 0x00EE, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "Purple", "min_bc": 0, "item": "SpawnCat",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_Wings": {
        "id": 0x00EF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Wings",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Golem'}],
    },
    "Blueprint_FireBall": {
        "id": 0x00F0, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FireBall",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'OrbLauncher'}],
    },
    "Blueprint_P_DmgSkillRanged": {
        "id": 0x00F1, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgSkillRanged",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Duelist'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Duelist'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Duelist'}],
    },
    "Blueprint_BulletBlade": {
        "id": 0x00F2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BulletBlade", "rarity": "Rare",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Castle', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'DookuCastleHard', 'min_bc': 4, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Demon'}],
    },
    "Blueprint_PrisonerHyperlight": {
        "id": 0x00F3, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "PrisonerHyperlight", "rarity": "Rare",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Cavern', 'min_bc': 2, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Castle', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'DookuCastleHard', 'min_bc': 4, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Demon'}],
    },
    "Blueprint_P_DeathBomb": {
        "id": 0x00F4, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_DeathBomb",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Skul": {
        "id": 0x00F5, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Skul",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Hook": {
        "id": 0x00F6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Hook", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Tumulus', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}],
    },
    "Blueprint_BumpShield": {
        "id": 0x00F7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BumpShield", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Tumulus', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}],
    },
    "Blueprint_PrisonerSylvanian": {
        "id": 0x00F8, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 4, "item": "PrisonerSylvanian", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Tumulus', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Cliff', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Bank', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}],
    },
    "Blueprint_MarkBow": {
        "id": 0x00F9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "MarkBow",
        "sources": [{'biome': 'Cemetery', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}],
    },
    "Blueprint_PrisonerBison": {
        "id": 0x00FA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 4, "item": "PrisonerBison", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}, {'biome': 'ClockTower', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}, {'biome': 'Bank', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}],
    },
    "Blueprint_ToxicCloud": {
        "id": 0x00FB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ToxicCloud", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FlyZombie'}],
    },
    "Blueprint_Shovel": {
        "id": 0x00FC, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Shovel", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FlyZombie'}],
    },
    "Blueprint_P_ShareDamage": {
        "id": 0x00FD, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_ShareDamage",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FlyZombie'}],
    },
    "Blueprint_Tombstone": {
        "id": 0x00FE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Tombstone",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FlyZombie'}],
    },
    "Blueprint_P_InvisibilityOnKill": {
        "id": 0x00FF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_InvisibilityOnKill",
        "sources": [{'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'TimeKeeperBot'}],
    },
    "Item_BlobbyFlameGum": {
        "id": 0x0100, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlobbyFlameGum",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_P_DmgNearRanged": {
        "id": 0x0101, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgNearRanged",
        "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FatZombie'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FatZombie'}],
    },
    "Blueprint_SlowOrb": {
        "id": 0x0102, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SlowOrb",
        "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}],
    },
    "Blueprint_SpikeShield": {
        "id": 0x0103, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SpikeShield",
        "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}],
    },
    "Blueprint_Assassin1": {
        "id": 0x0104, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "Assassin1",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Assassin2": {
        "id": 0x0105, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Assassin2",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Assassin3": {
        "id": 0x0106, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "Assassin3",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Assassin4": {
        "id": 0x0107, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 4, "item": "Assassin4",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_ThrowingSpear": {
        "id": 0x0108, "region": "Checks", "type": "blueprint_floor",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "ThrowingSpear",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_floor'}],
    },
    "Blueprint_PrisonerSanta": {
        "id": 0x0109, "region": "Checks", "type": "blueprint_floor",
        "dlc": "RiseOfTheGiant", "min_bc": 4, "item": "PrisonerSanta",
        "sources": [{'biome': 'Cavern', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_floor'}],
    },
    "Blueprint_GodAxe": {
        "id": 0x010A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GodAxe",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Earthquaker'}],
    },
    "Blueprint_IceArmor": {
        "id": 0x010B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "IceArmor",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Earthquaker'}],
    },
    "Blueprint_Club": {
        "id": 0x010C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "Club",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Earthquaker'}],
    },
    "Blueprint_PrisonerXmas": {
        "id": 0x010D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "PrisonerXmas",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'StompSkeleton'}],
    },
    "Blueprint_MagicSalve": {
        "id": 0x010E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "MagicSalve", "rarity": "Rare",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Arbiter'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Arbiter'}],
    },
    "Blueprint_PrisonerShaman": {
        "id": 0x010F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 4, "item": "PrisonerShaman", "rarity": "Rare",
        "sources": [{'biome': 'Cavern', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Arbiter'}, {'biome': 'Bank', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Arbiter'}],
    },
    "Blueprint_Giant1": {
        "id": 0x0110, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 1, "item": "Giant1",
        "sources": [{'biome': 'Giant', 'min_bc': 1, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Giant2": {
        "id": 0x0111, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 2, "item": "Giant2",
        "sources": [{'biome': 'Giant', 'min_bc': 2, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Giant3": {
        "id": 0x0112, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 3, "item": "Giant3",
        "sources": [{'biome': 'Giant', 'min_bc': 3, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Giant4": {
        "id": 0x0113, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 4, "item": "Giant4",
        "sources": [{'biome': 'Giant', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_EasierCurse": {
        "id": 0x0114, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_EasierCurse",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_ShovelKnight": {
        "id": 0x0115, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "ShovelKnight",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_P_DmgFirstHit": {
        "id": 0x0116, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgFirstHit",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KingsFinger'}],
    },
    "Blueprint_Tornado": {
        "id": 0x0117, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Tornado", "rarity": "Rare",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}],
    },
    "Blueprint_P_ScaledHealth": {
        "id": 0x0118, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_ScaledHealth",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}],
    },
    "Blueprint_QuickFists": {
        "id": 0x0119, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "QuickFists", "rarity": "Rare",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Lancer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Lancer'}],
    },
    "Blueprint_P_Health": {
        "id": 0x011A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Health",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Lancer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Lancer'}],
    },
    "Blueprint_BarrelLauncher": {
        "id": 0x011B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BarrelLauncher", "rarity": "Rare",
        "sources": [{'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hurler'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hurler'}],
    },
    "Blueprint_TeslaCoil": {
        "id": 0x011C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "TeslaCoil",
        "sources": [{'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mimic'}],
    },
    "Blueprint_Hotk1": {
        "id": 0x011D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "Hotk1",
        "sources": [{'biome': 'Throne', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Hotk2": {
        "id": 0x011E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Hotk2",
        "sources": [{'biome': 'Throne', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Hotk3": {
        "id": 0x011F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "Hotk3",
        "sources": [{'biome': 'Throne', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Hotk4": {
        "id": 0x0120, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 4, "item": "Hotk4",
        "sources": [{'biome': 'Throne', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_SonicCrossbow": {
        "id": 0x0121, "region": "Checks", "type": "blueprint_floor",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "SonicCrossbow",
        "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_floor'}],
    },
    "Blueprint_BleedAxe": {
        "id": 0x0122, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "BleedAxe",
        "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'DeathMage'}],
    },
    "Blueprint_ThunderShield": {
        "id": 0x0123, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "ThunderShield",
        "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Defender'}],
    },
    "Item_KingDefault": {
        "id": 0x0124, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "KingDefault",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Item_KingWhite": {
        "id": 0x0125, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "KingWhite",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_PrisonerGardener": {
        "id": 0x0126, "region": "Checks", "type": "blueprint_floor",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "PrisonerGardener",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_floor'}],
    },
    "Blueprint_ParryBlade": {
        "id": 0x0127, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "ParryBlade", "rarity": "Rare",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Pitcher'}],
    },
    "Blueprint_PrisonerMushroom": {
        "id": 0x0128, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 3, "item": "PrisonerMushroom",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Pitcher'}],
    },
    "Blueprint_SpawnFriendlyHardy": {
        "id": 0x0129, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "SpawnFriendlyHardy",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'ThrowableMushroom'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'ThrowableMushroom'}],
    },
    "Blueprint_PrisonerFriendlyHardy": {
        "id": 0x012A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 1, "item": "PrisonerFriendlyHardy",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'ThrowableMushroom'}, {'biome': 'Cliff', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'ThrowableMushroom'}],
    },
    "Blueprint_SmokeBomb": {
        "id": 0x012B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "SmokeBomb", "rarity": "Rare",
        "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fugitive'}],
    },
    "Blueprint_PrisonerFugitive": {
        "id": 0x012C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 2, "item": "PrisonerFugitive",
        "sources": [{'biome': 'Swamp', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fugitive'}],
    },
    "Blueprint_Blowgun": {
        "id": 0x012D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "Blowgun",
        "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Blowgunner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Blowgunner'}],
    },
    "Blueprint_PrisonerBlowgunner": {
        "id": 0x012E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "PrisonerBlowgunner",
        "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Blowgunner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Blowgunner'}],
    },
    "Blueprint_TickSacrifice": {
        "id": 0x012F, "region": "Checks", "type": "blueprint_floor",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "TickSacrifice",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Tick1": {
        "id": 0x0130, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 1, "item": "Tick1",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Tick2": {
        "id": 0x0131, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 2, "item": "Tick2",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Tick3": {
        "id": 0x0132, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 3, "item": "Tick3",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Tick4": {
        "id": 0x0133, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 4, "item": "Tick4",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_PrisonerTick": {
        "id": 0x0134, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 4, "item": "PrisonerTick",
        "sources": [{'biome': 'Swamp', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Tick'}],
    },
    "Blueprint_FlyingSword": {
        "id": 0x0135, "region": "Checks", "type": "blueprint_floor",
        "dlc": "FatalFalls", "min_bc": 0, "item": "FlyingSword",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Cultist": {
        "id": 0x0136, "region": "Checks", "type": "blueprint_floor",
        "dlc": "FatalFalls", "min_bc": 0, "item": "Cultist",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_floor'}],
    },
    "Blueprint_SnakeFang": {
        "id": 0x0137, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "SnakeFang",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'JavelinSnake'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'JavelinSnake'}],
    },
    "Blueprint_PrisonerJavelinSnake": {
        "id": 0x0138, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "PrisonerJavelinSnake",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'JavelinSnake'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'JavelinSnake'}],
    },
    "Blueprint_Lantern": {
        "id": 0x0139, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "Lantern", "rarity": "Rare",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Necromant'}],
    },
    "Blueprint_PrisonerNecromant": {
        "id": 0x013A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "PrisonerNecromant",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Necromant'}],
    },
    "Blueprint_LightningRod": {
        "id": 0x013B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "LightningRod",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'BootlegHomunculus'}],
    },
    "Blueprint_PrisonerBootleg": {
        "id": 0x013C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "PrisonerBootleg",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'BootlegHomunculus'}],
    },
    "Blueprint_CupidityDagger": {
        "id": 0x013D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "CupidityDagger",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'U28_Steal'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'U28_Steal'}],
    },
    "Blueprint_GuillainThief": {
        "id": 0x013E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "GuillainThief",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'U28_Steal'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'U28_Steal'}],
    },
    "Blueprint_SnakeSwordWeapon": {
        "id": 0x013F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "SnakeSwordWeapon",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Harpy'}, {'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Harpy'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Harpy'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Harpy'}],
    },
    "Blueprint_BouncingStone": {
        "id": 0x0140, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "BouncingStone",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Buer'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Buer'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Buer'}],
    },
    "Blueprint_Gardener1": {
        "id": 0x0141, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 1, "item": "Gardener1",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 1, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Gardener2": {
        "id": 0x0142, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 2, "item": "Gardener2",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Gardener3": {
        "id": 0x0143, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 3, "item": "Gardener3",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Gardener4": {
        "id": 0x0144, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 4, "item": "Gardener4",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Item_Trident": {
        "id": 0x0145, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "Trident",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_Shark": {
        "id": 0x0146, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "Shark",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'AnchorGuy'}],
    },
    "Blueprint_ANCHORGUY": {
        "id": 0x0147, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ANCHORGUY", "rarity": "Rare",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'AnchorGuy'}],
    },
    "Blueprint_BlueErinaceus": {
        "id": 0x0148, "region": "Checks", "type": "blueprint_floor",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "BlueErinaceus",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Servante1": {
        "id": 0x0149, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 1, "item": "Servante1",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Servante2": {
        "id": 0x014A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 2, "item": "Servante2",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Servante3": {
        "id": 0x014B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 3, "item": "Servante3",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Servante4": {
        "id": 0x014C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 4, "item": "Servante4",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Queen1": {
        "id": 0x014D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 1, "item": "Queen1",
        "sources": [{'biome': 'QueenArena', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Queen2": {
        "id": 0x014E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 2, "item": "Queen2",
        "sources": [{'biome': 'QueenArena', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Queen3": {
        "id": 0x014F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 3, "item": "Queen3",
        "sources": [{'biome': 'QueenArena', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Queen4": {
        "id": 0x0150, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 4, "item": "Queen4",
        "sources": [{'biome': 'QueenArena', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Banker": {
        "id": 0x0151, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Banker",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_GoldDigger": {
        "id": 0x0152, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "GoldDigger",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'U28_VacuumCleaner'}],
    },
    "Blueprint_P_U28_PerkGoldPerDamage": {
        "id": 0x0153, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_U28_PerkGoldPerDamage",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'U28_VacuumCleaner'}],
    },
    "Blueprint_MoneyShooter": {
        "id": 0x0154, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "MoneyShooter",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'GoldenBatKamikaze'}],
    },
    "Item_AlucardShield": {
        "id": 0x0155, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "Purple", "min_bc": 0, "item": "AlucardShield",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_Bible": {
        "id": 0x0156, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "Bible",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'MiniWerewolf'}, {'biome': 'PurpleGarden', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'MiniWerewolf'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 0, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'MiniWerewolf'}, {'biome': 'DookuCastleHard', 'min_bc': 1, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}],
    },
    "Blueprint_Hector": {
        "id": 0x0157, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 1, "item": "Hector",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}, {'biome': 'DookuCastleHard', 'min_bc': 1, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}],
    },
    "Blueprint_HauntedArmor": {
        "id": 0x0158, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "HauntedArmor",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'LancerPurple'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'HauntedArmor'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'LancerPurple'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'HauntedArmor'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'LancerPurple'}],
    },
    "Blueprint_HolyWater": {
        "id": 0x0159, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "HolyWater",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Merman'}],
    },
    "Blueprint_BatVolley": {
        "id": 0x015A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "BatVolley",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'BatDasherPurple'}],
    },
    "Blueprint_Cross": {
        "id": 0x015B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "Cross",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'BoneThrower'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'BoneThrower'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'BoneThrower'}],
    },
    "Blueprint_Simon": {
        "id": 0x015C, "region": "Checks", "type": "blueprint_floor",
        "dlc": "Purple", "min_bc": 0, "item": "Simon",
        "sources": [{'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Blueprint_ThrowingAxe": {
        "id": 0x015D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "ThrowingAxe",
        "sources": [{'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'HauntedArmor'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'HauntedArmor'}],
    },
    "Blueprint_RichterROB": {
        "id": 0x015E, "region": "Checks", "type": "blueprint_floor",
        "dlc": "Purple", "min_bc": 0, "item": "RichterROB",
        "sources": [{'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Adele1": {
        "id": 0x015F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 1, "item": "Adele1",
        "sources": [{'biome': 'DeathArena', 'min_bc': 1, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Adele2": {
        "id": 0x0160, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 2, "item": "Adele2",
        "sources": [{'biome': 'DeathArena', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Adele3": {
        "id": 0x0161, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 3, "item": "Adele3",
        "sources": [{'biome': 'DeathArena', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Adele4": {
        "id": 0x0162, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 4, "item": "Adele4",
        "sources": [{'biome': 'DeathArena', 'min_bc': 4, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Alucard": {
        "id": 0x0163, "region": "Checks", "type": "blueprint_floor",
        "dlc": "Purple", "min_bc": 0, "item": "Alucard",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Sypha": {
        "id": 0x0164, "region": "Checks", "type": "blueprint_floor",
        "dlc": "Purple", "min_bc": 0, "item": "Sypha",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Trevor": {
        "id": 0x0165, "region": "Checks", "type": "blueprint_floor",
        "dlc": "Purple", "min_bc": 0, "item": "Trevor",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Dooku1": {
        "id": 0x0166, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 1, "item": "Dooku1",
        "sources": [{'biome': 'DookuArena', 'min_bc': 1, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Dooku2": {
        "id": 0x0167, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 2, "item": "Dooku2",
        "sources": [{'biome': 'DookuArena', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Dooku3": {
        "id": 0x0168, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 3, "item": "Dooku3",
        "sources": [{'biome': 'DookuArena', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_Dooku4": {
        "id": 0x0169, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 4, "item": "Dooku4",
        "sources": [{'biome': 'DookuArena', 'min_bc': 4, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_Caltrops": {
        "id": 0x016A, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Caltrops",
        "sources": [{'biome': 'Challenge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_LighthouseKey": {
        "id": 0x016B, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "LighthouseKey",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_CollectorSpin": {
        "id": 0x016C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "CollectorSpin",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_BloodDrinker": {
        "id": 0x016D, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_BloodDrinker",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_Stomper": {
        "id": 0x016E, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Stomper",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_Berzerker": {
        "id": 0x016F, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Berzerker",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_GottaGoFast": {
        "id": 0x0170, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_GottaGoFast",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_Tinker": {
        "id": 0x0171, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Tinker",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_Menagerie": {
        "id": 0x0172, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Menagerie",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_Grenadier": {
        "id": 0x0173, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Grenadier",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_Superconductor": {
        "id": 0x0174, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Superconductor",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_Assassin": {
        "id": 0x0175, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Assassin",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_ASP_Damned": {
        "id": 0x0176, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Damned",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "BSC_BossRune1": {"id": 0x0177, "region": "Throne", "type": "rune", "dlc": "", "min_bc": 0, "item": "BossRune1"},
    "BSC_BossRune2": {"id": 0x0178, "region": "Throne", "type": "rune", "dlc": "", "min_bc": 1, "item": "BossRune2"},
    "BSC_BossRune3": {"id": 0x0179, "region": "Throne", "type": "rune", "dlc": "", "min_bc": 2, "item": "BossRune3"},
    "BSC_BossRune4": {"id": 0x017A, "region": "Throne", "type": "rune", "dlc": "", "min_bc": 3, "item": "BossRune4"},
    "BSC_BossRune5": {"id": 0x017B, "region": "Giant", "type": "rune", "dlc": "RiseOfTheGiant", "min_bc": 4, "item": "BossRune5"},
    "Item_KingsSpear": {
        "id": 0x017C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "KingsSpear",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_EvilEmpire": {
        "id": 0x017D, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "EvilEmpire",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_RhythmicBlade": {
        "id": 0x017E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "RhythmicBlade", "rarity": "Rare",
        "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Tick'}],
    },
    "Rune_ScoringKey": {
        "id": 0x017F, "region": "Checks", "type": "rune",
        "dlc": "", "min_bc": 0, "item": "ScoringKey",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'rune'}],
    },
    "Blueprint_BehemothHammer": {
        "id": 0x0180, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BehemothHammer",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_CrossBow": {
        "id": 0x0181, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "CrossBow",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_ImpaleSpear": {
        "id": 0x0182, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ImpaleSpear",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_ManyMobsAround": {
        "id": 0x0183, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_ManyMobsAround",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_Ammo": {
        "id": 0x0184, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Ammo",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_Curse": {
        "id": 0x0185, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Curse",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_BehemothDefault": {
        "id": 0x0186, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BehemothDefault",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessBehemoth": {
        "id": 0x0187, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FlawlessBehemoth",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Item_ConciergeFlame": {
        "id": 0x0188, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ConciergeFlame",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_TentacleWhip": {
        "id": 0x0189, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "TentacleWhip",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_EvilSword": {
        "id": 0x018A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "EvilSword",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_Food": {
        "id": 0x018B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Food",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_Rally": {
        "id": 0x018C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Rally",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_ForgeRefine1": {
        "id": 0x018D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ForgeRefine1",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_BeholderDefault": {
        "id": 0x018E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BeholderDefault",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessBeholder": {
        "id": 0x018F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FlawlessBeholder",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Item_ConjunctiviusHead": {
        "id": 0x0190, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ConjunctiviusHead",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_TickScytheLeft": {
        "id": 0x0191, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "TickScytheLeft",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_TickDefault": {
        "id": 0x0192, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "TickDefault",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessTick": {
        "id": 0x0193, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "FlawlessTick",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Item_MamaTickEye": {
        "id": 0x0194, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "MamaTickEye",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_ThrowingIce": {
        "id": 0x0195, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ThrowingIce",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FrostCrossBow": {
        "id": 0x0196, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FrostCrossBow",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_SpeedBuff": {
        "id": 0x0197, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_SpeedBuff",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_CorruptedHealing": {
        "id": 0x0198, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_CorruptedHealing",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_P_QuickHeal": {
        "id": 0x0199, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_QuickHeal",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_AssassinDefault": {
        "id": 0x019A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "AssassinDefault",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessAssassin": {
        "id": 0x019B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FlawlessAssassin",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Item_TimeKeeperHat": {
        "id": 0x019C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "TimeKeeperHat",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_GiantKiller": {
        "id": 0x019D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GiantKiller",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_GiantWhistle": {
        "id": 0x019E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GiantWhistle",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_GiantDefault": {
        "id": 0x019F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GiantDefault",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessGiant": {
        "id": 0x0200, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "FlawlessGiant",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Item_GiantFlame": {
        "id": 0x0201, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GiantFlame",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_GardenerSickles": {
        "id": 0x0202, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "GardenerSickles",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_GardenerDefault": {
        "id": 0x0203, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "GardenerDefault",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessGardener": {
        "id": 0x0204, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "FlawlessGardener",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Item_ScarecrowHat": {
        "id": 0x0205, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "FatalFalls", "min_bc": 0, "item": "ScarecrowHat",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_ArmoryUnlock": {
        "id": 0x0206, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ArmoryUnlock",
        "sources": [{'biome': 'Throne', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_HotkDefault": {
        "id": 0x0207, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HotkDefault",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessHotk": {
        "id": 0x0208, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FlawlessHotk",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Item_HandOfTheKingFlame": {
        "id": 0x0209, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "HandOfTheKingFlame",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_HeavyBow": {
        "id": 0x020A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "HeavyBow",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_ElbowBlades": {
        "id": 0x020B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ElbowBlades",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_WreckingBall": {
        "id": 0x020C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "WreckingBall",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_ServanteDefault": {
        "id": 0x020D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ServanteDefault",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessServante": {
        "id": 0x020E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "FlawlessServante",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Item_ServantsMask": {
        "id": 0x020F, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ServantsMask",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_QueenRapier": {
        "id": 0x0210, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "QueenRapier",
        "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_QueenDefault": {
        "id": 0x0211, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "QueenDefault",
        "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessQueen": {
        "id": 0x0212, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "FlawlessQueen",
        "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Item_QueenFlame": {
        "id": 0x0213, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "QueenFlame",
        "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_CollectorDefault": {
        "id": 0x0214, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "CollectorDefault",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Item_CollectorHood": {
        "id": 0x0215, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "CollectorHood",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_AdeleDefault": {
        "id": 0x0216, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "AdeleDefault",
        "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessAdele": {
        "id": 0x0217, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "FlawlessAdele",
        "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_VampireKiller": {
        "id": 0x0218, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "VampireKiller",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_DookuDefault": {
        "id": 0x0219, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "DookuDefault",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessDooku": {
        "id": 0x021A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "FlawlessDooku",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_FlawlessDooku": {
        "id": 0x021A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "FlawlessDooku",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Blueprint_RootBomb": {
        "id": 0x021B, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "RootBomb",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_BubbleShieldPower": {
        "id": 0x021C, "region": "Checks", "type": "blueprint_floor",
        "dlc": "FatalFalls", "min_bc": 0, "item": "BubbleShieldPower",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_floor'}],
    },
    "Blueprint_BroadSword": {
        "id": 0x021D, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "BroadSword",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Pan": {
        "id": 0x021E, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Pan",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_LongBow": {
        "id": 0x021F, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "LongBow",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_ExplosiveCrossBow": {
        "id": 0x0220, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "ExplosiveCrossBow",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Boomerang": {
        "id": 0x0221, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Boomerang",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Item_WiggleWhip": {
        "id": 0x0222, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "Purple", "min_bc": 0, "item": "WiggleWhip",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_AreaShield": { 
        "id": 0x0223, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "AreaShield",
        "sources": [{'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_PrisonerGold": { 
        "id": 0x0224, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "PrisonerGold",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_Indulgence": { 
        "id": 0x0225, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Indulgence",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SoreLooser'}],
    },
    "Blueprint_P_DamnedVigor": { 
        "id": 0x0226, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "P_DamnedVigor",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SoreLooser'}],
    },
    "Blueprint_Misericord": { 
        "id": 0x0227, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Misericord",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'DoomBringer'}],
    },
    "Blueprint_P_DemonicForce": { 
        "id": 0x0228, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "P_DemonicForce",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'DoomBringer'}],
    },
    "Blueprint_Anathema": { 
        "id": 0x0229, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Anathema",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Curser'}],
    },
    "Blueprint_P_CursedFlask": { 
        "id": 0x022A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "P_CursedFlask",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Curser'}],
    },
    "Blueprint_GiantStaff": {
        "id": 0x022B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "GiantStaff",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'AxeStatue'}],
    },
    "Blueprint_Statue": {
        "id": 0x022C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "Statue",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'AxeStatue'}],
    },
    "Blueprint_MedusaHead": {
        "id": 0x022D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "MedusaHead",
        "sources": [{'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Medusa'}],
    },
    "Blueprint_P_U28_PerkGoldShield": {
        "id": 0x022E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_U28_PerkGoldShield",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ShopMimic'}],
    },
    "Blueprint_P_U28_PerkGoldSpeed": {
        "id": 0x022F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_U28_PerkGoldSpeed",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ShopMimic'}],
    },
    "Blueprint_HandHook": {
        "id": 0x0230, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "HandHook",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BoilerRoom'}],
    },
    "Blueprint_ThrowingCards": {
        "id": 0x0231, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ThrowingCards",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BoilerRoom'}],
    },
    "Blueprint_Staphy": {
        "id": 0x0232, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "Staphy", "rarity": "Rare",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BoilerRoom'}],
    },
    "Rune_HomKey": {"id": 0x0233, "region": "Throne", "type": "rune", "dlc": "", "item": "HomKey"},
    "Item_Maria": {
        "id": 0x0234, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "Purple", "min_bc": 0, "item": "Maria",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Item_RiskOfRain": {
        "id": 0x0235, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "RiskOfRain",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_SlayTheSpire": {
        "id": 0x0236, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "SlayTheSpire",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BobbyFlame": {
        "id": 0x0237, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BobbyFlame",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlackHole": {
        "id": 0x0238, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlackHole",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlackHoleWhite": {
        "id": 0x0239, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 2, "item": "BlackHoleWhite",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlackHoleRed": {
        "id": 0x023A, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlackHoleRed",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlackHoleBlue": {
        "id": 0x023B, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlackHoleBlue",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlackHoleGreen": {
        "id": 0x023C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlackHoleGreen",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_Bitter": {
        "id": 0x023D, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Bitter",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_VortexBadSeed": {
        "id": 0x023E, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "VortexBadSeed",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_VortexAndSea": {
        "id": 0x023F, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "VortexAndSea",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_VortexFoundry": {
        "id": 0x0240, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "VortexFoundry",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_Guillain": {
        "id": 0x0241, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Guillain",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_Pecheur": {
        "id": 0x0242, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Pecheur",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_StaphyHead": {
        "id": 0x0243, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "StaphyHead",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Item_Flawless": { #todo might need DLCs
        "id": 0x0244, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Flawless",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_CellHead": {
        "id": 0x0245, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "CellHead",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlobbyFlame": {
        "id": 0x0246, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlobbyFlame",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_GlitchyHead": {
        "id": 0x0247, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "GlitchyHead",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Item_MushroomBoi": {
        "id": 0x0248, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "MushroomBoi",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'item_no_blueprint'}],
    },
    "Item_HordesZeroHood": {
        "id": 0x0249, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "HordesZeroHood",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlobbyFlameMagma": {
        "id": 0x024A, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "BlobbyFlameMagma",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Item_BlobbyFlameMalaise": {
        "id": 0x024B, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlobbyFlameMalaise",
        "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_GlitchyHeadDeepSpace": {
        "id": 0x024C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "GlitchyHeadDeepSpace",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_GlitchyHeadRed": {
        "id": 0x024D, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "GlitchyHeadRed",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlowTorchBlack": {
        "id": 0x024E, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlowTorchBlack",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}, {'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'item_no_blueprint'}, {'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Item_BlowTorchGold": {
        "id": 0x024F, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlowTorchGold",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Item_BlowTorchRed": {
        "id": 0x0250, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BlowTorchRed",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}, {'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'item_no_blueprint'}, {'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Item_BossCellHead": {
        "id": 0x0251, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 5, "item": "BossCellHead",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 5, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blueprint_Money5": {
        "id": 0x0252, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Money5",
        "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Blueprint_ShopCategories": {
        "id": 0x0253, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "ShopCategories",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
}

def location_id(name: str) -> int:
    return BASE_ID + LOCATION_TABLE[name]["id"]

def get_locations_for_dlcs(enabled_dlcs: Set[str]) -> Dict[str, dict]:
    return {n: d for n, d in LOCATION_TABLE.items() if d["dlc"] == "" or d["dlc"] in enabled_dlcs}

def get_locations_for_bc(enabled_dlcs: Set[str], bc_level: int) -> Dict[str, dict]:
    result = {}
    for name, data in get_locations_for_dlcs(enabled_dlcs).items():
        if "sources" in data:
            if any((s["dlc"]=="" or s["dlc"] in enabled_dlcs) and s["min_bc"]<=bc_level<=s["max_bc"] for s in data["sources"]):
                result[name] = data
        else:
            # Check optional min_bc on non-grouped locations (e.g. BC-gated biomes)
            if data.get("min_bc", 0) <= bc_level:
                result[name] = data
    return result

def _assert_no_duplicate_ids() -> None:
    seen: Dict[int, str] = {}
    for name, data in LOCATION_TABLE.items():
        oid = data["id"]
        if oid in seen: raise ValueError(f"Duplicate ID 0x{oid:04X}: '{seen[oid]}' and '{name}'")
        seen[oid] = name
_assert_no_duplicate_ids()
