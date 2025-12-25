# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_update_quality_does_not_change_item_name(self):
        items = [Item("foo", 0, 0)]
        app = GildedRose(items)

        app.update_quality()

        self.assertEqual("foo", items[0].name)

if __name__ == '__main__':
    unittest.main()
