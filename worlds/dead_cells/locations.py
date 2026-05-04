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
    HEAD                 = "head"
    SKIN                 = "skin"

LOCATION_TABLE: Dict[str, dict] = {
    "Prisoners' Quarters Enter": {"id": 0x0000, "region": "PrisonStart", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Prisoners' Quarters Exit": {"id": 0x0001, "region": "PrisonStart", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Promenade of the Condemned Enter": {"id": 0x0002, "region": "PrisonCourtyard", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Promenade of the Condemned Exit": {"id": 0x0003, "region": "PrisonCourtyard", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Toxic Sewers Enter": {"id": 0x0004, "region": "SewerShort", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Toxic Sewers Exit": {"id": 0x0005, "region": "SewerShort", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Prison Depths Enter": {"id": 0x0006, "region": "PrisonDepths", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Prison Depths Exit": {"id": 0x0007, "region": "PrisonDepths", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Corrupted Prison Enter": {"id": 0x0008, "region": "PrisonCorrupt", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Corrupted Prison Exit": {"id": 0x0009, "region": "PrisonCorrupt", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Ramparts Enter": {"id": 0x000A, "region": "PrisonRoof", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Ramparts Exit": {"id": 0x000B, "region": "PrisonRoof", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Ossuary Enter": {"id": 0x000C, "region": "Ossuary", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Ossuary Exit": {"id": 0x000D, "region": "Ossuary", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Ancient Sewers Enter": {"id": 0x000E, "region": "SewerDepths", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Ancient Sewers Exit": {"id": 0x000F, "region": "SewerDepths", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Black Bridge Enter": {"id": 0x0010, "region": "Bridge", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Black Bridge Exit": {"id": 0x0011, "region": "Bridge", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Insufferable Crypt Enter": {"id": 0x0012, "region": "BeholderPit", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Insufferable Crypt Exit": {"id": 0x0013, "region": "BeholderPit", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Stilt Village Enter": {"id": 0x0014, "region": "StiltVillage", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Stilt Village Exit": {"id": 0x0015, "region": "StiltVillage", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Slumbering Sanctuary Enter": {"id": 0x0016, "region": "AncientTemple", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Slumbering Sanctuary Exit": {"id": 0x0017, "region": "AncientTemple", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Graveyard Enter": {"id": 0x0018, "region": "Cemetery", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Graveyard Exit": {"id": 0x0019, "region": "Cemetery", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Clock Tower Enter": {"id": 0x001A, "region": "ClockTower", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Clock Tower Exit": {"id": 0x001B, "region": "ClockTower", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Forgotten Sepulcher Enter": {"id": 0x001C, "region": "Crypt", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Forgotten Sepulcher Exit": {"id": 0x001D, "region": "Crypt", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Clock Room Enter": {"id": 0x001E, "region": "TopClockTower", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Clock Room Exit": {"id": 0x001F, "region": "TopClockTower", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Cavern Enter": {"id": 0x0020, "region": "Cavern", "type": "biome_enter", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'biome_enter'}],},
    "Cavern Exit": {"id": 0x0021, "region": "Cavern", "type": "biome_exit", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'biome_exit'}],},
    "Guardian's Haven Enter": {"id": 0x0022, "region": "Giant", "type": "biome_enter", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'biome_enter'}],},
    "Guardian's Haven Exit": {"id": 0x0023, "region": "Giant", "type": "biome_exit", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'biome_exit'}],},
    "High Peak Castle Enter": {"id": 0x0024, "region": "Castle", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "High Peak Castle Exit": {"id": 0x0025, "region": "Castle", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Derelict Distillery Enter": {"id": 0x0026, "region": "Distillery", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Derelict Distillery Exit": {"id": 0x0027, "region": "Distillery", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Throne Room Enter": {"id": 0x0028, "region": "Throne", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Throne Room Exit": {"id": 0x0029, "region": "Throne", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Astrolab Enter": {"id": 0x002A, "region": "Astrolab", "type": "biome_enter", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'biome_enter'}],},
    "Astrolab Exit": {"id": 0x002B, "region": "Astrolab", "type": "biome_exit", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'biome_exit'}],},
    "Observatory Enter": {"id": 0x002C, "region": "Observatory", "type": "biome_enter", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'biome_enter'}],},
    "Observatory Exit": {"id": 0x002D, "region": "Observatory", "type": "biome_exit", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'biome_exit'}],},
    "Dilapidated Arboretum Enter": {"id": 0x002E, "region": "Greenhouse", "type": "biome_enter", "dlc": "TheBadSeed", "item": None, "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'biome_enter'}],},
    "Dilapidated Arboretum Exit": {"id": 0x002F, "region": "Greenhouse", "type": "biome_exit", "dlc": "TheBadSeed", "item": None, "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'biome_exit'}],},
    "Morass of the Banished Enter": {"id": 0x0030, "region": "Swamp", "type": "biome_enter", "dlc": "TheBadSeed", "item": None, "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'biome_enter'}],},
    "Morass of the Banished Exit": {"id": 0x0031, "region": "Swamp", "type": "biome_exit", "dlc": "TheBadSeed", "item": None, "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'biome_exit'}],},
    "Nest Enter": {"id": 0x0032, "region": "SwampHeart", "type": "biome_enter", "dlc": "TheBadSeed", "item": None, "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'biome_enter'}],},
    "Nest Exit": {"id": 0x0033, "region": "SwampHeart", "type": "biome_exit", "dlc": "TheBadSeed", "item": None, "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'biome_exit'}],},
    "Fractured Shrines Enter": {"id": 0x0034, "region": "Tumulus", "type": "biome_enter", "dlc": "FatalFalls", "item": None, "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'biome_enter'}],},
    "Fractured Shrines Exit": {"id": 0x0035, "region": "Tumulus", "type": "biome_exit", "dlc": "FatalFalls", "item": None, "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'biome_exit'}],},
    "Undying Shores Enter": {"id": 0x0036, "region": "Cliff", "type": "biome_enter", "dlc": "FatalFalls", "item": None, "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'biome_enter'}],},
    "Undying Shores Exit": {"id": 0x0037, "region": "Cliff", "type": "biome_exit", "dlc": "FatalFalls", "item": None, "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'biome_exit'}],},
    "Mausoleum Enter": {"id": 0x0038, "region": "GardenerStage", "type": "biome_enter", "dlc": "FatalFalls", "item": None, "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'biome_enter'}],},
    "Mausoleum Exit": {"id": 0x0039, "region": "GardenerStage", "type": "biome_exit", "dlc": "FatalFalls", "item": None, "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'biome_exit'}],},
    "Infested Shipwreck Enter": {"id": 0x003A, "region": "Shipwreck", "type": "biome_enter", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'biome_enter'}],},
    "Infested Shipwreck Exit": {"id": 0x003B, "region": "Shipwreck", "type": "biome_exit", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'biome_exit'}],},
    "Lighthouse Enter": {"id": 0x003C, "region": "Lighthouse", "type": "biome_enter", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'biome_enter'}],},
    "Lighthouse Exit": {"id": 0x003D, "region": "Lighthouse", "type": "biome_exit", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'biome_exit'}],},
    "Crown Enter": {"id": 0x003E, "region": "QueenArena", "type": "biome_enter", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'biome_enter'}],},
    "Crown Exit": {"id": 0x003F, "region": "QueenArena", "type": "biome_exit", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'biome_exit'}],},
    "Bank Enter": {"id": 0x0040, "region": "Bank", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Bank Exit": {"id": 0x0041, "region": "Bank", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Castle Outskirts Enter": {"id": 0x0042, "region": "PurpleGarden", "type": "biome_enter", "dlc": "Purple", "item": None, "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_enter'}],},
    "Castle Outskirts Exit": {"id": 0x0043, "region": "PurpleGarden", "type": "biome_exit", "dlc": "Purple", "item": None, "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_exit'}],},
    "Dracula's Castle Enter": {"id": 0x0044, "region": "DookuCastle", "type": "biome_enter", "dlc": "Purple", "item": None, "sources": [{'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_enter'}],},
    "Dracula's Castle Exit": {"id": 0x0045, "region": "DookuCastle", "type": "biome_exit", "dlc": "Purple", "item": None, "sources": [{'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_exit'}],},
    "2nd Dracula's Castle Enter": {"id": 0x0046, "region": "DookuCastleHard", "type": "biome_enter", "dlc": "Purple", "item": None, "sources": [{'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_enter'}],},
    "2nd Dracula's Castle Exit": {"id": 0x0047, "region": "DookuCastleHard", "type": "biome_exit", "dlc": "Purple", "item": None, "sources": [{'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_exit'}],},
    "Defiled Necropolis Enter": {"id": 0x0048, "region": "DeathArena", "type": "biome_enter", "dlc": "Purple", "item": None, "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_enter'}],},
    "Defiled Necropolis Exit": {"id": 0x0049, "region": "DeathArena", "type": "biome_exit", "dlc": "Purple", "item": None, "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_exit'}],},
    "Master's Keep Enter": {"id": 0x004A, "region": "DookuArena", "type": "biome_enter", "dlc": "Purple", "item": None, "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_enter'}],},
    "Master's Keep Exit": {"id": 0x004B, "region": "DookuArena", "type": "biome_exit", "dlc": "Purple", "item": None, "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'biome_exit'}],},
    "Challenge Enter": {"id": 0x004C, "region": "Challenge", "type": "biome_enter", "dlc": "", "item": None, "sources": [{'biome': 'Challenge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_enter'}],},
    "Challenge Exit": {"id": 0x004D, "region": "Challenge", "type": "biome_exit", "dlc": "", "item": None, "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'biome_exit'}],},
    "Vine Rune": {"id": 0x004E, "region": "PrisonCourtyard", "type": "rune", "dlc": "", "item": "LadderKey", "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'rune'}],},
    "Teleportation Rune": {"id": 0x004F, "region": "SewerShort", "type": "rune", "dlc": "", "item": "TeleportKey", "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'rune'}],},
    "Customization Rune": {"id": 0x0050, "region": "PrisonRoof", "type": "rune", "dlc": "", "item": "CustomKey", "sources": [{'biome': 'Roof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'rune'}],},
    "Ram Rune": {"id": 0x0051, "region": "Ossuary", "type": "rune", "dlc": "", "item": "BreakableGroundKey", "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'rune'}],},
    "Spider Rune": {"id": 0x0052, "region": "AncientTemple", "type": "rune", "dlc": "", "item": "WallJumpKey", "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'rune'}],},
    "Explorer's Rune": {"id": 0x0053, "region": "Crypt", "type": "rune", "dlc": "", "item": "ExploKey", "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'rune'}],},
    "The Concierge": {"id": 0x0054, "region": "Bridge", "type": "boss", "dlc": "", "item": None, "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'boss'}],},
    "Conjunctivius": {"id": 0x0055, "region": "BeholderPit", "type": "boss", "dlc": "", "item": None, "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'boss'}],},
    "The Time Keeper": {"id": 0x0056, "region": "TopClockTower", "type": "boss", "dlc": "", "item": None, "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'boss'}],},
    "The Giant": {"id": 0x0057, "region": "Giant", "type": "boss", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'boss'}],},
    "The Hand of the King": {"id": 0x0058, "region": "Throne", "type": "boss", "dlc": "", "item": None, "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'boss'}],},
    "The Collector": {"id": 0x0059, "region": "Observatory", "type": "boss", "dlc": "RiseOfTheGiant", "item": None, "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'boss'}],},
    "Mama Tick": {"id": 0x005A, "region": "SwampHeart", "type": "boss", "dlc": "TheBadSeed", "item": None, "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'boss'}],},
    "Scarecrow": {"id": 0x005B, "region": "GardenerStage", "type": "boss", "dlc": "FatalFalls", "item": None, "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'boss'}],},
    "Calliope": {"id": 0x005C, "region": "Lighthouse", "type": "boss", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'boss'}],},
    "Euterpe": {"id": 0x005D, "region": "Lighthouse", "type": "boss", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'boss'}],},
    "Kleio": {"id": 0x005E, "region": "Lighthouse", "type": "boss", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'boss'}],},
    "The Queen": {"id": 0x005F, "region": "QueenArena", "type": "boss", "dlc": "TheQueenAndTheSea", "item": None, "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'boss'}],},
    "Death": {"id": 0x0060, "region": "DeathArena", "type": "boss", "dlc": "Purple", "item": None, "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'boss'}],},
    "Dracula": {"id": 0x0061, "region": "DookuArena", "type": "boss", "dlc": "Purple", "item": None, "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'boss'}],},
    "Quick Bow": {
        "id": 0x0062, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "FastBow",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Magic Bow": {
        "id": 0x0063, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "MagicBow",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Disengagement": {
        "id": 0x0064, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Disengage",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Wish": {
        "id": 0x0065, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Wishes",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Royal Gardener Outfit": {
        "id": 0x0066, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "RoyalGardener",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_floor'}],
    },
    "Gordon Freeman Outfit": {
        "id": 0x0067, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "FreemanSkin",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Soul Knight Outfit": {
        "id": 0x0068, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "SoulKnight",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Familiar Outfit": {
        "id": 0x0069, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "Terraria",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Bobby Outfit (Lore Room)": {
        "id": 0x006A, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "Bobby",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Crowbar": {
        "id": 0x006B, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Crowbar",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Machete and Pistol": {
        "id": 0x006C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "MachetePistol",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Hard Light Sword": {
        "id": 0x006D, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "HardLightSword",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Pure Nail": {
        "id": 0x006E, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "PureNail",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Bone": {
        "id": 0x006F, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "SkulBone",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Panchaku": {
        "id": 0x0070, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "NunchuckPan",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Baseball Bat": {
        "id": 0x0071, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "BaseballBat",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "King Scepter": {
        "id": 0x0072, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "KingScepter",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Starfury": {
        "id": 0x0073, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Starfury",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Throwable Objects": {
        "id": 0x0074, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ThrowableStuff",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Laser Glaive": {
        "id": 0x0075, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "LaserGlaive",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Diverse Deck": {
        "id": 0x0076, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "DiverseDeckJuggernaut",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Face Flask": {
        "id": 0x0077, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "FaceFlask",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Pollo Power": {
        "id": 0x0078, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "PolloPower",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Swift Sword": {
        "id": 0x0079, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "SpeedBlade",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Lacerating Aura": {
        "id": 0x007A, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "DamageAura",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Meat Skewer": {
        "id": 0x007B, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "DashSword",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Hollow Knight Outfit": {
        "id": 0x007C, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "HollowKnight",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blasphemous Outfit": {
        "id": 0x007D, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "Blasphemous",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Guacamelee Outfit": {
        "id": 0x007E, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "Guacamelee",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "The Magician's Outfit": {
        "id": 0x007F, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "HyperLightDrifter",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Curse of the Dead Gods Outfit": {
        "id": 0x0080, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "CurseofTheDeadGods",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Hotline Miami Outfit": {
        "id": 0x0081, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "HotlineMiamiChicken",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Katana ZERO Outfit": {
        "id": 0x0082, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "KatanaZero",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Sewing Scissors": {
        "id": 0x0083, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Scissor",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Giant Comb": {
        "id": 0x0084, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Comb",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 5, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Berserker": {
        "id": 0x0085, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DeathShield", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'PrisonCourtyard', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'SewerDepths', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'StiltVillage', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Crypt', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Cavern', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Distillery', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Cliff', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}, {'biome': 'Bank', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AggressiveZombie'}],
    },
    "Adrenaline": {
        "id": 0x0086, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 3, "item": "P_DodgeHeal",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'SewerShort', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'PrisonDepths', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'PrisonRoof', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'StiltVillage', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Castle', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Greenhouse', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Swamp', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Cliff', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Rampager'}, {'biome': 'Shipwreck', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'Rampager'}],
    },
    "Double Crossb-o-matic": {
        "id": 0x0087, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HorizontalTurret", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 1, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Zombie'}],
    },
    "Blood Sword": {
        "id": 0x0088, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Bleeder",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 1, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Zombie'}],
    },
    "Bobby Outfit (Zombie)": {
        "id": 0x0089, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "PrisonerBobby", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCourtyard', 'min_bc': 1, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerShort', 'min_bc': 1, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonDepths', 'min_bc': 1, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonCorrupt', 'min_bc': 1, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PrisonRoof', 'min_bc': 1, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Ossuary', 'min_bc': 1, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'SewerDepths', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'AncientTemple', 'min_bc': 1, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Greenhouse', 'min_bc': 1, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Tumulus', 'min_bc': 1, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Zombie'}, {'biome': 'PurpleGarden', 'min_bc': 1, 'max_bc': 1, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Zombie'}],
    },
    "Kill Rhythm": {
        "id": 0x008A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "P_AttackSpeed_Combo", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'PrisonRoof', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'ClockTower', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Cavern', 'min_bc': 2, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Distillery', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}],
    },
    "Oven Axe": {
        "id": 0x008B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "HeavyAxe",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'PrisonRoof', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'ClockTower', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Cavern', 'min_bc': 2, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Distillery', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Enforcer'}],
    },
    "Infantry Bow": {
        "id": 0x008C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "CloseCombatBow",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 3, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}],
    },
    "Ice Bow": {
        "id": 0x008D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FrostBow", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 3, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}],
    },
    "Bow and Endless Quiver": {
        "id": 0x008E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "InfiniteBow", "rarity": "Legendary",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 3, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}],
    },
    "Skeleton Outfit": {
        "id": 0x008F, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "PrisonerSkeleton", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 3, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Archer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Archer'}],
    },
    "Lightning Bolt": {
        "id": 0x0090, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Lightning",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Ossuary', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}],
    },
    "Vampirism": {
        "id": 0x0091, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "LeechBuff", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Ossuary', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}],
    },
    "Mage Outfit": {
        "id": 0x0092, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 2, "item": "PrisonerMage", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'PrisonRoof', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Ossuary', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'AncientTemple', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Crypt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Tumulus', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Mage360'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mage360'}],
    },
    "Great Owl of War": {
        "id": 0x0093, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "Owl",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 1, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'PrisonDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Crypt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Castle', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Cliff', 'min_bc': 1, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'DookuCastle', 'min_bc': 1, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'DookuCastleHard', 'min_bc': 1, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}],
    },
    "Son Goku Outfit": {
        "id": 0x0094, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "PrisonerSonGoku", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 3, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'PrisonDepths', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Crypt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Castle', 'min_bc': 3, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'Cliff', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}, {'biome': 'DookuCastleHard', 'min_bc': 3, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'KunaiMaster'}],
    },
    "Acrobatipack": {
        "id": 0x0095, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Backpack_Ranged",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'PrisonRoof', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'ClockTower', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}],
    },
    "Crossbowman Outfit": {
        "id": 0x0096, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "PrisonerCrossbowMan", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'PrisonRoof', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'ClockTower', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}, {'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'CrossbowMan'}],
    },
    "Rampart": {
        "id": 0x0097, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Rampart", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}],
    },
    "Bloodthirsty Shield": {
        "id": 0x0098, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BloodShield", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}],
    },
    "Ice Shield": {
        "id": 0x0099, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "IceShield",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}],
    },
    "Sand Outfit": {
        "id": 0x009A, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 4, "item": "PrisonerSand", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 4, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'PrisonRoof', 'min_bc': 4, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'SewerDepths', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}, {'biome': 'Distillery', 'min_bc': 4, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shield'}],
    },
    "Porcupack": {
        "id": 0x009B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Backpack_Melee", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'Rat'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Rat'}],
    },
    "Fire Grenade": {
        "id": 0x009C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FireBomb",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'SewerShort', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 1, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}],
    },
    "Magnetic Grenade": {
        "id": 0x009D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "MagnetGrenade", "rarity": "Rare",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'SewerShort', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 2, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 1, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Grenader'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Grenader'}],
    },
    "Assassin's Dagger": {
        "id": 0x009E, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "BackStabber",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Ripper": {
        "id": 0x009F, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_AmmoOnHit",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Assault Shield": {
        "id": 0x00A0, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "DashShield",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Cleaver": {
        "id": 0x00A1, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "GroundSaw",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}],
    },
    "Spartan Sandals": {
        "id": 0x00A2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BumpBoots",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}],
    },
    "Phaser": {
        "id": 0x00A3, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BackBlink", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Runner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Runner'}],
    },
    "Corrupted Power": {
        "id": 0x00A4, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "DamageBuff", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'PrisonCorrupt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}],
    },
    "Explosive Decoy": {
        "id": 0x00A5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Decoy", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'PrisonCorrupt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}],
    },
    "Warrior Outfit": {
        "id": 0x00A6, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "PrisonerWarrior", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shielder'}],
    },
    "Knife Dance": {
        "id": 0x00A7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "KnivesCircle", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 3, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}],
    },
    "Oiled Sword": {
        "id": 0x00A8, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "OilSword",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 1, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 3, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 2, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'BatDasher'}],
    },
    "Wave of Denial": {
        "id": 0x00A9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Shockwave", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Ossuary', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'AncientTemple', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Tumulus', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}],
    },
    "Powerful Gernade": {
        "id": 0x00AA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ExplosiveGrenade",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Ossuary', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'AncientTemple', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Tumulus', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}],
    },
    "Aphrodite Outfit": {
        "id": 0x00AB, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "PrisonerAphrodite", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Ossuary', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'ClockTower', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Castle', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Shipwreck', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ClusterGrenader'}],
    },
    "Repeater Crossbow": {
        "id": 0x00AC, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "MultiCrossBow", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 2, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Swamp', 'min_bc': 1, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Ninja'}],
    },
    "Hayabusa Boots": {
        "id": 0x00AD, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 1, "item": "MultiKickBoots",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 2, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'ClockTower', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Crypt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Swamp', 'min_bc': 1, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Ninja'}],
    },
    "Black Outfit": {
        "id": 0x00AE, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "PrisonerBlack",  "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 3, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'ClockTower', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Crypt', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Swamp', 'min_bc': 3, 'max_bc': 2, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Ninja'}, {'biome': 'PurpleGarden', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Ninja'}],
    },
    "Frantic Sword": {
        "id": 0x00AF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "LowHealth", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}],
    },
    "Kamikaze Outfit": {
        "id": 0x00B0, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "PrisonerKamikaze",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}],
    },
    "Neon Outfit": {
        "id": 0x00B1, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "PrisonerNeon", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerShort', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'PrisonDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'SewerDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'AncientTemple', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Cemetery', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Crypt', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Distillery', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}, {'biome': 'Shipwreck', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BatKamikaze'}],
    },
    "Recovery": {
        "id": 0x00B2, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_SpeedHeal",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Armadillopack": {
        "id": 0x00B3, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_SuperParry",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Death's Scythe": {
        "id": 0x00B4, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "AdeleScythe",
        "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Rapier": {
        "id": 0x00B5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Rapier", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Scorpio'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Scorpio'}],
    },
    "Sewers Outfit": {
        "id": 0x00B6, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "PrisonerSewers", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Scorpio'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Scorpio'}],
    },
    "What Doesn't Kill Me": {
        "id": 0x00B7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_HealOnParry",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}],
    },
    "Swarm": {
        "id": 0x00B8, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SideBomb", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}],
    },
    "Valmont's Whip": {
        "id": 0x00B9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Whip", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Worm'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Worm'}],
    },
    "Force Shield": {
        "id": 0x00BA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HoldShield", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}],
    },
    "Stilt Outfit": {
        "id": 0x00BB, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "PrisonerStilt", "rarity": "Rare",
        "sources": [{'biome': 'SewerShort', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'SewerDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}, {'biome': 'Cliff', 'min_bc': 1, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'WormZombie'}],
    },
    "Spite Sword": {
        "id": 0x00BC, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "RevengeSword", "rarity": "Legendary",
        "sources": [{'biome': 'SewerShort', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Greenhouse', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}],
    },
    "Frostbite": {
        "id": 0x00BD, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_ColdDmg",
        "sources": [{'biome': 'SewerShort', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Greenhouse', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Fly'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fly'}],
    },
    "Pyrotechnics": {
        "id": 0x00BE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FlameThrower",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'Swamp', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fogger'}],
    },
    "Ghost Outfit": {
        "id": 0x00BF, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 2, "item": "PrisonerGhost", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'AncientTemple', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Fogger'}, {'biome': 'Swamp', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fogger'}],
    },
    "War Spear": {
        "id": 0x00C0, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Spear",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hammer'}, {'biome': 'Distillery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hammer'}],
    },
    "Oil Grenade": {
        "id": 0x00C1, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "OilBomb",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hammer'}, {'biome': 'Distillery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hammer'}],
    },
    "Cluster Grenade": {
        "id": 0x00C2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ClusterBomb",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'PrisonRoof', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}],
    },
    "Heavy Turret": {
        "id": 0x00C3, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HeavyTurret", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'PrisonRoof', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}],
    },
    "Demon Outfit": {
        "id": 0x00C4, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "PrisonerDemon", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'PrisonRoof', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cemetery', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Swamp', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cliff', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}],
    },
    "Execution": {
        "id": 0x00C5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Execute_LowHealth",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'PrisonRoof', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cemetery', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Comboter'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Comboter'}],
    },
    "Crusher": {
        "id": 0x00C6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Crusher",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Cemetery', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}],
    },
    "Open Wounds": {
        "id": 0x00C7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Bleed", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Cemetery', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}],
    },
    "Carduus Outfit": {
        "id": 0x00C8, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "PrisonerCarduus", "rarity": "Rare",
        "sources": [{'biome': 'PrisonDepths', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'AncientTemple', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Cemetery', 'min_bc': 1, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Distillery', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spinner'}],
    },
    "Barbed Tips": {
        "id": 0x00C9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgPlantedArrow",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Blobby'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Blobby'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Blobby'}],
    },
    "Flawless": {
        "id": 0x00CA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "PerfectHalberd", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Cliff', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Stomper'}],
    },
    "Blind Faith": {
        "id": 0x00CB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DodgeSlow",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Stomper'}, {'biome': 'Cliff', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Stomper'}],
    },
    "Flamethrower Turret": {
        "id": 0x00CC, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FireTurret", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Crypt', 'min_bc': 0, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Tumulus', 'min_bc': 1, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Shocker'}],
    },
    "Cloud Outfit": {
        "id": 0x00CD, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "PrisonerCloud", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 3, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Crypt', 'min_bc': 3, 'max_bc': 0, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Shocker'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Shocker'}],
    },
    "Hattori's Katana": {
        "id": 0x00CE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Katana",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'Crypt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}],
    },
    "Kill Bill Outfit": {
        "id": 0x00CF, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "PrisonerKillBill", "rarity": "Rare",
        "sources": [{'biome': 'PrisonCorrupt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'StiltVillage', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'Crypt', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}, {'biome': 'Bank', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Samurai'}],
    },
    "Nerves of Steel": {
        "id": 0x00D0, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "PreciseBow",
        "sources": [{'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Stun Grenade": {
        "id": 0x00D1, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "StunningGrenade",
        "sources": [{'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Lightspeed": {
        "id": 0x00D2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Dash",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Scheme": {
        "id": 0x00D3, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgSkl",
        "sources": [{'biome': 'PrisonRoof', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Minimoth'}],
    },
    "Gastronomy": {
        "id": 0x00D4, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Hot",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Telluric Shock": {
        "id": 0x00D5, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SeismicStomp",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Torch": {
        "id": 0x00D6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Burner",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spawner'}, {'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spawner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Spawner'}],
    },
    "Spiked Boots": {
        "id": 0x00D7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SpikedBoots", "rarity": "Rare",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}],
    },
    "Barnacle": {
        "id": 0x00D8, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "CeilTurret",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}],
    },
    "Armadillo Pack": {
        "id": 0x00D9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Backpack_Shield",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SpikedSatyr'}],
    },
    "Seismic Strike": {
        "id": 0x00DA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SismicBlade", "rarity": "Rare",
        "sources": [{'biome': 'Ossuary', 'min_bc': 2, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Bomber'}],
    },
    "Aladdin Outfit": {
        "id": 0x00DB, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "PrisonerAladdin", "rarity": "Rare",
        "sources": [{'biome': 'Ossuary', 'min_bc': 3, 'max_bc': 3, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Astrolab', 'min_bc': 3, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Tumulus', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Bomber'}, {'biome': 'Bank', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Bomber'}],
    },
    "Alchemic Carbine": {
        "id": 0x00DC, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "AlchemicGun",
        "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Front Line Shield": {
        "id": 0x00DD, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "WarriorShield",
        "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Sadist's Stiletto": {
        "id": 0x00DE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BleedCrit",
        "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Spiker'}, {'biome': 'Greenhouse', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Spiker'}],
    },
    "Piccolo Concierge Outfit": {
        "id": 0x00DF, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "Behemoth1",
        "sources": [{'biome': 'Bridge', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Misunderstood Concierge Outfit": {
        "id": 0x00E0, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 2, "item": "Behemoth2",
        "sources": [{'biome': 'Bridge', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Blacksmith Concierge Outfit": {
        "id": 0x00E1, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "Behemoth3",
        "sources": [{'biome': 'Bridge', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Golden Concierge Outfit": {
        "id": 0x00E2, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 4, "item": "Behemoth4",
        "sources": [{'biome': 'Bridge', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Starved Conjunctivius Outfit": {
        "id": 0x00E3, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "Beholder1",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Enraged Conjunctivius Outfit": {
        "id": 0x00E4, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 2, "item": "Beholder2",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Tentacled Conjunctivius Outfit": {
        "id": 0x00E5, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "Beholder3",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Aurora Borealis Conjunctivius Outfit": {
        "id": 0x00E6, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 4, "item": "Beholder4",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Parry Shield": {
        "id": 0x00E7, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "ParryShield",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Leghugger": {
        "id": 0x00E8, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "SpawnLilStaphy",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Wrenching Whip": {
        "id": 0x00E9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "HookWhip", "rarity": "Rare",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Shipwreck', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}],
    },
    "Masochist": {
        "id": 0x00EA, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_CDR_locked",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Shipwreck', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}],
    },
    "Scavenged Bombard": {
        "id": 0x00EB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "Cannon",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Shipwreck', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'PirateChief'}],
    },
    "Emergency Door": {
        "id": 0x00EC, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "PortableDoor",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Instinct of the Master of Arms": {
        "id": 0x00ED, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Traps",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Maria's Cat": {
        "id": 0x00EE, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "Purple", "min_bc": 0, "item": "SpawnCat",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Wings of the Crow": {
        "id": 0x00EF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Wings",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Golem'}],
    },
    "Fireball": {
        "id": 0x00F0, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FireBall",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'OrbLauncher'}],
    },
    "Parting Gift": {
        "id": 0x00F1, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgSkillRanged",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Duelist'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Duelist'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Duelist'}],
    },
    "Shrapnel Axes": {
        "id": 0x00F2, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BulletBlade", "rarity": "Rare",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Castle', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'DookuCastleHard', 'min_bc': 4, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Demon'}],
    },
    "Drifter Outfit": {
        "id": 0x00F3, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 2, "item": "PrisonerHyperlight", "rarity": "Rare",
        "sources": [{'biome': 'AncientTemple', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Cavern', 'min_bc': 2, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Castle', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'Bank', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Demon'}, {'biome': 'DookuCastleHard', 'min_bc': 4, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Demon'}],
    },
    "Dead Inside": {
        "id": 0x00F4, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_DeathBomb",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Skul Outfit": {
        "id": 0x00F5, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "Skul",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Grappling Hook": {
        "id": 0x00F6, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Hook", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Tumulus', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}],
    },
    "Knockback Shield": {
        "id": 0x00F7, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BumpShield", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Tumulus', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}],
    },
    "Sylvanian Outfit": {
        "id": 0x00F8, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 4, "item": "PrisonerSylvanian", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Tumulus', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Cliff', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Hooker'}, {'biome': 'Bank', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hooker'}],
    },
    "Hokuto's Bow": {
        "id": 0x00F9, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "MarkBow",
        "sources": [{'biome': 'Cemetery', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}, {'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}],
    },
    "Bison Outfit": {
        "id": 0x00FA, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 4, "item": "PrisonerBison", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}, {'biome': 'ClockTower', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}, {'biome': 'Bank', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'LeapingDuelyst'}],
    },
    "Corrosive Cloud": {
        "id": 0x00FB, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ToxicCloud", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FlyZombie'}],
    },
    "Shovel": {
        "id": 0x00FC, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Shovel", "rarity": "Rare",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FlyZombie'}],
    },
    "Shared Suffering": {
        "id": 0x00FD, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_ShareDamage",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FlyZombie'}],
    },
    "Tombstone": {
        "id": 0x00FE, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Tombstone",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FlyZombie'}],
    },
    "Predator": {
        "id": 0x00FF, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_InvisibilityOnKill",
        "sources": [{'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'TimeKeeperBot'}],
    },
    "Sweet Blob": {
        "id": 0x0100, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlobbyFlameGum",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Point Blank": {
        "id": 0x0101, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgNearRanged",
        "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FatZombie'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'FatZombie'}],
    },
    "Death Orb": {
        "id": 0x0102, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SlowOrb",
        "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}],
    },
    "Spiked Shield": {
        "id": 0x0103, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "SpikeShield",
        "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}, {'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'AxeThrower'}],
    },
    "Apex Temporal Outfit": {
        "id": 0x0104, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "Assassin1",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Red Temporal Outfit": {
        "id": 0x0105, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 2, "item": "Assassin2",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Hunter's Temporal Outfit": {
        "id": 0x0106, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "Assassin3",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Devilish Temporal Outfit": {
        "id": 0x0107, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 4, "item": "Assassin4",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Throwing Spear": {
        "id": 0x0108, "region": "Checks", "type": "blueprint_floor",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "ThrowingSpear",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_floor'}],
    },
    "Santa Outfit": {
        "id": 0x0109, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 4, "item": "PrisonerSanta",
        "sources": [{'biome': 'Cavern', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_floor'}],
    },
    "Boy's Axe": {
        "id": 0x010A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GodAxe",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Earthquaker'}],
    },
    "Ice Armor": {
        "id": 0x010B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "IceArmor",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Earthquaker'}],
    },
    "Toothpick": {
        "id": 0x010C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "Club",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Earthquaker'}],
    },
    "Flying Alcoholic Outfit": {
        "id": 0x010D, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "PrisonerXmas",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'StompSkeleton'}],
    },
    "Magic Missiles": {
        "id": 0x010E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "MagicSalve", "rarity": "Rare",
        "sources": [{'biome': 'Cavern', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Arbiter'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Arbiter'}],
    },
    "Shaman Outfit": {
        "id": 0x010F, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 4, "item": "PrisonerShaman", "rarity": "Rare",
        "sources": [{'biome': 'Cavern', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Arbiter'}, {'biome': 'Bank', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Arbiter'}],
    },
    "Mutineer Giant Outfit": {
        "id": 0x0110, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 1, "item": "Giant1",
        "sources": [{'biome': 'Giant', 'min_bc': 1, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Royal Giant Outfit": {
        "id": 0x0111, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 2, "item": "Giant2",
        "sources": [{'biome': 'Giant', 'min_bc': 2, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Frustrated Giant's Outfit": {
        "id": 0x0112, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 3, "item": "Giant3",
        "sources": [{'biome': 'Giant', 'min_bc': 3, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Cavern Dweller Giant Outfit": {
        "id": 0x0113, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 4, "item": "Giant4",
        "sources": [{'biome': 'Giant', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Alienation": {
        "id": 0x0114, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_EasierCurse",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Knight's Outfit": {
        "id": 0x0115, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "ShovelKnight",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Initiative": {
        "id": 0x0116, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_DmgFirstHit",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'KingsFinger'}],
    },
    "Tornado": {
        "id": 0x0117, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "Tornado", "rarity": "Rare",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}],
    },
    "Necromancy": {
        "id": 0x0118, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_ScaledHealth",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'CastleKnight'}],
    },
    "Hayabusa Gauntlets": {
        "id": 0x0119, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "QuickFists", "rarity": "Rare",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Lancer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Lancer'}],
    },
    "Soldier's Resistance": {
        "id": 0x011A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Health",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Lancer'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Lancer'}],
    },
    "Barrel Launcher": {
        "id": 0x011B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BarrelLauncher", "rarity": "Rare",
        "sources": [{'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hurler'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Hurler'}],
    },
    "Tesla Coil": {
        "id": 0x011C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "TeslaCoil",
        "sources": [{'biome': 'Distillery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Mimic'}],
    },
    "Loyal Hand of the King Outfit": {
        "id": 0x011D, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 1, "item": "Hotk1",
        "sources": [{'biome': 'Throne', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Majestic Hand of the King Outfit": {
        "id": 0x011E, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 2, "item": "Hotk2",
        "sources": [{'biome': 'Throne', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Red Hand of the King Outfit": {
        "id": 0x011F, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 3, "item": "Hotk3",
        "sources": [{'biome': 'Throne', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "The Leeching Hand of the King Outfit": {
        "id": 0x0120, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 4, "item": "Hotk4",
        "sources": [{'biome': 'Throne', 'min_bc': 4, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Sonic Carbine": {
        "id": 0x0121, "region": "Checks", "type": "blueprint_floor",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "SonicCrossbow",
        "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_floor'}],
    },
    "Hemorrhage": {
        "id": 0x0122, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "BleedAxe",
        "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'DeathMage'}],
    },
    "Thunder Shield": {
        "id": 0x0123, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "ThunderShield",
        "sources": [{'biome': 'Astrolab', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy', 'mob': 'Defender'}],
    },
    "King Outfit": {
        "id": 0x0124, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "KingDefault",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "White King Outfit": {
        "id": 0x0125, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "KingWhite",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Gardener Outfit": {
        "id": 0x0126, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "PrisonerGardener",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_floor'}],
    },
    "Flashing Fans": {
        "id": 0x0127, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "ParryBlade", "rarity": "Rare",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Pitcher'}],
    },
    "Mushroom King Outfit": {
        "id": 0x0128, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 3, "item": "PrisonerMushroom",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Pitcher'}],
    },
    "Mushroom Boi!": {
        "id": 0x0129, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "SpawnFriendlyHardy",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'ThrowableMushroom'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'ThrowableMushroom'}],
    },
    "Friendly Hardy Outfit": {
        "id": 0x012A, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 1, "item": "PrisonerFriendlyHardy",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'ThrowableMushroom'}, {'biome': 'Cliff', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'ThrowableMushroom'}],
    },
    "Smoke Bomb": {
        "id": 0x012B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "SmokeBomb", "rarity": "Rare",
        "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fugitive'}],
    },
    "Fugitive Outfit": {
        "id": 0x012C, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 2, "item": "PrisonerFugitive",
        "sources": [{'biome': 'Swamp', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Fugitive'}],
    },
    "Blowgun": {
        "id": 0x012D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "Blowgun",
        "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Blowgunner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Blowgunner'}],
    },
    "Blowgunner Outfit": {
        "id": 0x012E, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "PrisonerBlowgunner",
        "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Blowgunner'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Blowgunner'}],
    },
    "Sacrificial Tick Outfit": {
        "id": 0x012F, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "TickSacrifice",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_floor'}],
    },
    "Sharp Mama Tick Outfit": {
        "id": 0x0130, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 1, "item": "Tick1",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Wigged Mama Tick Outfit": {
        "id": 0x0131, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 2, "item": "Tick2",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Mad Tick Outfit": {
        "id": 0x0132, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 3, "item": "Tick3",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Furious Tick Outfit": {
        "id": 0x0133, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 4, "item": "Tick4",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Tick Outfit": {
        "id": 0x0134, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 4, "item": "PrisonerTick",
        "sources": [{'biome': 'Swamp', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Tick'}],
    },
    "Serenade": {
        "id": 0x0135, "region": "Checks", "type": "blueprint_floor",
        "dlc": "FatalFalls", "min_bc": 0, "item": "FlyingSword",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_floor'}],
    },
    "Cultist Outfit": {
        "id": 0x0136, "region": "Checks", "type": "blueprint_floor",
        "dlc": "FatalFalls", "min_bc": 0, "item": "Cultist",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_floor'}],
    },
    "Snake Fangs": {
        "id": 0x0137, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "SnakeFang",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'JavelinSnake'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'JavelinSnake'}],
    },
    "Javelin Snake Outfit": {
        "id": 0x0138, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 0, "item": "PrisonerJavelinSnake",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'JavelinSnake'}, {'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'JavelinSnake'}],
    },
    "Ferryman's Lantern": {
        "id": 0x0139, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "Lantern", "rarity": "Rare",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Necromant'}],
    },
    "Necromancer Outfit": {
        "id": 0x013A, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 0, "item": "PrisonerNecromant",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'Necromant'}],
    },
    "Lightning Rods": {
        "id": 0x013B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "LightningRod",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'BootlegHomunculus'}],
    },
    "Bootleg Outfit": {
        "id": 0x013C, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 0, "item": "PrisonerBootleg",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'BootlegHomunculus'}],
    },
    "Dagger of Profit": {
        "id": 0x013D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "CupidityDagger",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'U28_Steal'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'U28_Steal'}],
    },
    "Guillain Outfit": {
        "id": 0x013E, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "GuillainThief",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'U28_Steal'}, {'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'U28_Steal'}],
    },
    "Whip Sword": {
        "id": 0x013F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "SnakeSwordWeapon",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Harpy'}, {'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Harpy'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Harpy'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Harpy'}],
    },
    "Rebound Stone": {
        "id": 0x0140, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "BouncingStone",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Buer'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Buer'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Buer'}],
    },
    "Rusted Scarecrow Outfit": {
        "id": 0x0141, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 1, "item": "Gardener1",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 1, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Cardinal Scarecrow Outfit": {
        "id": 0x0142, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 2, "item": "Gardener2",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 2, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Festering Scarecrow Outfit": {
        "id": 0x0143, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 3, "item": "Gardener3",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 3, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Murderous Scarecrow Outfit": {
        "id": 0x0144, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 4, "item": "Gardener4",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 4, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Abyssal Trident": {
        "id": 0x0145, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "Trident",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Maw of the Deep": {
        "id": 0x0146, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "Shark",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'AnchorGuy'}],
    },
    "Anchor Guy Outfit": {
        "id": 0x0147, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ANCHORGUY", "rarity": "Rare",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'AnchorGuy'}],
    },
    "Delayed Hedgehog Outfit": {
        "id": 0x0148, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "BlueErinaceus",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_floor'}],
    },
    "Burnished Servants Outfit": {
        "id": 0x0149, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 1, "item": "Servante1",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Indigo Servants Outfit": {
        "id": 0x014A, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 2, "item": "Servante2",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Shining Servants Outfit": {
        "id": 0x014B, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 3, "item": "Servante3",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Luminous Servants Outfit": {
        "id": 0x014C, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 4, "item": "Servante4",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "White Gold Queen Outfit": {
        "id": 0x014D, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 1, "item": "Queen1",
        "sources": [{'biome': 'QueenArena', 'min_bc': 1, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Cherry Blossom Queen Outfit": {
        "id": 0x014E, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 2, "item": "Queen2",
        "sources": [{'biome': 'QueenArena', 'min_bc': 2, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Spicy Queen Outfit": {
        "id": 0x014F, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 3, "item": "Queen3",
        "sources": [{'biome': 'QueenArena', 'min_bc': 3, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Stinging Queen Outfit": {
        "id": 0x0150, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 4, "item": "Queen4",
        "sources": [{'biome': 'QueenArena', 'min_bc': 4, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Banker Outfit": {
        "id": 0x0151, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "Banker",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Gold Digger": {
        "id": 0x0152, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "GoldDigger",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'U28_VacuumCleaner'}],
    },
    "Midas' Blood": {
        "id": 0x0153, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_U28_PerkGoldPerDamage",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'U28_VacuumCleaner'}],
    },
    "Money Shooter": {
        "id": 0x0154, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "MoneyShooter",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'GoldenBatKamikaze'}],
    },
    "Alucard's Shield": {
        "id": 0x0155, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "Purple", "min_bc": 0, "item": "AlucardShield",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Bible": {
        "id": 0x0156, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "Bible",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'MiniWerewolf'}, {'biome': 'PurpleGarden', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 2, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'MiniWerewolf'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 0, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'MiniWerewolf'}, {'biome': 'DookuCastleHard', 'min_bc': 1, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}],
    },
    "Hector Outfit": {
        "id": 0x0157, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 1, "item": "Hector",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}, {'biome': 'DookuCastle', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}, {'biome': 'DookuCastleHard', 'min_bc': 1, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Werewolf'}],
    },
    "Haunted Armor Outfit": {
        "id": 0x0158, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "HauntedArmor",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'LancerPurple'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'HauntedArmor'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'LancerPurple'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'HauntedArmor'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'LancerPurple'}],
    },
    "Holy Water": {
        "id": 0x0159, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "HolyWater",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Merman'}],
    },
    "Bat Volley": {
        "id": 0x015A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "BatVolley",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'BatDasherPurple'}],
    },
    "Cross": {
        "id": 0x015B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "Cross",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'BoneThrower'}, {'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'BoneThrower'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'BoneThrower'}],
    },
    "Simon Outfit": {
        "id": 0x015C, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "Simon",
        "sources": [{'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Throwing Axe": {
        "id": 0x015D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "ThrowingAxe",
        "sources": [{'biome': 'DookuCastle', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'HauntedArmor'}, {'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'HauntedArmor'}],
    },
    "Richter Outfit": {
        "id": 0x015E, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "RichterROB",
        "sources": [{'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Cold Death Outfit": {
        "id": 0x015F, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 1, "item": "Adele1",
        "sources": [{'biome': 'DeathArena', 'min_bc': 1, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Twilight Death Outfit": {
        "id": 0x0160, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 2, "item": "Adele2",
        "sources": [{'biome': 'DeathArena', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Regal Death Outfit": {
        "id": 0x0161, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 3, "item": "Adele3",
        "sources": [{'biome': 'DeathArena', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Pale Death Outfit": {
        "id": 0x0162, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 4, "item": "Adele4",
        "sources": [{'biome': 'DeathArena', 'min_bc': 4, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Alucard Outfit": {
        "id": 0x0163, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "Alucard",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Sypha Outfit": {
        "id": 0x0164, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "Sypha",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Trevor Outfit": {
        "id": 0x0165, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "Trevor",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_floor'}],
    },
    "Moonlit Dracula Outfit": {
        "id": 0x0166, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 1, "item": "Dooku1",
        "sources": [{'biome': 'DookuArena', 'min_bc': 1, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Grand Dracula Outfit": {
        "id": 0x0167, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 2, "item": "Dooku2",
        "sources": [{'biome': 'DookuArena', 'min_bc': 2, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Vampiric Dracula Outfit": {
        "id": 0x0168, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 3, "item": "Dooku3",
        "sources": [{'biome': 'DookuArena', 'min_bc': 3, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Dark Lord Dracula Outfit": {
        "id": 0x0169, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 4, "item": "Dooku4",
        "sources": [{'biome': 'DookuArena', 'min_bc': 4, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Caltrops": {
        "id": 0x016A, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "P_Caltrops",
        "sources": [{'biome': 'Challenge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Lighthouse Key": {
        "id": 0x016B, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "LighthouseKey",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Collector's Syringe": {
        "id": 0x016C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "CollectorSpin",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Blood Drinker": {
        "id": 0x016D, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_BloodDrinker",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Stomper": {
        "id": 0x016E, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Stomper",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Relentless": {
        "id": 0x016F, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Berzerker",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Gotta Go Fast": {
        "id": 0x0170, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_GottaGoFast",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Tinker": {
        "id": 0x0171, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Tinker",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Menagerie": {
        "id": 0x0172, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Menagerie",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Grenadier": {
        "id": 0x0173, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Grenadier",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Superconductor": {
        "id": 0x0174, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Superconductor",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Assassin": {
        "id": 0x0175, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Assassin",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Damned": {
        "id": 0x0176, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Damned",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Boss Stem Cell 1": {"id": 0x0177, "region": "Throne", "type": "rune", "dlc": "", "min_bc": 0, "item": "BossRune1","sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'BossCell'}],},
    "Boss Stem Cell 2": {"id": 0x0178, "region": "Throne", "type": "rune", "dlc": "", "min_bc": 1, "item": "BossRune2","sources": [{'biome': 'Throne', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'BossCell'}],},
    "Boss Stem Cell 3": {"id": 0x0179, "region": "Throne", "type": "rune", "dlc": "", "min_bc": 2, "item": "BossRune3","sources": [{'biome': 'Throne', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'BossCell'}],},
    "Boss Stem Cell 4": {"id": 0x017A, "region": "Throne", "type": "rune", "dlc": "", "min_bc": 3, "item": "BossRune4","sources": [{'biome': 'Throne', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'BossCell'}],},
    "Boss Stem Cell 5": {"id": 0x017B, "region": "Giant", "type": "rune", "dlc": "RiseOfTheGiant", "min_bc": 4, "item": "BossRune5","sources": [{'biome': 'Giant', 'min_bc': 4, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'BossCell'}],},
    "Symmetrical Lance": {
        "id": 0x017C, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "KingsSpear",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Evil Empire Head": {
        "id": 0x017D, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "EvilEmpire",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Rhythm n' Bouzouki": {
        "id": 0x017E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "RhythmicBlade", "rarity": "Rare",
        "sources": [{'biome': 'Swamp', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy', 'mob': 'Tick'}],
    },
    "Challenger's Rune": {
        "id": 0x017F, "region": "Checks", "type": "rune",
        "dlc": "", "min_bc": 0, "item": "ScoringKey",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'rune'}],
    },
    "Flint": {
        "id": 0x0180, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "BehemothHammer",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Heavy Crossbow": {
        "id": 0x0181, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "CrossBow",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Impaler": {
        "id": 0x0182, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ImpaleSpear",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Melee": {
        "id": 0x0183, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_ManyMobsAround",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Ammo": {
        "id": 0x0184, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Ammo",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Acceptance": {
        "id": 0x0185, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Curse",
        "sources": [{'biome': 'Bridge', 'min_bc': 3, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Concierge Outfit": {
        "id": 0x0186, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "BehemothDefault",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Flawless Concierge Outfit": {
        "id": 0x0187, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "FlawlessBehemoth",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Concierge Flame": {
        "id": 0x0188, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "ConciergeFlame",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Tentacle": {
        "id": 0x0189, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "TentacleWhip",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Cursed Sword": {
        "id": 0x018A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "EvilSword",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Extended Healing": {
        "id": 0x018B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Food",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Rally": {
        "id": 0x018C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_Rally",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Advanced Forge 1": {
        "id": 0x018D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ForgeRefine1",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Classic Conjunctivius Outfit": {
        "id": 0x018E, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "BeholderDefault",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Flawless Conjunctivius Outfit": {
        "id": 0x018F, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "FlawlessBeholder",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Conjunctivius Tentacles": {
        "id": 0x0190, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "ConjunctiviusHead",
        "sources": [{'biome': 'BeholderPit', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Scythe Claw": {
        "id": 0x0191, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "TickScytheLeft",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Classic Mama Tick Outfit": {
        "id": 0x0192, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "TickDefault",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Flawless Mama Tick Outfit": {
        "id": 0x0193, "region": "Checks", "type": "skin",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "FlawlessTick",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'blueprint_enemy'}],
    },
    "Mama Tick Eye": {
        "id": 0x0194, "region": "Checks", "type": "head",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "MamaTickEye",
        "sources": [{'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'item_no_blueprint'}],
    },
    "Ice Shards": {
        "id": 0x0195, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ThrowingIce",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Ice Crossbow": {
        "id": 0x0196, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "FrostCrossBow",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Velocity": {
        "id": 0x0197, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_SpeedBuff",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Tainted Flask": {
        "id": 0x0198, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_CorruptedHealing",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Emergency Triage": {
        "id": 0x0199, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_QuickHeal",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Classic Temporal Outfit": {
        "id": 0x019A, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "AssassinDefault",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Flawless Time Keeper Outfit": {
        "id": 0x019B, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "FlawlessAssassin",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Time Keeper Hat": {
        "id": 0x019C, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "TimeKeeperHat",
        "sources": [{'biome': 'TopClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Giantkiller": {
        "id": 0x019D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GiantKiller",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Giant Whistle": {
        "id": 0x019E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GiantWhistle",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Classic Giant Outfit": {
        "id": 0x019F, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GiantDefault",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Flawless Giant Outfit": {
        "id": 0x0200, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "FlawlessGiant",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Giant Flame": {
        "id": 0x0201, "region": "Checks", "type": "head",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "GiantFlame",
        "sources": [{'biome': 'Giant', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Scarecrow's Sickles": {
        "id": 0x0202, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "GardenerSickles",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Classic Scarecrow Outfit": {
        "id": 0x0203, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 0, "item": "GardenerDefault",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Flawless Scarecrow Outfit": {
        "id": 0x0204, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 0, "item": "FlawlessGardener",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy'}],
    },
    "Scarecrow Hat": {
        "id": 0x0205, "region": "Checks", "type": "head",
        "dlc": "FatalFalls", "min_bc": 0, "item": "ScarecrowHat",
        "sources": [{'biome': 'GardenerStage', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'item_no_blueprint'}],
    },
    "Recycling Tubes": {
        "id": 0x0206, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "ArmoryUnlock",
        "sources": [{'biome': 'Throne', 'min_bc': 1, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "The Hand of the King Outfit": {
        "id": 0x0207, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "HotkDefault",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Flawless Hand of the King Outfit": {
        "id": 0x0208, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "FlawlessHotk",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy'}],
    },
    "Hand of the King Flame": {
        "id": 0x0209, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "HandOfTheKingFlame",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Gilded Yumi": {
        "id": 0x020A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "HeavyBow",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Bladed Tonfas": {
        "id": 0x020B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ElbowBlades",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Wrecking Ball": {
        "id": 0x020C, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "WreckingBall",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Servants Outfit": {
        "id": 0x020D, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ServanteDefault",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Flawless Servants Outfit": {
        "id": 0x020E, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "FlawlessServante",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Servants Mask": {
        "id": 0x020F, "region": "Checks", "type": "head",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ServantsMask",
        "sources": [{'biome': 'Lighthouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Queen's Rapier": {
        "id": 0x0210, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "QueenRapier",
        "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Queen Outfit": {
        "id": 0x0211, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "QueenDefault",
        "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Flawless Queen Outfit": {
        "id": 0x0212, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "FlawlessQueen",
        "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy'}],
    },
    "Queen Flame": {
        "id": 0x0213, "region": "Checks", "type": "head",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "QueenFlame",
        "sources": [{'biome': 'QueenArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Collector Outfit": {
        "id": 0x0214, "region": "Checks", "type": "skin",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "CollectorDefault",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'blueprint_enemy'}],
    },
    "Collector Hood": {
        "id": 0x0215, "region": "Checks", "type": "head",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "CollectorHood",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Death Outfit": {
        "id": 0x0216, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "AdeleDefault",
        "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Flawless Death Outfit": {
        "id": 0x0217, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "FlawlessAdele",
        "sources": [{'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Vampire Killer": {
        "id": 0x0218, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "VampireKiller",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Dracula Outfit": {
        "id": 0x0219, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "DookuDefault",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Flawless Dracula Outfit": {
        "id": 0x021A, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "FlawlessDooku",
        "sources": [{'biome': 'DookuArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy'}],
    },
    "Root Grenade": {
        "id": 0x021B, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "RootBomb",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Cocoon": {
        "id": 0x021C, "region": "Checks", "type": "blueprint_floor",
        "dlc": "FatalFalls", "min_bc": 0, "item": "BubbleShieldPower",
        "sources": [{'biome': 'Cliff', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_floor'}],
    },
    "Broadsword": {
        "id": 0x021D, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "BroadSword",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Vorpan": {
        "id": 0x021E, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "Pan",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Marksman's Bow": {
        "id": 0x021F, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "LongBow",
        "sources": [{'biome': 'Ossuary', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Explosive Crossbow": {
        "id": 0x0220, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "ExplosiveCrossBow",
        "sources": [{'biome': 'PrisonCourtyard', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Boomerang": {
        "id": 0x0221, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Boomerang",
        "sources": [{'biome': 'Castle', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Morning Star": {
        "id": 0x0222, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "Purple", "min_bc": 0, "item": "WiggleWhip",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Punishment": { 
        "id": 0x0223, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "AreaShield",
        "sources": [{'biome': 'ClockTower', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Golden Outfit": { 
        "id": 0x0224, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "PrisonerGold",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Indulgence": { 
        "id": 0x0225, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Indulgence",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SoreLooser'}],
    },
    "Damned Vigor": { 
        "id": 0x0226, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "P_DamnedVigor",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'SoreLooser'}],
    },
    "Misericorde": { 
        "id": 0x0227, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Misericord",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'DoomBringer'}],
    },
    "Demonic Strength": { 
        "id": 0x0228, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "P_DemonicForce",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'DoomBringer'}],
    },
    "Anathema": { 
        "id": 0x0229, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "Anathema",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Curser'}],
    },
    "Cursed Flask": { 
        "id": 0x022A, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 2, "item": "P_CursedFlask",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'Curser'}],
    },
    "Iron Staff": {
        "id": 0x022B, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "FatalFalls", "min_bc": 0, "item": "GiantStaff",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'AxeStatue'}],
    },
    "Statue Outfit": {
        "id": 0x022C, "region": "Checks", "type": "skin",
        "dlc": "FatalFalls", "min_bc": 0, "item": "Statue",
        "sources": [{'biome': 'Tumulus', 'min_bc': 0, 'max_bc': 5, 'dlc': 'FatalFalls', 'type': 'blueprint_enemy', 'mob': 'AxeStatue'}],
    },
    "Medusa's Head": {
        "id": 0x022D, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "Purple", "min_bc": 0, "item": "MedusaHead",
        "sources": [{'biome': 'DookuCastleHard', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'blueprint_enemy', 'mob': 'Medusa'}],
    },
    "Gold Plating": {
        "id": 0x022E, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_U28_PerkGoldShield",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ShopMimic'}],
    },
    "Get Rich Quick": {
        "id": 0x022F, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "", "min_bc": 0, "item": "P_U28_PerkGoldSpeed",
        "sources": [{'biome': 'Bank', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_enemy', 'mob': 'ShopMimic'}],
    },
    "Hand Hook": {
        "id": 0x0230, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "HandHook",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BoilerRoom'}],
    },
    "Killing Deck": {
        "id": 0x0231, "region": "Checks", "type": "blueprint_enemy",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "ThrowingCards",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BoilerRoom'}],
    },
    "Staphy Outfit": {
        "id": 0x0232, "region": "Checks", "type": "skin",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "Staphy", "rarity": "Rare",
        "sources": [{'biome': 'Shipwreck', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'blueprint_enemy', 'mob': 'BoilerRoom'}],
    },
    "Homunculus Rune": {"id": 0x0233, "region": "Throne", "type": "rune", "dlc": "", "item": "HomKey"},
    "Maria Outfit": {
        "id": 0x0234, "region": "Checks", "type": "skin",
        "dlc": "Purple", "min_bc": 0, "item": "Maria",
        "sources": [{'biome': 'PurpleGarden', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Risk of Rain Outfit": {
        "id": 0x0235, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "RiskOfRain",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Slay the Spire Outfit": {
        "id": 0x0236, "region": "Checks", "type": "skin",
        "dlc": "", "min_bc": 0, "item": "SlayTheSpire",
        "sources": [{'biome': 'StiltVillage', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Bobby Head": {
        "id": 0x0237, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BobbyFlame",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Black Hole": {
        "id": 0x0238, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlackHole",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "White Black Hole": {
        "id": 0x0239, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 2, "item": "BlackHoleWhite",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 2, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Red Black Hole": {
        "id": 0x023A, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlackHoleRed",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Blue Black Hole": {
        "id": 0x023B, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlackHoleBlue",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Green Black Hole": {
        "id": 0x023C, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlackHoleGreen",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Bitter": {
        "id": 0x023D, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "Bitter",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Sanguine Vortex": {
        "id": 0x023E, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "VortexBadSeed",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Abyssal Vortex": {
        "id": 0x023F, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "VortexAndSea",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Dark Vortex": {
        "id": 0x0240, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "VortexFoundry",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Guillain Head": {
        "id": 0x0241, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "Guillain",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Fisherman's Hood": {
        "id": 0x0242, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "Pecheur",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Leghugger Head": {
        "id": 0x0243, "region": "Checks", "type": "head",
        "dlc": "TheQueenAndTheSea", "min_bc": 0, "item": "StaphyHead",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheQueenAndTheSea', 'type': 'item_no_blueprint'}],
    },
    "Flawless Head": { #todo might need DLCs
        "id": 0x0244, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "Flawless",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Cell Head": {
        "id": 0x0245, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "CellHead",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Toxic Blob": {
        "id": 0x0246, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlobbyFlame",
        "sources": [{'biome': 'SewerShort', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Glitchy Head": {
        "id": 0x0247, "region": "Checks", "type": "head",
        "dlc": "RiseOfTheGiant", "min_bc": 5, "item": "GlitchyHead",
        "sources": [{'biome': 'Observatory', 'min_bc': 5, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Mushroom Boi Cap": {
        "id": 0x0248, "region": "Checks", "type": "head",
        "dlc": "TheBadSeed", "min_bc": 0, "item": "MushroomBoi",
        "sources": [{'biome': 'Greenhouse', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'item_no_blueprint'}],
    },
    "Hordes Zero Hood": {
        "id": 0x0249, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "HordesZeroHood",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Magma Blob": {
        "id": 0x024A, "region": "Checks", "type": "head",
        "dlc": "RiseOfTheGiant", "min_bc": 0, "item": "BlobbyFlameMagma",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'RiseOfTheGiant', 'type': 'item_no_blueprint'}],
    },
    "Malaise Blob": {
        "id": 0x024B, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlobbyFlameMalaise",
        "sources": [{'biome': 'Crypt', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Spatial Anomaly": {
        "id": 0x024C, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "GlitchyHeadDeepSpace",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Menacing Anomaly": {
        "id": 0x024D, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "GlitchyHeadRed",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Black Blowtorch": {
        "id": 0x024E, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlowTorchBlack",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}, {'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'item_no_blueprint'}, {'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Gold Blowtorch": {
        "id": 0x024F, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlowTorchGold",
        "sources": [{'biome': 'Throne', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Bright Red Blowtorch": {
        "id": 0x0250, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 0, "item": "BlowTorchRed",
        "sources": [{'biome': 'Bridge', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}, {'biome': 'SwampHeart', 'min_bc': 0, 'max_bc': 5, 'dlc': 'TheBadSeed', 'type': 'item_no_blueprint'}, {'biome': 'DeathArena', 'min_bc': 0, 'max_bc': 5, 'dlc': 'Purple', 'type': 'item_no_blueprint'}],
    },
    "Boss Cell Head": {
        "id": 0x0251, "region": "Checks", "type": "head",
        "dlc": "", "min_bc": 5, "item": "BossCellHead",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 5, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Gold Reserves V": {
        "id": 0x0252, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "Money5",
        "sources": [{'biome': 'SewerDepths', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Merchandise Categories": {
        "id": 0x0253, "region": "Checks", "type": "blueprint_floor",
        "dlc": "", "min_bc": 0, "item": "ShopCategories",
        "sources": [{'biome': 'Cemetery', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'blueprint_floor'}],
    },
    "Shatter": {
        "id": 0x0254, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Shatter",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Toxin Lover": {
        "id": 0x0255, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_ToxinLover",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
    "Firestarter": {
        "id": 0x0256, "region": "Checks", "type": "item_no_blueprint",
        "dlc": "", "min_bc": 0, "item": "ASP_Firestarter",
        "sources": [{'biome': 'PrisonStart', 'min_bc': 0, 'max_bc': 5, 'dlc': '', 'type': 'item_no_blueprint'}],
    },
}

def location_id(name: str) -> int:
    return BASE_ID + LOCATION_TABLE[name]["id"]

def get_locations_for_dlcs(enabled_dlcs: Set[str], disabled_types: Set[str]) -> Dict[str, dict]:
    return {n: d for n, d in LOCATION_TABLE.items() if (d["dlc"] == "" or d["dlc"] in enabled_dlcs) and not d["type"] in disabled_types}

def get_valid_locations(enabled_dlcs, disabled_types, bc_level, created_locations):
    valid_locations = {}

    for loc_name, loc_data in LOCATION_TABLE.items():

        if loc_name not in created_locations:
            continue
        dlc = loc_data.get("dlc")
        if dlc and dlc not in enabled_dlcs:
            continue

        loc_type = loc_data.get("type")
        if loc_type in disabled_types:
            continue

        valid_locations[loc_name] = loc_data

    return valid_locations

def _assert_no_duplicate_ids() -> None:
    seen: Dict[int, str] = {}
    for name, data in LOCATION_TABLE.items():
        oid = data["id"]
        if oid in seen: raise ValueError(f"Duplicate ID 0x{oid:04X}: '{seen[oid]}' and '{name}'")
        seen[oid] = name
_assert_no_duplicate_ids()
