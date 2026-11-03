"""Room randomizer: invariants of each mode, door logic, determinism, slot data, full generation."""
from BaseClasses import CollectionState
from Fill import distribute_items_restrictive
from test.general import gen_steps, setup_multiworld
from worlds.AutoWorld import AutoWorldRegister, call_all

from ..data import game_data
from ..logic.room_rando import boss_biome_tiers, normal_group, retarget
from . import DeadCellsTestBase

ALL_DLC = dict(dlc_rise_of_the_giant=1, dlc_the_bad_seed=1, dlc_fatal_falls=1,
               dlc_the_queen_and_the_sea=1, dlc_return_to_castlevania=1)
CONFIGS = {"no_dlc": {}, "all_dlc_bc5": {**ALL_DLC, "boss_cells": 5}, "bc0": {"boss_cells": 0},
           "bad_seed_enemy_sanity": {"dlc_the_bad_seed": 1, "enemy_sanity": 1}}
MODES = ("depth", "tier", "chaotic")
ALWAYS_FIXED = ("PrisonStart", "Bank", "BossRush", "Challenge")


class TestRoomRandomizer(DeadCellsTestBase):
    def _world(self, mode, opts=None, seed=1):
        mw = setup_multiworld(AutoWorldRegister.world_types["Dead Cells"], gen_steps, seed,
                              {**(opts or {}), "room_randomizer": mode})
        return mw, mw.worlds[1]

    def test_off_is_vanilla(self):
        mw, world = self._world("off")
        self.assertTrue(all(k == v for k, v in world.room_map.items()))
        self.assertEqual(world.fill_slot_data()["room_randomizer"], {"mode": "off", "map": {}, "doors": []})

    def test_mode_invariants(self):
        data = game_data()
        tiers = boss_biome_tiers(data)
        kind = lambda b: ("boss", tiers[b]) if b in tiers else ("group", normal_group(data, b, tiers))
        for mode in MODES:
            for label, opts in CONFIGS.items():
                for seed in (1, 2, 3):
                    with self.subTest(mode=mode, config=label, seed=seed):
                        _, world = self._world(mode, opts, seed)
                        m = world.room_map
                        self.assertEqual(sorted(m), sorted(m.values()))             #a permutation
                        self.assertTrue(all(m[b] == b for b in ALWAYS_FIXED if b in m))
                        for a, b in m.items():
                            if a == b:
                                continue                                            #fixed or left in place
                            if mode == "depth":
                                self.assertEqual(data.biomes[a].depth, data.biomes[b].depth)
                            elif mode == "tier":
                                self.assertEqual(kind(a), kind(b))

    def test_every_mode_generates_fills_and_is_beatable(self):
        for mode in MODES:
            for label, opts in CONFIGS.items():
                with self.subTest(mode=mode, config=label):
                    mw, _ = self._world(mode, opts, 5)
                    state = CollectionState(mw)
                    for item in mw.itempool:
                        state.collect(item, prevent_sweep=True)
                    state.sweep_for_advancements()
                    self.assertEqual([l.name for l in mw.get_locations(1) if not l.can_reach(state)], [])
                    distribute_items_restrictive(mw)
                    call_all(mw, "post_fill")
                    self.assertTrue(mw.can_beat_game(CollectionState(mw)))

    def test_same_seed_same_rooms(self):
        for mode in MODES:
            self.assertEqual(self._world(mode, ALL_DLC, 9)[1].room_map, self._world(mode, ALL_DLC, 9)[1].room_map)
        self.assertNotEqual(self._world("chaotic", ALL_DLC, 9)[1].room_map, self._world("chaotic", ALL_DLC, 10)[1].room_map)

    def test_door_logic_follows_the_new_destination(self):
        d = game_data()
        #abilities of the door stay, the unlock of the old destination is replaced by the unlock of the new one
        self.assertEqual(retarget([["Tumulus"]], "Tumulus", "StiltVillage", d), [["StiltVillage"]])
        self.assertEqual(retarget([["TeleportKey", "Greenhouse"]], "Greenhouse", "PrisonCourtyard", d), [["TeleportKey"]])
        self.assertEqual(retarget([[]], "PrisonCourtyard", "Ossuary", d), [["Ossuary"]])
        self.assertEqual(retarget([["LadderKey"], ["WallJumpKey"]], "SewerShort", "Greenhouse", d),
                         [["LadderKey", "Greenhouse"], ["WallJumpKey", "Greenhouse"]])
        self.assertEqual(retarget([["Tumulus"]], "Tumulus", "Tumulus", d), [["Tumulus"]])
        #requirements live on the doors: Boss Cells never follow a biome
        self.assertEqual(retarget([["Progressive Stem Cell:5", "Astrolab"]], "Astrolab", "Castle", d),
                         [["Progressive Stem Cell:5", "Castle"]])
        self.assertEqual(retarget([["Tumulus"]], "Tumulus", "Astrolab", d), [["Astrolab"]])
        #physical obstacles of the exit never change, whatever the destination
        self.assertEqual(retarget([["LadderKey", "Greenhouse"], ["WallJumpKey", "Greenhouse"]], "Greenhouse", "Ossuary", d),
                         [["LadderKey", "Ossuary"], ["WallJumpKey", "Ossuary"]])

    def test_distillery_is_entered_from_the_tier_2_boss_levels(self):
        d = game_data()
        self.assertEqual({t.src for t in d.transitions if t.dst == "Distillery"}, {"Giant", "TopClockTower", "GardenerStage"})
        self.assertEqual([t.dst for t in d.transitions if t.src == "Distillery"], ["Throne"])
        self.assertFalse([t for t in d.transitions if t.src == "Throne" and t.dst == "Distillery"])

    def test_room_tiers_are_not_the_boss_rush_tiers(self):
        d = game_data()
        self.assertEqual(boss_biome_tiers(d)["DookuArena"], 3)                  #tier 3 for the room randomizer
        self.assertEqual(boss_biome_tiers(d)["Observatory"], 3)                 #the Collector counts here
        self.assertIn("Boss_DookuBeast", d.boss_tiers["2"])                     #while the boss rush counts Dracula twice (normal T2; Beast T3)
        self.assertIn("Boss_DookuBeast", d.boss_tiers["3"])
        self.assertNotIn("Boss_Collector", [b for t in d.boss_tiers.values() for b in t])
        self.assertEqual(len([b for b in d.boss_tiers["3"] if b.startswith("Boss_Amazon")]), 1)  #count only one Amazon

    def test_astrolab_distillery_observatory_can_move(self):
        d = game_data()
        self.assertEqual({b for b, t in boss_biome_tiers(d).items() if t == 2}, {"TopClockTower", "Giant", "GardenerStage"})
        moved = set()
        for mode in ("tier", "chaotic"):
            for seed in range(1, 25):
                _, world = self._world(mode, {**ALL_DLC, "boss_cells": 5}, seed)
                moved |= {b for b in ("Astrolab", "Observatory", "Distillery") if world.room_map[b] != b}
        self.assertEqual(moved, {"Astrolab", "Observatory", "Distillery"})

    def test_slot_data_for_the_mod(self):
        _, world = self._world("tier", ALL_DLC, 4)
        rr = world.fill_slot_data()["room_randomizer"]
        self.assertEqual(rr["mode"], "tier")
        self.assertEqual(rr["map"], world.room_map)
        self.assertTrue(rr["doors"])
        for door in rr["doors"]:                            #doors and map tell the same story
            self.assertEqual(door["to"], rr["map"][door["original"]])
        self.assertIn({"from": "PrisonStart", "original": "PrisonCourtyard", "to": rr["map"]["PrisonCourtyard"]}, rr["doors"])

    def test_bank_depth_follows_the_position_not_the_content(self):
        _, world = self._world("chaotic", ALL_DLC, 6)
        data = world.data
        for depth, contents in world.depth_regions.items():
            positions = [b for b in world.biome_regions if data.biomes[b].depth == depth]
            self.assertEqual(sorted(contents), sorted(world.room_map[p] for p in positions))
