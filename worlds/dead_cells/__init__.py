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
    get_progression_items, item_id, PROG, USFL, FILR, TRAP,
)
from .locations import (
    LOCATION_TABLE, BASE_ID as LOC_BASE_ID,
    get_locations_for_bc, location_id,
)
from .regions import create_regions, REGION_DLC
from .rules import set_rules as apply_location_rules
from .base_classes import DeadCellsItem


# ─────────────────────────────────────────────────────────────────────────────
# Items that are always base-game weapons (no blueprint required)
# Excluded when include_base_weapons is off
# ─────────────────────────────────────────────────────────────────────────────
BASE_WEAPONS = {
    "QuickSword", "DualDaggers", "StunMace",
    "DualBow", "ThrowingKnife", "LightningWhip", "ThrowingTorch", "Freeze",
    "Shield", "GreedShield",
    "ExtraHeal",
    "FastGrenade", "IceBomb",
    "StandardTurret", "RootTrap",
}

BASE_META = {#"Flask1" in prog
    "Flask2", "Flask3", "Flask4",
    "Money1", "Money2", "Money3", "Money4",
    "RandomBow", "RandomShield", "RandomCC",
    "Recycling1", "Recycling2",
    "ShopRerolls", "PokebombUnlock", "MirrorUnlock", "BackpackUnlock",
}

BASE_PERKS = {
    "P_CDR_Kill", "P_DmgKill", "P_DmgRevenge",
    "P_DeployedDmg", "P_NoMobAround", "P_CDR_Distance",
    "P_CDR_Parry", "P_DmgParry", "P_HealOnKill",
    "P_Yolo", "P_CDR_Crit",
}

BASE_ASPECTS = {
    "ASP_Shatter", "ASP_ToxinLover", "ASP_Firestarter",
}

BASE_SKINS = {
    "PrisonerGOG", "PrisonerFrench", "PrisonerRetro", "Snowman", "SantaKLOS",
}

BASE_HEADS = {
    "BlackHoleViolet", "VortexHelloDarkness", "BlowTorch",
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

    def _item_enabled(self, item_id: str) -> bool:
        """Return True if this item should be included in the pool."""
        data = ITEM_TABLE[item_id]
        _, classification, dlc = data

        # Filter by DLC
        if dlc and dlc not in self.enabled_dlcs:
            return False

        # Filter cosmetics if option is off
        if not self.options.include_cosmetics:
            cat = _ITEM_CATEGORY.get(item_id, "")
            if cat in COSMETIC_CATEGORIES:
                return False

        # Filter base weapons if option is off
        if not self.options.include_base_weapons:
            if item_id in BASE_WEAPONS:
                return False

        return True

    # ── AP World interface ────────────────────────────────────────────────────

    def generate_early(self) -> None:
        """Called before multiworld generation. Resolve options."""
        self.enabled_dlcs = self._build_enabled_dlcs()

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

    def create_items(self) -> None:
        """
        Build and fill the item pool.

        Strategy:
        1. Count available locations (respecting DLC + BC filters).
        2. Always place all progression items (runes).
        3. Fill remaining slots with useful items, then fillers, then traps.
        """
        bc = self.options.boss_cells.value
        trap_pct = self.options.trap_percentage.value / 100.0

        # Active locations (determines pool size)
        active_locs = get_locations_for_bc(self.enabled_dlcs, bc)
        pool_size = len(active_locs)

        # DEBUG
        print("Beholder4 in pool:", "Blueprint_Beholder4" in active_locs)
        print("BossRune4 in pool:", "BSC_BossRune4" in active_locs)
        print("BossRune5 in pool:", "BSC_BossRune5" in active_locs)
        prog_items = get_progression_items(self.enabled_dlcs)
        useful_items = [
            name for name, data in get_items_for_dlcs(self.enabled_dlcs).items()
            if data[1] == USFL and self._item_enabled(name)
        ]
        print(f"[DC DEBUG] pool_size (locations): {pool_size}")
        print(f"[DC DEBUG] prog_items: {len(prog_items)}")
        print(f"[DC DEBUG] useful_items: {len(useful_items)}")
        print(f"[DC DEBUG] prog + useful: {len(prog_items) + len(useful_items)}")
        remaining = pool_size - len(prog_items) - len(useful_items)
        print(f"[DC DEBUG] remaining for fillers/traps: {remaining}")
        filler_pool = [name for name, data in get_filler_items(self.enabled_dlcs).items() if self._item_enabled(name)]
        print(f"[DC DEBUG] filler_pool size: {len(filler_pool)}")
        # END DEBUG

        items_to_place: List[DeadCellsItem] = []
        
        reachable_item_names = {
            data["item"]
            for data in active_locs.values()
            if data.get("item") is not None
        }

        # ── Progression items (always included) ──────────────────────────────
        prog_items = get_progression_items(self.enabled_dlcs)
        for name in prog_items:
            # BossRuneN is in the pool only if N <= bsc_level
            if name.startswith("BossRune"):
                n = int(name[-1])
                if n > bc:
                    continue
            items_to_place.append(self.create_item(name))

        # ── Useful items ──────────────────────────────────────────────────────
        useful_items = [
            name for name, data in get_items_for_dlcs(self.enabled_dlcs).items()
            if data[1] == USFL and self._item_enabled(name) and name in reachable_item_names
        ]
        for name in useful_items:
            items_to_place.append(self.create_item(name))
            
        # ── Base items ───────────────────────────────────────────────────────
        for name in BASE_WEAPONS:
            items_to_place.append(self.create_item(name))
        
        for name in BASE_META:
            items_to_place.append(self.create_item(name))
                
        for name in BASE_PERKS:
            items_to_place.append(self.create_item(name))
        
        for name in BASE_ASPECTS:
            items_to_place.append(self.create_item(name))
        
        for name in BASE_SKINS:
            items_to_place.append(self.create_item(name))
        
        for name in BASE_HEADS:
            items_to_place.append(self.create_item(name))

        # ── Trim or pad to pool_size ─────────────────────────────────────────
        remaining = pool_size - len(items_to_place)

        if remaining < 0:
            # More items than locations: demote excess useful items to filler
            # Keep all progression, trim useful from the end
            prog_count = len(prog_items)
            trimmed_useful = items_to_place[prog_count:prog_count + (len(useful_items) + remaining)]
            items_to_place = items_to_place[:prog_count] + trimmed_useful

        elif remaining > 0:
            # Fill remaining slots with traps + fillers
            trap_count = int(remaining * trap_pct)
            filler_count = remaining - trap_count

            trap_pool = list(get_trap_items().keys())
            filler_pool = [
                name for name, data in get_filler_items(self.enabled_dlcs).items()
                if self._item_enabled(name)
            ]

            # Cycle through traps
            for i in range(trap_count):
                trap_name = trap_pool[i % len(trap_pool)]
                items_to_place.append(self.create_item(trap_name))

            # Cycle through fillers
            for i in range(filler_count):
                filler_name = filler_pool[i % len(filler_pool)]
                items_to_place.append(self.create_item(filler_name))

        self.multiworld.itempool += items_to_place

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
