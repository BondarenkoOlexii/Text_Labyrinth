class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return f"Піца з тістом: {self.dough}, соусом: {self.sauce}, начинки: {', '.join(self.topping)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_topping(self, topping):
        self.pizza.topping.append(topping)
        return self

    def build(self):
        return self.pizza



class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_margherita(self):
        return (self.builder
                .set_dough("тонке")
                .set_sauce("томатний")
                .add_topping("моцарела")
                .add_topping("базилік")
                .build())

    def make_pepperoni(self):
        return (self.builder
                .set_dough("товсте")
                .set_sauce("томатний")
                .add_topping("моцарела")
                .add_topping("пепероні")
                .build())


if __name__ == "__main__":
    builder = PizzaBuilder()
    director = PizzaDirector(builder)

    margherita = director.make_margherita()
    pepperoni = director.make_pepperoni()

    print(margherita)
    print(pepperoni)
