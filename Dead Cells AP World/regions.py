from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

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
    dereliict_distillery = Region("Derelict Distillery", world.player, world.multiworld)

    # Third Bosses
    throne_room = Region("Throne Room", world.player, world.multiworld)

    # Seventh Stage
    astrolab = Region("Astrolab", world.player, world.multiworld)

    # Special Stages
    bank = Region("The Bank", world.player, world.multiworld)

    regions = [
        prison_quarter,
        condemned_promenade,toxic_sewer,
        prison_depths,corrupt_prison,
        ramparts,ancient_sewer,ossuary,
        black_bridge, insuff_crypt,
        stilt_village, slumber_sanctuary, graveyard,
        clock_tower, forgotten_sepulcher,
        clock_room,
        high_peak_castle, dereliict_distillery,
        throne_room,
        astrolab,
        bank]

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
    astrolab = world.get_region("Astrolab")
    bank = world.get_region("The Bank")


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
    stilt_village.connect(clock_tower, "Clock Tower to Clock Village")