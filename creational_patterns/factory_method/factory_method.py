from abc import ABC, abstractmethod


class Trancport(ABC):
    @abstractmethod
    def deliever(self, packeg:str):
        pass


class Truck(Trancport):
    def deliever(self, packeg:str):
        return(f"Відправлення {packeg} доставлено вантажним автомобілем")

class Ship(Trancport):
    def deliever(self, packeg:str):
        return(f"Відправлення {packeg} доставлено кораблем")

class Plane(Trancport):
    def deliever(self, packeg:str):
        return (f"Відправлення {packeg} доставлено літаком")


class Logistics(ABC):
    def plan_of_deliever(self, packeg: str):
        transport = self.create_transport()

        result = f"Логіст: Замовлення прийнято. Я обираю транспорт...\n"
        result += f"Логіст: Використано {transport.__class__.__name__}. "
        result += transport.deliever(packeg)

        return result

    @abstractmethod
    def create_transport(self):
        pass

class RoadLogistkic(Logistics):
    def create_transport(self):
        return Truck()

class WaterLogistkic(Logistics):
    def create_transport(self):
        return Ship()

class FlyLogistkic(Logistics):
    def create_transport(self):
        return Plane()


if __name__ == "__main__":
    road = RoadLogistkic()
    print(road.plan_of_deliever("Книги"))

    water = WaterLogistkic()
    print(water.plan_of_deliever("Гумові Каченята"))

    plane = FlyLogistkic()
    print(plane.plan_of_deliever("Посилки з Аліекспрес"))