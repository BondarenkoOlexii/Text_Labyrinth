from abc import ABC, abstractmethod

# Компонент
class Coffee(ABC):
    @abstractmethod
    def cost(self): pass

    @abstractmethod
    def description(self): pass


class SimpleCoffee(Coffee):
    def cost(self):
        return 20

    def description(self):
        return "Проста кава"


#базовий клас для добавок
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee


# Конкретні декоратори (добавки)
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 5

    def description(self):
        return self._coffee.description() + ", молоко"


class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", цукор"


class Caramel(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 7

    def description(self):
        return self._coffee.description() + ", карамель"



if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"{coffee.description()} = {coffee.cost()} грн")

    coffee_milk = Milk(coffee)
    print(f"{coffee_milk.description()} = {coffee_milk.cost()} грн")

    coffee_sugar_milk = Sugar(Milk(coffee))
    print(f"{coffee_sugar_milk.description()} = {coffee_sugar_milk.cost()} грн")

    coffee_full = Caramel(Sugar(Milk(coffee)))
    print(f"{coffee_full.description()} = {coffee_full.cost()} грн")
