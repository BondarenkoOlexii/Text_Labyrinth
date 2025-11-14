from abc import ABC, abstractmethod



class Engine(ABC):
    @abstractmethod
    def info(self): pass
    @abstractmethod
    def price(self): pass


class Body(ABC):
    @abstractmethod
    def info(self): pass
    @abstractmethod
    def price(self): pass





class ElectricEngine(Engine):
    def info(self):
        return "Електродвигун — 250 кВт, без викидів CO₂"
    def price(self):
        return 10000

class ElectricBody(Body):
    def info(self):
        return "Легкий алюмінієвий кузов з аеродинамічним дизайном"
    def price(self):
        return 7000



class GasolineEngine(Engine):
    def info(self):
        return "Бензиновий двигун — 2.0 Turbo, 180 к.с."
    def price(self):
        return 8000

class GasolineBody(Body):
    def info(self):
        return "Кузов зі сталі, класичний дизайн седану"
    def price(self):
        return 6000



class DieselEngine(Engine):
    def info(self):
        return "Дизельний двигун — 2.5 TDI, 160 к.с., економний"
    def price(self):
        return 7000

class DieselBody(Body):
    def info(self):
        return "Посилений кузов для вантажів або позашляховиків"
    def price(self):
        return 6500




class AbstractCarFactory(ABC):
    @abstractmethod
    def create_engine(self): pass

    @abstractmethod
    def create_body(self): pass



class ElectricCarFactory(AbstractCarFactory):
    def create_engine(self):
        return ElectricEngine()
    def create_body(self):
        return ElectricBody()

class GasolineCarFactory(AbstractCarFactory):
    def create_engine(self):
        return GasolineEngine()
    def create_body(self):
        return GasolineBody()

class DieselCarFactory(AbstractCarFactory):
    def create_engine(self):
        return DieselEngine()
    def create_body(self):
        return DieselBody()




def build_car(factory: AbstractCarFactory):
    engine = factory.create_engine()
    body = factory.create_body()
    print("\n--- Збірка авто завершена! ---")
    print(engine.info())
    print(body.info())
    print(f"Загальна ціна авто: {engine.price() + body.price()} $")




if __name__ == "__main__":
    print("Виберіть тип машини:\n1. Електро\n2. Бензин\n3. Дизель")
    choice = input("Ваш вибір: ")

    if choice == "1":
        factory = ElectricCarFactory()
    elif choice == "2":
        factory = GasolineCarFactory()
    elif choice == "3":
        factory = DieselCarFactory()
    else:
        print("Невірний вибір!")
        exit()

    build_car(factory)
