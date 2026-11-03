"""Full generation under many option combos (regions, pool size, fill, beatability, pruning, traps, bank depth)."""
from collections import Counter

from BaseClasses import CollectionState
from Fill import distribute_items_restrictive
from Options import OptionError
from test.general import gen_steps, setup_multiworld
from worlds.AutoWorld import AutoWorldRegister, call_all

from ..data import game_data
from . import DeadCellsTestBase

ALL_DLC = dict(dlc_rise_of_the_giant=1, dlc_the_bad_seed=1, dlc_fatal_falls=1,
               dlc_the_queen_and_the_sea=1, dlc_return_to_castlevania=1)
NO_TRAPS = {f"trap_weight_{t}": 0 for t in ("curse", "elite", "gold", "weapon_break", "reverse", "challenge")}

CASES = {
    "default": {},
    "bc0": {"boss_cells": 0},
    "bc5": {"boss_cells": 5, "dlc_rise_of_the_giant": 1},
    "only_castlevania": {"dlc_return_to_castlevania": 1},
    "all_dlc_bc2": ALL_DLC,
    "all_dlc_bc5": {**ALL_DLC, "boss_cells": 5},
    "no_cosmetics": {"include_cosmetics": 0},
    "no_aspects_no_base": {"include_aspects": 0, "include_base_weapons": 0, "include_base_mutations": 0},
    "no_distillery": {"exclude_distillery": 1, "boss_cells": 3},
    "all_traps": {"trap_percentage": 100},
    "enemy_sanity": {"enemy_sanity": 1},
    "enemy_sanity_bc0": {"enemy_sanity": 1, "boss_cells": 0},
    "enemy_sanity_all_dlc": {**ALL_DLC, "enemy_sanity": 1},
    "enemy_sanity_bc5_no_cosmetics": {**ALL_DLC, "boss_cells": 5, "enemy_sanity": 1, "include_cosmetics": 0, "exclude_distillery": 1},
    "kitchen_sink": {**ALL_DLC, "boss_cells": 5, "include_cosmetics": 0, "include_aspects": 0, "exclude_distillery": 1},
}


