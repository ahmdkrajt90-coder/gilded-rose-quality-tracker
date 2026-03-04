class GildedRose:
    """Inventory rules for the Gilded Rose kata with Conjured support."""

    SULFURAS = "Sulfuras, Hand of Ragnaros"
    AGED_BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    CONJURED_TOKEN = "Conjured"

    @classmethod
    def update_quality(cls, items):
        for item in items:
            if cls._is_sulfuras(item):
                continue

            if cls._is_brie(item):
                cls._increase(item, 1)
            elif cls._is_backstage(item):
                cls._update_backstage(item)
            else:
                cls._decrease(item, cls._degrade_step(item))

            item.sell_in -= 1
            cls._handle_expired(item)
            cls._clamp_quality(item)

        return items

    # Helpers
    @classmethod
    def _is_sulfuras(cls, item):
        return item.name == cls.SULFURAS

    @classmethod
    def _is_brie(cls, item):
        return item.name == cls.AGED_BRIE

    @classmethod
    def _is_backstage(cls, item):
        return item.name == cls.BACKSTAGE

    @classmethod
    def _is_conjured(cls, item):
        return cls.CONJURED_TOKEN in item.name

    @classmethod
    def _degrade_step(cls, item):
        return 2 if cls._is_conjured(item) else 1

    @classmethod
    def _increase(cls, item, amount):
        item.quality += amount

    @classmethod
    def _decrease(cls, item, amount):
        item.quality -= amount

    @classmethod
    def _update_backstage(cls, item):
        if item.sell_in <= 5:
            cls._increase(item, 3)
        elif item.sell_in <= 10:
            cls._increase(item, 2)
        else:
            cls._increase(item, 1)

    @classmethod
    def _handle_expired(cls, item):
        if item.sell_in >= 0:
            return

        if cls._is_brie(item):
            cls._increase(item, 1)
        elif cls._is_backstage(item):
            item.quality = 0
        else:
            cls._decrease(item, cls._degrade_step(item))

    @classmethod
    def _clamp_quality(cls, item):
        if cls._is_sulfuras(item):
            return
        item.quality = max(0, min(50, item.quality))
