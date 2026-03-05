from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import DeadCellsAPWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    # Runes
    "Vine Rune": 1,
    "Teleport Rune": 2,
    "Ram Rune": 3,
    "Explore Rune": 4,
    "Spider Rune": 5,
    "Homunculus Rune": 6,
    # Upgrades
    "Dash": 7, # For Richter Mode
    "High Jump": 8, # For Richter Mode
    "Flask 1": 9,
    "Flask 2": 10,
    "Flask 3": 11,
    "Flask 4": 12,
    "Reserve 1": 13,
    "Reserve 2": 14,
    "Reserve 3": 15,
    "Reserve 4": 16,
    "Reserve 5": 17,
    "Recycling 1": 18,
    "Recycling 2": 19,
    "Random Melee Weapon": 20,
    "Random Starter Bow": 21,
    "Random Starter Shield": 22,
    "Restock": 23,
    "Specialist's Showroom": 24,
    "Hunter's Mirror": 25,
    "Merchandise Categories": 26,
    "Advanced Forge": 27,
    "Recycling Tubes": 28,
    "Backpack": 29,
    "Training Room": 30,
    # Default Melee Weapons
    "Assassin's Dagger Blueprint": 31,
    "Broadsword Blueprint": 32,
    "Cursed Sword Blueprint": 33,
    "Impaler Blueprint": 34,
    "Symmetrical Lance Blueprint": 35,
    "Spartan Sandals Blueprint": 36,
    "Flint Blueprint": 37,
    "Tentacle Blueprint": 38,
    "Vorpan Blueprint": 39,
    "Crowbar Blueprint": 40,
    "Iron Staff Blueprint": 41,
    "Machete and Pistol Blueprint": 42,
    "Hard Light Sword Blueprint": 43,
    "Blood Sword Blueprint": 44,
    "Panchaku Blueprint": 45,
    "Baseball Bat Blueprint" : 46,
    "King Scepter Blueprint": 47,
    "Starfury Blueprint": 48,
    # Chance Melee Weapons (Base Game)
    "Spite Sword Blueprint": 49,
    "Shovel Blueprint": 50,
    "Sadist's Stiletto Blueprint": 51,
    "Shrapnel Axes Blueprint": 52,
    "Seismic Strike Blueprint": 53,
    "War Spear Blueprint":54

}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class DeadCellsLocation(Location):
    game = "Dead Cells"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: DeadCellsAPWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: DeadCellsAPWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    prison_quarter = world.get_region("Prison Quarter")
    condemned_promenade = world.get_region("Condemned Promenade")
    toxic_sewer = world.get_region("Toxic Sewer")
    prison_depths = world.get_region("Prison Depths")
    corrupt_prison = world.get_region("Corrupt Prison")
    ramparts = world.get_region("Ramparts")
    ancient_sewer = world.get_region("Ancient Sewer")
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
    dereliict_distillery = world.get_region("Derelict Distillery")
    throne_room = world.get_region("Throne Room")

    #
    prison_quarter_locations = get_location_names_with_ids(
        ["Broadsword Blueprint",
         "Crowbar Blueprint",
         "Machete and Pistol Blueprint",
         "Hard Light Sword Blueprint",
         "Pure Nail Blueprint",
         "Bone Blueprint",
         "Panchaku Blueprint",
         "Baseball Bat Blueprint",
         "King Scepter Blueprint",
         "Starfury Blueprint",
         ])
    prison_quarter.add_locations(prison_quarter_locations, DeadCellsLocation)




def create_events(world: DeadCellsAPWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)