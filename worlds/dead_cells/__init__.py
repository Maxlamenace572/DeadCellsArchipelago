"""
Dead Cells - Archipelago World
__init__.py

Main world class. Orchestrates item pool construction, location creation,
region wiring, win condition, and slot data generation.
"""

from typing import Dict, List, Set, Any
from BaseClasses import Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .options import DeadCellsOptions
from .items import (
    ITEM_TABLE, BASE_ID as ITEM_BASE_ID,
    DLC_RISE_OF_GIANT, DLC_BAD_SEED, DLC_FATAL_FALLS,
    DLC_QUEEN_AND_SEA, DLC_PURPLE,
    get_items_for_dlcs, get_filler_items, get_trap_items,
    get_progression_items, item_id, PROG, USFL, FILR, TRAP, is_cosmetic
)
from .locations import (
    LOCATION_TABLE, BASE_ID as LOC_BASE_ID,
    get_valid_locations, location_id,
)
from .regions import create_regions, REGION_DLC
from .rules import set_rules as apply_location_rules
from .base_classes import DeadCellsItem
from BaseClasses import LocationProgressType

# ─────────────────────────────────────────────────────────────────────────────
# Items that are always base-game weapons (no blueprint required)
# Excluded when include_base_weapons is off
# ─────────────────────────────────────────────────────────────────────────────
# ─────────────────────────────────────
# BASE LOADOUT ITEMS
# ─────────────────────────────────────


BASE_WEAPONS = {
    "Balanced Blade",
    "Twin Daggers",
    "Nutcracker",

    "Multiple-nocks Bow",
    "Throwing Knife",
    "Electric Whip",
    "Firebrands",
    "Ice Blast",

    "Cudgel",
    "Greed Shield",

    "Tonic",

    "Infantry Grenade",
    "Ice Grenade",

    "Sinew Slicer",
    "Wolf Trap",
}


# ─────────────────────────────────────
# BASE META UPGRADES
# ─────────────────────────────────────

BASE_META = {
    "Progressive Flask",
    "Progressive Gold Reserves",
    "Random Starter Bow",
    "Random Starter Shield",
    "Random Melee Weapon",
    "Progressive Recycling",
    "Restock",
    "Specialist's Showroom",
    "Hunter's Mirror",
    "Backpack",
}


# ─────────────────────────────────────
# BASE MUTATIONS
# ─────────────────────────────────────

BASE_PERKS = {
    "Killer Instinct",
    "Combo",
    "Vengeance",
    "Support",
    "Tranquility",
    "Velocity",
    "Counterattack",
    "Spite",
    "Frenzy",
    "Ygdar Orus Li Ox",
    "Critical Recovery",
}


# ─────────────────────────────────────
# BASE OUTFITS
# ─────────────────────────────────────

BASE_SKINS = {
    "GOG Outfit",
    "French Outfit",
    "Retro Outfit",
    "Snowman Outfit",
    "Santa Outfit",
}


# ─────────────────────────────────────
# BASE HEAD COSMETICS
# ─────────────────────────────────────

BASE_HEADS = {
    "Violet Black Hole",
    "Hello Darkness Vortex",
    "Blowtorch",
}

# Cosmetic categories excluded when include_cosmetics is off
COSMETIC_CATEGORIES = {"Skin", "Head"}


# ─────────────────────────────────────────────────────────────────────────────
# Web world (documentation / hints for the AP website)
# ─────────────────────────────────────────────────────────────────────────────
class DeadCellsWebWorld(WebWorld):
    theme = "dirt"
    tutorials = [
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to setting up Dead Cells Archipelago.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["You"],
        )
    ]


