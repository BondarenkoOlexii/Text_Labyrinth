from abc import ABC, abstractmethod


class Hero(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

    @abstractmethod
    def stats(self):
        pass

    @abstractmethod
    def items(self):
        pass


class Drow_Ranger(Hero):
    def accept(self, visitor):
        visitor.visit_Drow_Ranger(self)

    def stats(self):
        return {'hp': 2300, 'dmg': 130, 'hp_regen': 10, 'mana_regen': 3}

    def items(self):
        return ["Dragon Lance", "Hurricane Pike", "Butterfly", "Black King Bar"]


class Axe(Hero):
    def accept(self, visitor):
        visitor.visit_Axe(self)

    def stats(self):
        return {'hp': 3400, 'dmg': 95, 'hp_regen': 18, 'mana_regen': 1.5}

    def items(self):
        return ["Blink Dagger", "Blade Mail", "Heart of Tarrasque", "Phase Boots"]


class Leshrak(Hero):
    def accept(self, visitor):
        visitor.visit_Leshrak(self)

    def stats(self):
        return {'hp': 2700, 'dmg': 115, 'hp_regen': 7.5, 'mana_regen': 6.5}

    def items(self):
        return ["Bottle", "Blood Stone", "Kaya and Sange", "Octarine Core", "Eternal Shroud"]


class Lion(Hero):
    def accept(self, visitor):
        visitor.visit_Lion(self)

    def stats(self):
        return {'hp': 2250, 'dmg': 80, 'hp_regen': 5.5, 'mana_regen': 4.5}

    def items(self):
        return ["Blink Dagger", "Aghanim's Scepter"]


class Snapfire(Hero):
    def accept(self, visitor):
        visitor.visit_Snapfire(self)

    def stats(self):
        return {'hp': 2550, 'dmg': 100, 'hp_regen': 6, 'mana_regen': 5}

    def items(self):
        return ["Solar Crest", "Glimmer Cape", "Force Staff"]



class HeroVisitor(ABC):
    @abstractmethod
    def visit_Drow_Ranger(self, hero): pass

    @abstractmethod
    def visit_Axe(self, hero): pass

    @abstractmethod
    def visit_Leshrak(self, hero): pass

    @abstractmethod
    def visit_Lion(self, hero): pass

    @abstractmethod
    def visit_Snapfire(self, hero): pass


class ItemsVisitor(HeroVisitor):
    def __init__(self, damage_items, hp_regen_items, hp_items):
        self.damage_items = damage_items
        self.hp_regen_items = hp_regen_items
        self.hp_items = hp_items

    def apply_items(self, hero):
        stats = hero.stats()
        for item in hero.items():
            if item in self.damage_items:
                stats['dmg'] += self.damage_items[item]
            if item in self.hp_regen_items:
                stats['hp_regen'] += self.hp_regen_items[item]
            if item in self.hp_items:
                stats['hp'] += self.hp_items[item]
        return stats

    def visit_Drow_Ranger(self, hero):
        updated_stats = self.apply_items(hero)
        print(f"Drow Ranger items: {hero.items()}, updated stats: {updated_stats}")

    def visit_Axe(self, hero):
        updated_stats = self.apply_items(hero)
        print(f"Axe items: {hero.items()}, updated stats: {updated_stats}")

    def visit_Leshrak(self, hero):
        updated_stats = self.apply_items(hero)
        print(f"Leshrak items: {hero.items()}, updated stats: {updated_stats}")

    def visit_Lion(self, hero):
        updated_stats = self.apply_items(hero)
        print(f"Lion items: {hero.items()}, updated stats: {updated_stats}")

    def visit_Snapfire(self, hero):
        updated_stats = self.apply_items(hero)
        print(f"Snapfire items: {hero.items()}, updated stats: {updated_stats}")


if __name__ == "__main__":
    damage_items = {'Butterfly': 50, 'Hurricane Pike': 22, "Aghanim's Scepter": 100}
    hp_regen_items = {'Bottle': 10, 'Kaya and Sange': 25, 'Heart of Tarrasque': 60}
    hp_items = {'Octarine Core': 600, 'Heart of Tarrasque': 500}

    items_visitor = ItemsVisitor(damage_items, hp_regen_items, hp_items)

    heroes = [Drow_Ranger(), Axe(), Leshrak(), Lion(), Snapfire()]
    for hero in heroes:
        hero.accept(items_visitor)
