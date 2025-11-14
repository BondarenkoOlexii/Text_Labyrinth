from abc import ABC, abstractmethod

class Abstract_NightClub(ABC):
    @abstractmethod
    def get_in(self):
        pass


class NightClub(Abstract_NightClub):
    def get_in(self):
        print("Вхід до клубу дозволенний")

    def dance(self):
        print("Ви танцюєте на танцполі")

    def oreder_drink(self, drink):
        print(f"Ви замовили - {drink} у бармена")

class NightClubeGuard(Abstract_NightClub):
    def __init__(self):
        self.club = NightClub()
        self.allow = False

    def allowed(self, age: int):
        if age >= 18:
            self.allow = True
        else:
            self.allow = False
    def get_in(self):
        if self.allow:
            self.club.get_in()
        else:
            print("Вам сюди не можна")

    def dance(self):
        if self.allow:
            self.club.dance()
        else:
            print("Ви не ввійшли в клуб")

    def dance(self):
        if self.allow:
            drinks = ["Мохіто", "Джин-Тонік", "Пиво", "Віскі", "Сік"]
            print("\nМеню напоїв:")
            for i, d in enumerate(drinks, start=1):
                print(f"{i} {d}")

            try:
                choice = int(input("Виберіть напій (номер): "))
                if 1 <= choice <= len(drinks):
                    selected_drink = drinks[choice - 1]
                    self.club.oreder_drink(selected_drink)
                else:
                    print("Невірний вибір.")
            except ValueError:
                print("Введіть номер, а не текст.")


if __name__ == '__main__':
    club = NightClubeGuard()
    club.get_in()

    while True:
        print("\n=== Нічний клуб ===")
        print("1. Танцювати")
        print("2. Замовити напій")
        print("3. Вийти з клубу")

        choice = input("Ваш вибір: ")

        if choice == "1":
            club.dance()
        elif choice == "2":
            club.oreder_drink()
        elif choice == "3":
            print("Ви залишили клуб. До зустрічі!")
            break
        else:
            print("Невірна опція.")