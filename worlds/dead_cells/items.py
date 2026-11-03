"""Item pool construction. Everything is driven by items.json flags (class, count, start, unlock_for...)."""
from BaseClasses import ItemClassification
from Options import OptionError

from .constants import COSMETIC_CATEGORIES, TRAP_WEIGHT_OPTIONS
from .data import ItemDef


def is_precollected(world, it: ItemDef) -> bool:
    """Items the player simply starts with because the matching 'include ...' option is off."""
    o = world.options
    return ((it.start == "weapon" and not o.include_base_weapons)
            or (it.start == "mutation" and not o.include_base_mutations)
            or (it.cat == "aspect" and not o.include_aspects))


def item_enabled(world, it: ItemDef) -> bool:
    if it.dlc and it.dlc not in world.enabled_dlcs:
        return False
    if it.cat == "event":                                   #locked on its "<boss> Defeat" location
        return False
    if it.unlock_for and it.unlock_for not in world.biome_regions:
        return False                                        #that biome is not part of this seed
    if it.cat in COSMETIC_CATEGORIES and not world.options.include_cosmetics and not it.keep_without_cosmetics:
        return False
    return not is_precollected(world, it)


def _is_progression(it: ItemDef) -> bool:
    return it.classification.startswith("progression")


def create_items(world) -> None:
    mw, player, data, opts = world.multiworld, world.player, world.data, world.options

    #1) boss "<X> Defeated" events are locked on their "<X> Defeat" location
    for item_name, loc_name in data.event_items.items():
        if loc_name in world.location_gates:
            mw.get_location(loc_name, player).place_locked_item(world.create_item(item_name))

    slots = len(mw.get_unfilled_locations(player))
    candidates = [it for it in data.items.values() if item_enabled(world, it)]

    #2) progression (with its copy count), then traps, then everything else
    pool: list[str] = []
    for it in candidates:
        if _is_progression(it):
            copies = getattr(opts, it.count_option).value if it.count_option else it.count
            pool += [it.name] * copies
    if len(pool) > slots:
        raise OptionError(f"Dead Cells ({world.player_name}): {len(pool)} progression items for only {slots} locations.")

    weights = {name: getattr(opts, opt).value for opt, name in TRAP_WEIGHT_OPTIONS.items()}
    traps = [it.name for it in candidates if it.classification == "trap" and weights.get(it.name, 0) > 0]
    if traps:
        n_traps = min(slots - len(pool), int(slots * opts.trap_percentage.value / 100))
        pool += world.random.choices(traps, weights=[weights[t] for t in traps], k=n_traps)

    rest = [it.name for it in candidates if not _is_progression(it) and it.classification != "trap"]
    world.random.shuffle(rest)
    pool += rest[:slots - len(pool)]

    filler = [it.name for it in data.items.values() if it.filler_pool and item_enabled(world, it)]
    while len(pool) < slots:
        pool.append(world.random.choice(filler))

    mw.itempool += [world.create_item(name) for name in pool]
