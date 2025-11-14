class GameMemento():
    def __init__(self, hp, attack):
        self._hp = hp
        self._dmg = attack

    def get_hp(self):
        return self._hp

    def get_dmg(self):
        return self._dmg


class Player():
    def __init__(self):
        self.hp = 100
        self.dmg = 10

    def take_damage(self, amount):
        self.hp -= amount
        self.dmg += amount // 10
        print(f"\nГравцю нанесли {amount} урона, в нього залишилось {self.hp} а його урон виріс до {self.dmg}")

    def heal(self, amount):
        self.hp += amount
        self.dmg -= amount // 10
        print(f"\nГравцю відхілили {amount} хп, тепер його здоров'я = {self.hp} але урон від атаки впав до {self.dmg}")

    def save(self):
        print("Зберігаємо стан")
        return GameMemento(self.hp, self.dmg)

    def returner(self, memento):
        self.hp = memento.get_hp()
        self.dmg = memento.get_dmg()
        print(f"Гравця повернуло на один крок назад, його хп = {self.hp}, а урон = {self.dmg}")

class GameHistory():
    def __init__(self):
        self._save = []

    def add_save(self, memento):
        self._save.append(memento)

    def last_save(self):
        if len(self._save) >= 2:
            return self._save[-2]
        else:
            return None
if __name__ == "__main__":
    player = Player()
    history = GameHistory()


    history.add_save(player.save())
    player.take_damage(10)
    history.add_save(player.save())
    player.take_damage(50)
    history.add_save(player.save())
    player.heal(20)
    history.add_save(player.save())
    player.returner(history.last_save())