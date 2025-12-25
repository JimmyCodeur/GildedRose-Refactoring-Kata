# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from gilded_rose import GildedRose, Item


def build_items():
    return [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]


def parse_days(argv) -> int:
    days = 2
    if len(argv) > 1:
        days = int(argv[1]) + 1
    return days


def print_day(day: int, items) -> None:
    print("-------- day %s --------" % day)
    print("name, sellIn, quality")
    for item in items:
        print(item)
    print("")


def main() -> None:
    print("OMGHAI!")
    items = build_items()
    days = parse_days(sys.argv)

    for day in range(days):
        print_day(day, items)
        GildedRose(items).update_quality()


if __name__ == "__main__":
    main()
