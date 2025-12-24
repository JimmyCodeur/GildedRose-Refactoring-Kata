# -*- coding: utf-8 -*-

def _is_aged_brie(item) -> bool:
    return item.name == "Aged Brie"


def _is_backstage(item) -> bool:
    return item.name == "Backstage passes to a TAFKAL80ETC concert"


def _is_sulfuras(item) -> bool:
    return item.name == "Sulfuras, Hand of Ragnaros"


def _increase_quality(item, amount: int = 1) -> None:
    item.quality += amount
    if item.quality > 50:
        item.quality = 50


def _decrease_quality(item, amount: int = 1) -> None:
    item.quality -= amount
    if item.quality < 0:
        item.quality = 0


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if (not _is_aged_brie(item)) and (not _is_backstage(item)):
                if item.quality > 0:
                    if not _is_sulfuras(item):
                        _decrease_quality(item, 1)
            else:
                if item.quality < 50:
                    _increase_quality(item, 1)

                    if _is_backstage(item):
                        if item.sell_in < 11:
                            if item.quality < 50:
                                _increase_quality(item, 1)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                _increase_quality(item, 1)

            if not _is_sulfuras(item):
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if not _is_aged_brie(item):
                    if not _is_backstage(item):
                        if item.quality > 0:
                            if not _is_sulfuras(item):
                                _decrease_quality(item, 1)
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        _increase_quality(item, 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
