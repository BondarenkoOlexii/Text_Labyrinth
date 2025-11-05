from abc import ABC, abstractmethod

# Абстрактна фабрика
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# Конкретні фабрики
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

# Абстрактні продукти
class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self):
        pass

    @abstractmethod
    def cooperate_with(self, collaboration: AbstractProductA):
        pass

# Конкретні продукти для сімейства 1
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "Результат Продукту A1"

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "Результат Продукту B1"

    def cooperate_with(self, collaboration: AbstractProductA):
        result = collaboration.useful_function_a()
        return f"({self.useful_function_b()}) взаємодіє з ({result})"


# Конкретні продукти для сімейства 2
class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "Результат Продукту A2"

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "Результат Продукту B2"

    def cooperate_with(self, collaboration: AbstractProductA):
        result = collaboration.useful_function_a()
        return f"({self.useful_function_b()}) взаємодіє з ({result})"


# Клієнтський код
def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print("Клієнт надав запит на взаємодію з продуктом:")
    print(product_b.cooperate_with(product_a))


if __name__ == "__main__":
    print("Клієнт працює з першою фабрикою:")
    client_code(ConcreteFactory1())
    print("\n" + "="*30 + "\n")

    print("Клієнт працює з другою фабрикою:")
    client_code(ConcreteFactory2())