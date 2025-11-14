from abc import ABC, abstractmethod
import time


class Observer(ABC):
    @abstractmethod
    def update(self, price):
        pass


class StockMarket:
    def __init__(self):
        self._price = {'Bitcoin': 0, 'Ethereum': 0, 'USD Coin': 0, 'Dogecoin': 0}
        self._observers = {}


    def add_observer(self, observer, subsribtion):
        self._observers[observer] = subsribtion

    def remove_observer(self, observer):
        del self._observers[observer]

    def notify(self):
        for observer, sup in self._observers.items():
            if sup == 'Light':
                time.sleep(1)
                observer.update(self._price)
            elif sup == 'Medium':
                time.sleep(0.5)
                observer.update(self._price)
            elif sup == 'VIP':
                observer.update(self._price)
            else:
                time.sleep(2)
                observer.update(self._price)

    def update_price(self, prices: dict):
        for key, value in prices.items():
            if key in self._price:
                self._price[key] = value
        self.notify()

class User_1(Observer):
    def update(self, price):
        print(f"Я юзер 1 - {price}")

class User_2(Observer):
    def update(self, price):
        print(f"Я юзер 2 - {price}")

class User_3(Observer):
    def update(self, price):
        print(f"Я юзер 3 - {price}")

class User_4(Observer):
    def update(self, price):
        print(f"Я юзер 4 - {price}")


if __name__ == "__main__":
    market = StockMarket()

    client_1 = User_1()
    market.add_observer(client_1, "Light")

    client_2 = User_2()
    market.add_observer(client_2, "Medium")

    client_3 = User_3()
    market.add_observer(client_3, "VIP")

    client_4 = User_4()
    market.add_observer(client_4, "SUPER_PUPER_VIP")

    market.update_price({
        'Bitcoin': 69000,
        'Ethereum': 3200,
        'USD Coin': 1,
        'Dogecoin': 0.12
    })

    market.remove_observer(client_3)

    market.update_price({
        'Bitcoin': 70000,
        'Dogecoin': 0.15
    })

    market.add_observer(client_3, "VIP")

    market.update_price({
        'Bitcoin': 59000,
        'Dogecoin': 0.20,
        'Ethereum': 5000,
    })