class TestGeneration(DeadCellsTestBase):
    def _world(self, opts):
        return setup_multiworld(AutoWorldRegister.world_types["Dead Cells"], gen_steps, 1, opts)

    def _all_state(self, mw):
        state = CollectionState(mw)
        for item in mw.itempool:
            state.collect(item, prevent_sweep=True)
        state.sweep_for_advancements()
        return state

    def test_pool_matches_locations_fill_succeeds_and_game_is_beatable(self):
        for label, opts in CASES.items():
            with self.subTest(label):
                mw = self._world(opts)
                self.assertEqual(len(mw.itempool), len(mw.get_unfilled_locations(1)))
                distribute_items_restrictive(mw)
                call_all(mw, "post_fill")
                self.assertTrue(mw.can_beat_game(CollectionState(mw)))

    def test_every_location_is_reachable_in_every_config(self):
        """Impossible locations are pruned at creation, so nothing may stay unreachable."""
        for label, opts in CASES.items():
            with self.subTest(label):
                mw = self._world(opts)
                state = self._all_state(mw)
                self.assertEqual([l.name for l in mw.get_locations(1) if not l.can_reach(state)], [])

    def test_bc5_requires_rise_of_the_giant(self):
        with self.assertRaises(OptionError):
            self._world({"boss_cells": 5})
        self._world({"boss_cells": 5, "dlc_rise_of_the_giant": 1})

    def test_unreachable_boss_rush_and_counters_are_pruned(self):
        names = lambda opts: set(self._world(opts).worlds[1].pruned_locations)  # noqa: E731
        self.assertEqual(names({}), {"Wish", "Triumph Outfit", "Giant Comb", "Spatial Anomaly"})
        self.assertEqual(names(ALL_DLC), set())
        #boss rush 3&4 needs two tier 2 bosses. Dracula counts as tier 2 (phase 1) AND tier 3 (phase 2),
        #so Castlevania alone is enough; the Collector is not a boss rush boss.
        self.assertNotIn("Wish", names({"dlc_fatal_falls": 1}))
        self.assertNotIn("Wish", names({"dlc_rise_of_the_giant": 1}))
        self.assertNotIn("Wish", names({"dlc_return_to_castlevania": 1}))
        self.assertNotIn("Triumph Outfit", names({"dlc_return_to_castlevania": 1}))

    def test_bank_depth_only_constrains_the_bank_source(self):
        mw = self._world({})
        world = mw.worlds[1]
        state = CollectionState(mw)
        for name in ("Vine Rune", "The Specialist's Showroom"):
            state.collect(world.create_item(name), prevent_sweep=True)
        #Lightning Bolt drops from PrisonRoof (depth 2); the old rule also demanded a depth-4 biome.
        self.assertFalse(any(state.can_reach_region(r, 1) for r in world.depth_regions[4]))
        self.assertTrue(mw.get_location("Lightning Bolt", 1).can_reach(state))
        #and the Bank alternative is gated by depth, separately from the classic sources.
        bank = [g for g in world.location_gates["Lightning Bolt"] if "Bank" in g.biomes]
        self.assertTrue(bank and all(g.depths for g in bank))

    def test_trap_weights(self):
        only_curse = {**NO_TRAPS, "trap_weight_curse": 10, "trap_percentage": 40}
        traps = Counter(i.name for i in self._world(only_curse).itempool if i.trap)
        self.assertEqual(set(traps), {"Curse Trap"})
        self.assertGreater(traps["Curse Trap"], 50)
        self.assertEqual(sum(1 for i in self._world({**NO_TRAPS, "trap_percentage": 40}).itempool if i.trap), 0)
        mixed = Counter(i.name for i in self._world({**NO_TRAPS, "trap_weight_gold": 9, "trap_weight_elite": 1,
                                                    "trap_percentage": 60}).itempool if i.trap)
        self.assertGreater(mixed["Gold Trap"], mixed["Elite Trap"] * 3)

    def _enemy_locations(self, opts):
        mw = self._world({"enemy_sanity": 1, **opts})
        names = set(mw.worlds[1].data.enemy_names.values())
        return {l.name for l in mw.get_locations(1)} & names

    def test_enemy_sanity_is_off_by_default(self):
        mw = self._world({})
        self.assertEqual(self._enemy_locations({}) - {l.name for l in self._world({"enemy_sanity": 1}).get_locations(1)}, set())
        self.assertFalse({l.name for l in mw.get_locations(1)} & set(mw.worlds[1].data.enemy_names.values()))

    def test_enemy_sanity_never_adds_bosses(self):
        from ..data import game_data
        from ..data.enemies import boss_mobs
        import json, pkgutil
        bosses = boss_mobs(json.loads(pkgutil.get_data("worlds.dead_cells.data", "tracker.json")))
        self.assertEqual(len(bosses), 14)
        data = game_data()
        self.assertFalse(bosses & set(data.enemy_names))                        #no enemy location for a boss
        self.assertFalse({f"Kill {b}" for b in bosses} & set(data.locations))

    def test_enemy_sanity_follows_dlc_and_boss_cells(self):
        base, full = self._enemy_locations({}), self._enemy_locations({**ALL_DLC, "boss_cells": 5})
        self.assertEqual(len(full), 83)                                         #every non-boss enemy of mobs.json
        self.assertTrue(base < full)                                            #DLC-only enemies appear with their DLC
        self.assertIn("Kill Medusa", full - base)
        self.assertLess(len(self._enemy_locations({"boss_cells": 0})), len(base))   # BC-gated enemies need the BC

    def test_enemy_display_names(self):
        data = game_data()
        self.assertEqual(data.enemy_names["Fly"], "Kill Buzzcutter")
        self.assertEqual(data.enemy_names["LancerPurple"], "Kill Armor Knight")
        self.assertIn("Kill Armor Knight", self._enemy_locations({**ALL_DLC, "boss_cells": 5}))

    def test_slot_data_keys(self):
        data = self._world({}).worlds[1].fill_slot_data()
        for key in ("boss_cells", "death_link", "respawn_up", "apworld_version", "trap_weights"):
            self.assertIn(key, data)
        self.assertEqual(set(data["trap_weights"]), {"Curse Trap", "Elite Trap", "Gold Trap",
                                                     "Weapon Break Trap", "Reverse Trap", "Challenge Trap"})
