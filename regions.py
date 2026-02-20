from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import DeadCellsAPWorld


def create_and_connect_regions(world: DeadCellsAPWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: DeadCellsAPWorld) -> None:
    #First Stage
    prison_quarter = Region("Prisoners' Quarters", world.player, world.multiworld)
    
    #Second Stages
    condemned_promenade = Region("Promenade of the Condemned", world.player, world.multiworld)
    toxic_sewer = Region("Toxic Sewers", world.player, world.multiworld)
    
    #Optional Stages
    prison_depths = Region("Prison Depths", world.player, world.multiworld)
    corrupt_prison = Region("Corrupted Prison", world.player, world.multiworld)

    #Third Stages
    ramparts = Region("Ramparts", world.player, world.multiworld)
    ancient_sewer = Region("Ancient Sewers", world.player, world.multiworld)
    ossuary = Region("Ossuary", world.player, world.multiworld)

    #First Bosses
    black_bridge = Region("Black Bridge", world.player, world.multiworld)
    insuff_crypt = Region("Insufferable Crypt", world.player, world.multiworld)

    # Fourth Stages
    stilt_village = Region("Stilt Village", world.player, world.multiworld)
    slumber_sanctuary = Region("Slumbering Sanctuary", world.player, world.multiworld)
    graveyard = Region("Graveyard", world.player, world.multiworld)

    regions = [prison_quarter,condemned_promenade,toxic_sewer,prison_depths,corrupt_prison,ramparts,ancient_sewer,ossuary]

    # Adds regions to multiworld
    world.multiworld.regions += regions


def connect_regions(world: DeadCellsAPWorld) -> None:
    # Grabs regions from world
    prison_quarter = world.get_region("Prisoners' Quarter")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
    overworld.exits.append(overworld_to_bottom_right_room)

    # You can then connect the Entrance to the target region.
    overworld_to_bottom_right_room.connect(bottom_right_room)

    # An even easier way is to use the region.connect helper.
    overworld.connect(right_room, "Overworld to Right Room")
    right_room.connect(final_boss_room, "Right Room to Final Boss Room")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        overworld.connect(top_middle_room, "Overworld to Top Middle Room")