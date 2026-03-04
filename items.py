class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Normal(Item):
    def update_quality(self):
        if self.quality > 0:
            self.quality -= 1
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality -= 1


class AgedBrie(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1


class Sulfuras(Item):
    def update_quality(self):
        pass


class Backstage(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11 and self.quality < 50:
                self.quality += 1
            if self.sell_in < 6 and self.quality < 50:
                self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0


class Conjured(Item):
    def update_quality(self):
        if self.quality > 0:
            self.quality -= 2
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality -= 2
