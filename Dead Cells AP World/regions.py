from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import DeadCellsAPWorld


def create_and_connect_regions(world: DeadCellsAPWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: DeadCellsAPWorld) -> None:
    # First Stage
    prison_quarter = Region("Prisoners' Quarters", world.player, world.multiworld)
    
    # Second Stages
    condemned_promenade = Region("Promenade of the Condemned", world.player, world.multiworld)
    toxic_sewer = Region("Toxic Sewers", world.player, world.multiworld)

    # Optional Stages
    prison_depths = Region("Prison Depths", world.player, world.multiworld)
    corrupt_prison = Region("Corrupted Prison", world.player, world.multiworld)

    # Third Stages
    ramparts = Region("Ramparts", world.player, world.multiworld)
    ancient_sewer = Region("Ancient Sewers", world.player, world.multiworld)
    ossuary = Region("Ossuary", world.player, world.multiworld)

    # First Bosses
    black_bridge = Region("Black Bridge", world.player, world.multiworld)
    insuff_crypt = Region("Insufferable Crypt", world.player, world.multiworld)

    # Fourth Stages
    stilt_village = Region("Stilt Village", world.player, world.multiworld)
    slumber_sanctuary = Region("Slumbering Sanctuary", world.player, world.multiworld)
    graveyard = Region("Graveyard", world.player, world.multiworld)

    # Fifth Stages
    clock_tower = Region("Clock Tower", world.player, world.multiworld)
    forgotten_sepulcher = Region("Forgotten Sepulcher", world.player, world.multiworld)

    # Second Bosses
    clock_room = Region("Clock Room", world.player, world.multiworld)

    # Sixth Stages
    high_peak_castle = Region("High Peak Castle", world.player, world.multiworld)
    derelict_distillery = Region("Derelict Distillery", world.player, world.multiworld)

    # Third Bosses
    throne_room = Region("Throne Room", world.player, world.multiworld)

    regions = [
        prison_quarter,
        condemned_promenade,toxic_sewer,
        prison_depths,corrupt_prison,
        ramparts,ancient_sewer,ossuary,
        black_bridge, insuff_crypt,
        stilt_village, slumber_sanctuary, graveyard,
        clock_tower, forgotten_sepulcher,
        clock_room,
        high_peak_castle, derelict_distillery,
        throne_room]

    # Rise of the Giant DLC Regions
    if world.options.rise_of_the_giant:
        cavern = Region("Cavern", world.player, world.multiworld)
        guardians_haven = Region("Guardians Haven", world.player, world.multiworld)
        astrolab = Region("Astrolab", world.player, world.multiworld)
        observatory = Region("Observatory", world.player, world.multiworld)
        regions.append(cavern)
        regions.append(guardians_haven)
        regions.append(astrolab)
        regions.append(observatory)
    # Bad Seed DLC Regions
    if world.options.bad_seed:
        dilapidated_arboretum = Region("Dilapidated Arboretum", world.player, world.multiworld)
        morass_banished = Region("Morass of the Banished", world.player, world.multiworld)
        nest = Region("Nest", world.player, world.multiworld)
        regions.append(dilapidated_arboretum)
        regions.append(morass_banished)
        regions.append(nest)
    # Fatal Falls DLC Regions
    if world.options.fatal_falls:
        fractured_shrines = Region("Fractured Shrines", world.player, world.multiworld)
        undying_shores = Region("Undying Shores", world.player, world.multiworld)
        mausoleum = Region("Mausoleum", world.player, world.multiworld)
        regions.append(fractured_shrines)
        regions.append(undying_shores)
        regions.append(mausoleum)
    # Queen and the Sea DLC Regions
    if world.options.queen_and_the_sea:
        infested_shipwreck = Region("Infested Shipwreck", world.player, world.multiworld)
        lighthouse = Region("Lighthouse", world.player, world.multiworld)
        the_crown = Region("The Crown", world.player, world.multiworld)
        regions.append(infested_shipwreck)
        regions.append(lighthouse)
        regions.append(the_crown)
    # Return to Castlevania DLC Regions
    if world.options.return_to_castlevania:
        castle_outskirts = Region("Castle Outskirts", world.player, world.multiworld)
        dracula_castle = Region("Dracula Castle", world.player, world.multiworld)
        defiled_necropolis = Region("Defiled Necropolis", world.player, world.multiworld)
        masters_keep = Region("Masters Keep", world.player, world.multiworld)
        regions.append(castle_outskirts)
        regions.append(dracula_castle)
        regions.append(defiled_necropolis)
        regions.append(masters_keep)

    # Adds regions to multiworld
    world.multiworld.regions += regions


