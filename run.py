from item import Item
from gilded_rose import GildedRose


def main():
    items = [
        Item("+5 Dexterity Vest", 10, 20),
        Item("Aged Brie", 2, 0),
        Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Item("Conjured Mana Cake", 3, 6),
    ]

    GildedRose.update_quality(items)

    for it in items:
        print(f"{it.name:40} sell_in={it.sell_in:3}  quality={it.quality:3}")


if __name__ == "__main__":
    main()
