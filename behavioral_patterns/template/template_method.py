from abc import ABC, abstractmethod

class Order(ABC):
    """Абстрактний шаблон замовлення"""

    def __init__(self, extras=None):
        self.extras = extras or []
        self.take_order()
        self.prepare_ingredients()
        self.cook()
        self.add_extras()
        self.serve()

    def take_order(self):
        print(f"\nВи замовили: {self.__class__.__name__} з {', '.join(self.extras) if self.extras else 'нічим'}")

    def prepare_ingredients(self):
        print("Підготовка інгредієнтів: борошно, яйця, цукор, молоко, сіль...")

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass

    def serve(self):
        print(f"Ваш {self.__class__.__name__.lower()} готовий!\n")


class Croissant(Order):
    def cook(self):
        print("Випікаємо круасан 15 хвилин при 180 градусів")

    def add_extras(self):
        allowed = {"шоколад", "джем", "горіхи", "сир"}
        valid = [x for x in self.extras if x in allowed]
        print("Додаємо:", ", ".join(valid) if valid else "нічого")


class Cake(Order):
    def cook(self):
        print("Випікаємо торт 40 хвилин при 175 градусів")

    def add_extras(self):
        allowed = {"крем", "фрукти", "ягоди", "шоколад", "горіхи"}
        valid = [x for x in self.extras if x in allowed]
        print("Додаємо:", ", ".join(valid) if valid else "нічого")


class Donut(Order):
    def cook(self):
        print("Смажимо пончик у фритюрі 5 хвилин при 180 градусів")

    def add_extras(self):
        allowed = {"присипка", "шоколад", "ванільний крем"}
        valid = [x for x in self.extras if x in allowed]
        print("Додаємо:", ", ".join(valid) if valid else "нічого")


if __name__ == "__main__":
    orders = [
        Croissant(["шоколад", "горіхи"]),
        Cake(["ягоди", "крем"]),
        Donut(["присипка"])
    ]
