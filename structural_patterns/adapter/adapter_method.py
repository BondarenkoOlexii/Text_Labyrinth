class EuropeanSocketInterface:
    def voltage(self):
        pass
    def live(self):
        pass
    def neutral(self):
        pass



class AmericanSocket:
    def power_120v(self):
        return "120В змінного струму"



class SocketAdapter(EuropeanSocketInterface):
    def __init__(self, american_socket: AmericanSocket):
        self.american_socket = american_socket

    def voltage(self):
        return "220В"

    def live(self):
        return "фаза"

    def neutral(self):
        return "нуль"

    def convert_power(self):
        original = self.american_socket.power_120v()
        return f"Адаптер перетворив {original} → {self.voltage()}"



class Laptop:
    def charge(self, socket: EuropeanSocketInterface):
        print(f"Зарядка ноутбука... використовується {socket.voltage()}, {socket.live()}, {socket.neutral()}")


if __name__ == "__main__":
    american_socket = AmericanSocket()
    adapter = SocketAdapter(american_socket)

    laptop = Laptop()
    laptop.charge(adapter)

    print(adapter.convert_power())
