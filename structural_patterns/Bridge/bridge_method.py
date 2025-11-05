class Device:
    def enable(self): pass
    def disable(self): pass
    def set_volume(self, level): pass



class TV(Device):
    def enable(self):
        print("Телевізор увімкнено")

    def disable(self):
        print("Телевізор вимкнено")

    def set_volume(self, level):
        print(f"Гучність телевізора: {level}")


class Radio(Device):
    def enable(self):
        print("Радіо увімкнено")

    def disable(self):
        print("Радіо вимкнено")

    def set_volume(self, level):
        print(f"Гучність радіо: {level}")


class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.enable()

    def turn_off(self):
        self.device.disable()

    def volume(self, level):
        self.device.set_volume(level)


# Розширена абстракція (пульт з додатковими фічами)
class AdvancedRemote(RemoteControl):
    def mute(self):
        print("Пристрій вимкнено в беззвучний режим")
        self.device.set_volume(0)



if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    remote_tv = RemoteControl(tv)
    remote_radio = AdvancedRemote(radio)


    remote_tv.turn_on()
    remote_tv.volume(15)
    remote_tv.turn_off()

    print("=" * 5)


    remote_radio.turn_on()
    remote_radio.volume(10)
    remote_radio.mute()
    remote_radio.turn_off()
