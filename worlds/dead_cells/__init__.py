"""Dead Cells - Archipelago world.

Thin orchestration only. The game's content lives in data/*.json, the logic grammar in
logic/requirements.py, and each generation step in its own small module:

    data/       JSON files + typed loader        (what exists)
    regions.py  region graph                      (where it is)
    locations.py  which locations exist           (what can be checked)
    items.py    item pool                         (what can be found)
    rules.py    access rules                      (what is required)
"""
from typing import Any

from BaseClasses import ItemClassification, Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from . import items, regions, rules
from .base_classes import DeadCellsItem
from .constants import DLC_OPTIONS, ITEM_BASE_ID, LOCATION_BASE_ID, MAX_BC, TRAP_WEIGHT_OPTIONS, world_version
from .data import game_data
from .options import DeadCellsOptions, dead_cells_option_groups

_DATA = game_data()


class DeadCellsWebWorld(WebWorld):
    theme = "dirt"
    tutorials = [Tutorial("Setup Guide", "A guide to setting up Dead Cells Archipelago.", "English",
                          "setup_en.md", "setup/en", ["Max_lamenace572"])]
    option_groups = dead_cells_option_groups


class DeadCellsWorld(World):
    """Dead Cells randomizer: blueprints, runes, upgrades, skins and aspects spread across the biomes."""

    game = "Dead Cells"
    web = DeadCellsWebWorld()
    options_dataclass = DeadCellsOptions
    options: DeadCellsOptions

    data = _DATA
    item_name_to_id = {n: ITEM_BASE_ID + i.id for n, i in _DATA.items.items()}
    location_name_to_id = {n: LOCATION_BASE_ID + l.id for n, l in _DATA.locations.items()}
    item_name_groups = {k: set(v) for k, v in _DATA.groups["items"].items()}
    location_name_groups = {**{k: set(v) for k, v in _DATA.groups["locations"].items()},
                            "Enemy Kills": set(_DATA.enemy_names.values())}

    enabled_dlcs: set[str]
    biome_regions: dict
    location_gates: dict
    room_map: dict
    depth_regions: dict
    pruned_locations: list
    entrance_requirements: list

    # ── generation steps ─────────────────────────────────────────────────────
    def generate_early(self) -> None:
        if self.options.boss_cells.value == MAX_BC and not self.options.dlc_rise_of_the_giant:
            raise OptionError(f"Dead Cells ({self.player_name}): the 5 Boss Cells goal is only reachable through "
                              "the Astrolab, so it requires the 'Rise of the Giant' DLC. Enable it or lower Boss Cells.")
        self.enabled_dlcs = {dlc for opt, dlc in DLC_OPTIONS.items() if getattr(self.options, opt)}
        for it in self.data.items.values():                 #"include ... = off" -> player just starts with them
            if items.is_precollected(self, it) and (not it.dlc or it.dlc in self.enabled_dlcs):
                self.multiworld.push_precollected(self.create_item(it.name))

    def create_regions(self) -> None:
        regions.create_regions(self)

    def create_items(self) -> None:
        items.create_items(self)

    def set_rules(self) -> None:
        rules.set_rules(self)

    # ── items ────────────────────────────────────────────────────────────────
    def create_item(self, name: str) -> DeadCellsItem:
        return DeadCellsItem(name, ItemClassification[self.data.items[name].classification],
                             self.item_name_to_id[name], self.player)

    def get_filler_item_name(self) -> str:
        pool = [n for n, i in self.data.items.items() if i.filler_pool and not i.dlc]
        return self.random.choice(pool)

    def write_spoiler_header(self, spoiler_handle) -> None:
        moved = {a: b for a, b in self.room_map.items() if a != b}
        if moved:
            spoiler_handle.write(f"\nRoom randomizer ({self.options.room_randomizer.current_key}) for {self.player_name}:\n")
            for original, actual in moved.items():
                spoiler_handle.write(f"  doors to {self.data.ap_name(original)} lead to {self.data.ap_name(actual)}\n")

    # ── client ───────────────────────────────────────────────────────────────
    def _room_slot_data(self) -> dict[str, Any]:
        """For the mod. `map`: whenever the game would load biome D (through any door), load map[D].
        `doors`: the same, door by door (from biome, biome it used to lead to, biome it leads to now)."""
        if self.options.room_randomizer.current_key == "off":
            return {"mode": "off", "map": {}, "doors": []}
        return {
            "mode": self.options.room_randomizer.current_key,
            "map": dict(self.room_map),
            "doors": [{"from": t.src, "original": t.dst, "to": self.room_map.get(t.dst, t.dst)}
                      for t in self.data.transitions if t.src in self.biome_regions and t.dst in self.biome_regions],
        }

    def fill_slot_data(self) -> dict[str, Any]:
        o = self.options
        return {
            "apworld_version":              world_version(),
            "boss_cells":                   o.boss_cells.value,
            "damage_link":                  bool(o.damage_link.value),
            "damage_link_group":            str(o.damage_link_group.value),
            "death_link":                   o.death_link.value,
            "death_link_aspect":            bool(o.death_link_aspect.value),
            "death_link_group":             str(o.death_link_group.value),
            "death_trap":                   bool(o.death_trap.value),
            "death_trap_link":              bool(o.death_trap_link.value),
            "dlc_rise_of_the_giant":        bool(o.dlc_rise_of_the_giant.value),
            "dlc_the_bad_seed":             bool(o.dlc_the_bad_seed.value),
            "dlc_fatal_falls":              bool(o.dlc_fatal_falls.value),
            "dlc_the_queen_and_the_sea":    bool(o.dlc_the_queen_and_the_sea.value),
            "dlc_return_to_castlevania":    bool(o.dlc_return_to_castlevania.value),
            "enemy_sanity":                 bool(o.enemy_sanity.value),
            "exclude_distillery":           bool(o.exclude_distillery.value),
            "flawless_scroll":              bool(o.flawless_scroll.value),
            "health_link":                  bool(o.health_link.value),
            "health_link_group":            str(o.health_link_group.value),
            "health_curse_link":            bool(o.health_curse_link.value),
            "include_cosmetics":            bool(o.include_cosmetics.value),
            "include_aspects":              bool(o.include_aspects.value),
            "include_base_weapons":         bool(o.include_base_weapons.value),
            "room_randomizer":              self._room_slot_data(),
            "trap_percentage":              o.trap_percentage.value,
            "trap_weights":                 {opt: getattr(o, opt).value for opt, name in TRAP_WEIGHT_OPTIONS.items()},
            "trap_link":                    bool(o.trap_link.value),
            "trap_link_group":              str(o.trap_link_group.value),
            "respawn_up":                   bool(o.respawn_up.value),
        }