# ─────────────────────────────────────────────────────────────────────────────
# Main World class
# ─────────────────────────────────────────────────────────────────────────────
class DeadCellsWorld(World):
    """
    Dead Cells randomizer for Archipelago.
    Randomizes weapons, skills, runes, upgrades, skins and aspects
    across biomes, with full DLC support and Boss Cell difficulty scaling.
    """

    game = "Dead Cells"
    options_dataclass = DeadCellsOptions
    options: DeadCellsOptions
    web = DeadCellsWebWorld()

    item_name_to_id = {
        name: ITEM_BASE_ID + data[0]
        for name, data in ITEM_TABLE.items()
    }
    location_name_to_id = {
        name: LOC_BASE_ID + data["id"]
        for name, data in LOCATION_TABLE.items()
    }

    # Populated in generate_early, used throughout
    enabled_dlcs: Set[str] = set()
    cosmetics: set[str] = set()

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _build_enabled_dlcs(self) -> Set[str]:
        """Resolve which DLCs are active based on options."""
        dlcs = set()
        if self.options.dlc_rise_of_the_giant:
            dlcs.add(DLC_RISE_OF_GIANT)
        if self.options.dlc_the_bad_seed:
            dlcs.add(DLC_BAD_SEED)
        if self.options.dlc_fatal_falls:
            dlcs.add(DLC_FATAL_FALLS)
        if self.options.dlc_the_queen_and_the_sea:
            dlcs.add(DLC_QUEEN_AND_SEA)
        if self.options.dlc_return_to_castlevania:
            dlcs.add(DLC_PURPLE)
        return dlcs


    def _item_enabled(self, item_name: str) -> bool:
        data = ITEM_TABLE[item_name]
        _, classification, dlc = data

    # DLC filter
        if dlc and dlc not in self.enabled_dlcs:
            return False

    # Cosmetic filter
        if not self.options.include_cosmetics.value:
            cat = _ITEM_CATEGORY.get(item_name)
            if cat in COSMETIC_CATEGORIES:
                 return False

    # Base weapon filter
        if not self.options.include_base_weapons.value:
            if item_name in BASE_WEAPONS:
                return False
            
    # Base mutation filter
        if not self.options.include_base_mutations.value:
            if item_name in BASE_PERKS:
                return False

        return True

    # ── AP World interface ────────────────────────────────────────────────────

    def generate_early(self) -> None:
        self.enabled_dlcs = self._build_enabled_dlcs()

        if not self.options.include_base_weapons.value:
            for name in BASE_WEAPONS:
                self.multiworld.push_precollected(self.create_item(name))

        if not self.options.include_base_mutations.value:
            for name in BASE_PERKS:
                self.multiworld.push_precollected(self.create_item(name))

    def create_regions(self) -> None:
        """Create all regions and wire transitions."""
        create_regions(self)

    def create_item(self, name: str) -> DeadCellsItem:
        """Create a single AP item by name."""
        data = ITEM_TABLE[name]
        return DeadCellsItem(
            name,
            data[1],  # classification
            self.item_name_to_id[name],
            self.player,
        )

    def create_items(self):
        multiworld = self.multiworld
        player = self.player
        enabled_dlcs = self.enabled_dlcs

        # ─────────────────────────────────────
        # 1. Gather item groups
        # ─────────────────────────────────────
        progression_items = get_progression_items(enabled_dlcs)   # dict[name, (offset, class, dlc)]
        useful_items = get_items_for_dlcs(enabled_dlcs)           # dict[name, (offset, class, dlc)]
        filler_items = get_filler_items(enabled_dlcs)             # list[str]
        trap_items = get_trap_items()                             # list[str]

    # Remove progression items from useful pool
        useful_items = [name for name in useful_items if name not in progression_items]

    # ─────────────────────────────────────
    # 2. Remove cosmetics if option disabled
    # ─────────────────────────────────────
        if not self.options.include_cosmetics.value:
            def not_cosmetic(name: str) -> bool:
                return not is_cosmetic(name)

        # Keep Cultist Outfit even if cosmetics are disabled, because it is progression
            progression_items = {
                name: data
                for name, data in progression_items.items()
                if not_cosmetic(name) or name == "Cultist Outfit"
        }

            useful_items = [
               name for name in useful_items
               if not_cosmetic(name) or name == "Cultist Outfit"
        ]

            filler_items = [
                name for name in filler_items
                if not_cosmetic(name) or name == "Cultist Outfit"
        ]

    # ─────────────────────────────────────
    # 3. Count locations
    # ─────────────────────────────────────
        total_locations = len(self.created_locations)

    # ─────────────────────────────────────
    # 4. Build progression pool
    # ─────────────────────────────────────
        itempool: list[str] = []

        progression_list = list(progression_items.keys())

    # Remove progressive items that need custom counts
        custom_progressives = {
            "Progressive Stem Cell",
            "Progressive Flask",
            "Progressive Gold Reserves",
    }
        progression_list = [name for name in progression_list if name not in custom_progressives]

    # Progressive Stem Cells: count based on boss_cells option
        max_bc = self.options.boss_cells.value
        itempool += ["Progressive Stem Cell"] * max_bc

    # Progressive Flask: always 4 total
        itempool += ["Progressive Flask"] * 4

    # Progressive Gold Reserves: always 5 total
        itempool += ["Progressive Gold Reserves"] * 5

    # Add remaining progression items once each
        itempool += progression_list

    # Safety: make sure Cultist Outfit exists if enabled in this DLC set
        if (
            "Cultist Outfit" in ITEM_TABLE
            and (ITEM_TABLE["Cultist Outfit"][2] == "" or ITEM_TABLE["Cultist Outfit"][2] in enabled_dlcs)
            and "Cultist Outfit" not in itempool
        ):
            itempool.append("Cultist Outfit")

    # Calculate remaining slots
        remaining_slots = total_locations - len(itempool)

        if remaining_slots < 0:
           
            itempool = itempool[:total_locations]
            remaining_slots = 0

        # ─────────────────────────────────────
        # 5. Add useful items (one copy each)
        # ─────────────────────────────────────
        useful_list = list(useful_items)

            # Safety: remove any progression items that somehow remained
        useful_list = [name for name in useful_list if name not in progression_items]

            # Optional shuffle so order is not predictable
        import random
        random.shuffle(useful_list)

            # Only add one copy of each useful item, up to remaining slots
        useful_to_add = useful_list[:remaining_slots]
        itempool += useful_to_add
        remaining_slots -= len(useful_to_add)

    # ─────────────────────────────────────
    # 6. Add traps
    # ─────────────────────────────────────
        trap_percentage = self.options.trap_percentage.value / 100.0
        trap_count = min(len(trap_items), int(total_locations * trap_percentage))

        if trap_count > 0:
            random.shuffle(trap_items)
            itempool += trap_items[:trap_count]
            remaining_slots -= trap_count

    # ─────────────────────────────────────
    # 7. Fill the rest with filler
    # ─────────────────────────────────────
        if remaining_slots > 0:
            if filler_items:
                random.shuffle(filler_items)
                filler_cycle = (
                    filler_items * ((remaining_slots // len(filler_items)) + 1)
                )[:remaining_slots]
                itempool += filler_cycle
            else:
                print("[DC DEBUG] No filler items available; leaving remaining slots empty.")

    # ─────────────────────────────────────
    # 8. Safety trim if pool overflowed
    # ─────────────────────────────────────
        if len(itempool) > total_locations:
            overflow = len(itempool) - total_locations
            print(f"[DC DEBUG] Trimming {overflow} excess items.")

            for _ in range(overflow):
                # Prefer removing filler first
                for i in range(len(itempool) - 1, -1, -1):
                    if itempool[i] in filler_items:
                        itempool.pop(i)
                        break
                else:
                    # Then remove useful
                    for i in range(len(itempool) - 1, -1, -1):
                        if itempool[i] in useful_items:
                            itempool.pop(i)
                            break
                    else:
                    # Last resort: remove last non-progression duplicate
                        itempool.pop()

    # ─────────────────────────────────────
    # 9. Convert to AP items
    # ─────────────────────────────────────
        final_items = []

        for name in itempool:
            if name not in ITEM_TABLE:
                raise KeyError(f"[DC ERROR] Item '{name}' is missing from ITEM_TABLE")

            item_data = ITEM_TABLE[name]
            final_items.append(
                DeadCellsItem(
                    name,
                    item_data[1],   # classification
                    item_id(name),
                player,
            )
        )

        multiworld.itempool += final_items


    def set_rules(self) -> None:
        """
        Additional rules beyond region entrances.
        Region-level rules are already set in create_regions().
        Here we apply location-level rules and the completion condition.
        """
        # Location-level rules (blueprints, BSC gates, skin counts, etc.)
        apply_location_rules(self)

        # Victory condition: reach the End region
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.can_reach("End", "Region", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        """
        Return slot data sent to the game client on connection.
        The Dead Cells mod uses this to configure the session.
        """
        multiworld = self.multiworld
        player = self.player

        early_locations = [
            loc for loc in multiworld.get_locations(player)
            if getattr(loc, "min_bc", 0) == 0
        ]

        progression_items = [
            item for item in multiworld.itempool
            if item.name in [
            "LadderKey",
            "WallJumpKey",
            "BreakableGroundKey",
            "HomKey",
            "ProgBossRune"
        ]
    ]  

        for item, loc in zip(progression_items, early_locations):
            if not loc.item:
                loc.place_locked_item(item)

        return {
            "boss_cells":                self.options.boss_cells.value,
            "death_link":                bool(self.options.death_link.value),
            "dlc_rise_of_the_giant":     bool(self.options.dlc_rise_of_the_giant.value),
            "dlc_the_bad_seed":          bool(self.options.dlc_the_bad_seed.value),
            "dlc_fatal_falls":           bool(self.options.dlc_fatal_falls.value),
            "dlc_the_queen_and_the_sea": bool(self.options.dlc_the_queen_and_the_sea.value),
            "dlc_return_to_castlevania": bool(self.options.dlc_return_to_castlevania.value),
            "include_cosmetics":         bool(self.options.include_cosmetics.value),
            "include_base_weapons":      bool(self.options.include_base_weapons.value),
            "trap_percentage":           self.options.trap_percentage.value,
        }

    def get_filler_item_name(self) -> str:
        """
        Called by AP when it needs an extra filler item (e.g. for item links).
        Returns a random filler item name valid for this world's DLC set.
        """
        fillers = list(get_filler_items(self.enabled_dlcs).keys())
        return self.random.choice(fillers)


# ─────────────────────────────────────────────────────────────────────────────
# Category cache — built once at import time from items.json
# Used by _item_enabled() to filter cosmetics
# ─────────────────────────────────────────────────────────────────────────────
import json as _json
import os as _os

_ITEMS_JSON_PATH = _os.path.join(_os.path.dirname(__file__), "items.json")
try:
    with open(_ITEMS_JSON_PATH) as _f:
        _raw = _json.load(_f)
    _ITEM_CATEGORY: Dict[str, str] = {k: v["category"] for k, v in _raw.items()}
except FileNotFoundError:
    _ITEM_CATEGORY = {}
