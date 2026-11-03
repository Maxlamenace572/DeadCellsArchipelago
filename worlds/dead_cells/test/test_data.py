"""Pure data checks: no generation needed. These replace the 'typo in a hand-written list' class of bugs."""
import dataclasses
import unittest

from ..data import game_data
from ..data.validate import validate


class TestData(unittest.TestCase):
    def test_data_files_are_consistent(self):
        self.assertEqual(validate(), [])

    def test_validator_catches_mistakes(self):
        d = game_data()
        broken = dataclasses.replace(d, rules={**d.rules, "No Such Location": "Vine Rune", "Ripper": "Spidr Rune"})
        errors = "\n".join(validate(broken))
        self.assertIn("No Such Location", errors)
        self.assertIn("Spidr Rune", errors)

    def test_ids_are_stable_and_unique(self):
        d = game_data()
        self.assertEqual(len({i.id for i in d.items.values()}), len(d.items))
        self.assertEqual(len({l.id for l in d.locations.values()}), len(d.locations))

    def test_every_boss_event_has_its_item(self):
        d = game_data()
        self.assertEqual(len(d.event_items), 11)
        self.assertTrue(all(name in d.items for name in d.event_items))

    def test_enemy_ids_are_frozen_and_complete(self):
        d = game_data()
        enemy_locs = [l for l in d.locations.values() if l.type == "enemy"]
        self.assertEqual(len(enemy_locs), len(d.enemy_names))
        self.assertTrue(all(l.id >= 1000 for l in enemy_locs))
