# Підсистема (складні об'єкти)
class TV:
    def on(self):
        print("Телевізор увімкнено")
    def off(self):
        print("Телевізор вимкнено")

class DVDPlayer:
    def on(self):
        print("DVD-програвач увімкнено")
    def play(self, movie):
        print(f"Відтворення фільму: {movie}")
    def off(self):
        print("DVD-програвач вимкнено")

class SoundSystem:
    def on(self):
        print("Акустика увімкнена")
    def set_volume(self, level):
        print(f"Гучність встановлено на {level}")
    def off(self):
        print("Акустика вимкнена")

class Lights:
    def dim(self):
        print("Світло приглушено")
    def on(self):
        print("Світло увімкнено")


#Фасад
class HomeTheaterFacade:
    def __init__(self, tv, dvd, sound, lights):
        self.tv = tv
        self.dvd = dvd
        self.sound = sound
        self.lights = lights

    def watch_movie(self, movie):
        print("Підготовка до перегляду...")
        self.lights.dim()
        self.tv.on()
        self.sound.on()
        self.sound.set_volume(15)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Завершення перегляду...")
        self.lights.on()
        self.dvd.off()
        self.sound.off()
        self.tv.off()
