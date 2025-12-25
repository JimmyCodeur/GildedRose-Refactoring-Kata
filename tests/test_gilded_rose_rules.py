# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


def update_days(items, days: int):
    app = GildedRose(items)
    for _ in range(days):
        app.update_quality()

class TestGildedRoseBusinessRules(unittest.TestCase):

    # --- Quality bounds ---

    def test_quality_is_never_negative(self):
        items = [Item("foo", 5, 0)]
        update_days(items, 1)
        self.assertGreaterEqual(items[0].quality, 0)

        items = [Item("foo", 0, 0)]
        update_days(items, 2)
        self.assertGreaterEqual(items[0].quality, 0)

    def test_quality_never_exceeds_50_for_normal_items(self):
        items = [Item("foo", 5, 50)]
        update_days(items, 1)
        self.assertLessEqual(items[0].quality, 50)

    def test_quality_never_exceeds_50_for_aged_brie(self):
        items = [Item("Aged Brie", 5, 50)]
        update_days(items, 1)
        self.assertLessEqual(items[0].quality, 50)

    # --- Sulfuras ---

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        update_days(items, 5)
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 80)

    # --- Aged Brie ---

    def test_aged_brie_increases_in_quality_over_time(self):
        items = [Item("Aged Brie", 2, 0)]
        update_days(items, 1)
        self.assertEqual(items[0].quality, 1)

    def test_aged_brie_increases_faster_after_expiration(self):
        items = [Item("Aged Brie", 0, 0)]
        update_days(items, 1)
        self.assertEqual(items[0].quality, 2)

    # --- Backstage passes ---

    def test_backstage_increases_by_1_when_more_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        update_days(items, 1)
        self.assertEqual(items[0].quality, 21)

    def test_backstage_increases_by_2_when_6_to_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        update_days(items, 1)
        self.assertEqual(items[0].quality, 22)

    def test_backstage_increases_by_3_when_0_to_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        update_days(items, 1)
        self.assertEqual(items[0].quality, 23)

    def test_backstage_quality_drops_to_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        update_days(items, 1)
        self.assertEqual(items[0].quality, 0)

    # --- Conjured (not part of current legacy behavior) ---

    @unittest.skip("Conjured items not implemented in current legacy behavior (Golden Master).")
    def test_conjured_degrades_twice_as_fast_if_present(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        update_days(items, 1)
        self.assertEqual(items[0].quality, 4)


if __name__ == "__main__":
    unittest.main()
