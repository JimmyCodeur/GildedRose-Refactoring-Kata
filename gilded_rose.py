# -*- coding: utf-8 -*-
from __future__ import annotations

AGED_BRIE = "Aged Brie"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


def _is_aged_brie(item) -> bool:
    return item.name == AGED_BRIE


def _is_backstage(item) -> bool:
    return item.name == BACKSTAGE


def _is_sulfuras(item) -> bool:
    return item.name == SULFURAS


def _increase_quality(item, amount: int = 1) -> None:
    item.quality += amount
    if item.quality > 50:
        item.quality = 50


def _decrease_quality(item, amount: int = 1) -> None:
    item.quality -= amount
    if item.quality < 0:
        item.quality = 0


class GildedRose:
    def __init__(self, items: list["Item"]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item: "Item") -> None:
        self._update_quality_before_sell_in(item)
        self._decrement_sell_in(item)
        self._apply_expired_rules(item)

    def _update_quality_before_sell_in(self, item: "Item") -> None:
        if self._is_regular_item(item):
            self._update_regular_item(item)
            return

        if _is_aged_brie(item):
            self._update_aged_brie(item)
            return

        if _is_backstage(item):
            self._update_backstage(item)
            return

        # Sulfuras : nothing to do (quality & sell_in don't change)
        return

    def _decrement_sell_in(self, item: "Item") -> None:
        if not _is_sulfuras(item):
            item.sell_in -= 1

    def _apply_expired_rules(self, item: "Item") -> None:
        if item.sell_in >= 0:
            return

        if _is_aged_brie(item):
            _increase_quality(item, 1)
            return

        if _is_backstage(item):
            item.quality = 0
            return

        if self._is_regular_item(item):
            _decrease_quality(item, 1)
            return

        # Sulfuras : nothing to do
        return

    def _is_regular_item(self, item: "Item") -> bool:
        return (not _is_aged_brie(item)) and (not _is_backstage(item)) and (not _is_sulfuras(item))

    def _update_regular_item(self, item: "Item") -> None:
        _decrease_quality(item, 1)

    def _update_aged_brie(self, item: "Item") -> None:
        _increase_quality(item, 1)

    def _update_backstage(self, item: "Item") -> None:
        _increase_quality(item, 1)
        if item.sell_in < 11:
            _increase_quality(item, 1)
        if item.sell_in < 6:
            _increase_quality(item, 1)


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