def connect_regions(world: DeadCellsAPWorld) -> None:
    # Grabs regions from world
    prison_quarter = world.get_region("Prisoners' Quarter")
    condemned_promenade = world.get_region("Condemned Promenade")
    toxic_sewer = world.get_region("Toxic Sewers")
    prison_depths = world.get_region("Prison Depths")
    corrupt_prison = world.get_region("Corrupted Prison")
    ramparts = world.get_region("Ramparts")
    ancient_sewer = world.get_region("Ancient Sewers")
    ossuary = world.get_region("Ossuary")
    black_bridge = world.get_region("Black Bridge")
    insuff_crypt = world.get_region("Insufferable Crypt")
    stilt_village = world.get_region("Stilt Village")
    slumber_sanctuary = world.get_region("Slumbering Sanctuary")
    graveyard = world.get_region("Graveyard")
    clock_tower = world.get_region("Clock Tower")
    forgotten_sepulcher = world.get_region("Forgotten Sepulcher")
    clock_room = world.get_region("Clock Room")
    high_peak_castle = world.get_region("High Peak Castle")
    derelict_distillery = world.get_region("Derelict Distillery")
    throne_room = world.get_region("Throne Room")
    if world.options.rise_of_the_giant:
        cavern = world.get_region("Cavern")
        guardians_haven = world.get_region("Guardians Haven")
        astrolab = world.get_region("Astrolab")
        observatory = world.get_region("Observatory")
    if world.options.bad_seed:
        dilapidated_arboretum = world.get_region("Dilapidated Arboretum")
        morass_banished = world.get_region("Morass of the Banished")
        nest = world.get_region("Nest")
    if world.options.fatal_falls:
        fractured_shrines = world.get_region("Fractured Shrines")
        undying_shores = world.get_region("Undying Shores")
        mausoleum = world.get_region("Mausoleum")
    if world.options.queen_and_the_sea:
        infested_shipwreck = world.get_region("Infested Shipwreck")
        lighthouse = world.get_region("Lighthouse")
        the_crown = world.get_region("The Crown")
    if world.options.return_to_castlevania:
        castle_outskirts = world.get_region("Castle Outskirts")
        dracula_castle = world.get_region("Dracula Castle")
        defiled_necropolis = world.get_region("Defiled Necropolis")
        masters_keep = world.get_region("Masters Keep")


    # First Stage Connections
    prison_quarter.connect(condemned_promenade, "Prison to Promenade of the Condemned")
    prison_quarter.connect(toxic_sewer, "Prison to Toxic Sewers", lambda state: state.has("Vine Rune", world.player))

    # Second Stage Connections
    condemned_promenade.connect(ramparts, "Promenade of the Condemned to Ramparts")
    condemned_promenade.connect(ossuary, "Promenade of the Condemned to Ossuary", lambda state: state.has("Teleport Rune", world.player))
    condemned_promenade.connect(prison_depths, "Promenade of the Condemned to Prison Depths", lambda state: state.has("Spider Rune", world.player))
    toxic_sewer.connect(ramparts, "Toxic Sewers to Ramparts")
    toxic_sewer.connect(corrupt_prison, "Toxic Sewers to Corrupt Prison", lambda state: state.has("Spider Rune", world.player))
    toxic_sewer.connect(ancient_sewer, "Toxic Sewers to Ancient Sewers", lambda state: state.has("Ram Rune", world.player))

    # Optional Stage Connections
    prison_depths.connect(ossuary, "Prison Depths to Ossuary", lambda state: state.has("Ram Rune", world.player))
    corrupt_prison.connect(ancient_sewer, "Corrupt Prison to Ancient Sewers")

    # Third Stage Connections
    ossuary.connect(black_bridge, "Ossuary to Black Bridge")
    ramparts.connect(black_bridge, "Ramparts to Black Bridge")
    ancient_sewer.connect(insuff_crypt, "Ancient Sewers to Insufferable Crypt")

    # First Boss Stage Connections
    black_bridge.connect(stilt_village, "Black Bridge to Stilt Village")
    black_bridge.connect(slumber_sanctuary, "Black Bridge to Slumbering Sanctuary", lambda state: state.has("Spider Rune", world.player))
    insuff_crypt.connect(slumber_sanctuary, "Insufferable Crypt to Slumbering Sanctuary")
    insuff_crypt.connect(graveyard, "Insufferable Crypt to Graveyard", lambda state: state.has("Spider Rune", world.player))

    # Fourth Stage Connections
    stilt_village.connect(clock_tower, "Stilt Village to Clock Tower")
    stilt_village.connect(forgotten_sepulcher, "Stilt Village to Forgotten Sepulcher", lambda state: state.has("Teleport Rune", world.player))
    slumber_sanctuary.connect(clock_tower, "Slumbering Sanctuary to Clock Tower")
    slumber_sanctuary.connect(forgotten_sepulcher, "Slumbering Sanctuary to Forgotten Sepulcher", lambda state: state.has("Teleport Rune", world.player))

    # Fifth Stage Connections
    clock_tower.connect(clock_room, "Clock Tower to Clock Room")
    forgotten_sepulcher.connect(clock_room, "Forgotten Sepulcher to Clock Room")

    # Second Boss Stage Connections
    clock_room.connect(derelict_distillery, "Clock Room to Derelict Distillery")
    clock_room.connect(high_peak_castle, "Clock Room to High Peak Castle")

    # Sixth Stage Connections
    derelict_distillery.connect(throne_room, "Derelict Distillery to Throne Room")
    high_peak_castle.connect(throne_room, "High Peak Castle to Throne Room")

