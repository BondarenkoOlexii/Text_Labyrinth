from abc import ABC, abstractmethod
import random


class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def take_damage(self, amount):
        pass


class Goblin(Enemy):

    def __init__(self, hp):
        self.hp = hp

    def attack(self):
        damage = random.randint(1, 5)
        print(f"Гоблін завдав вам {damage} шкоди")
        return damage

    def take_damage(self, amount):
        self.hp -= amount
        print(f"Гобліну завднанно {amount} шкоди, в нього залишилось {self.hp} hp")
        if self.hp <= 0:
            print("Гоблін вбитий")
            return 0
        else:
            return self.hp


class Zombi(Enemy):
    def __init__(self, hp):
        self.hp = hp

    def attack(self):
        damage = random.randint(3, 8)
        print(f"Зомбі завдав вам {damage} шкоди")
        return damage

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print("Зомбі впав назад в могилу")
            return 0
        else:
            print(f"Зомбі отримав {amount} шкоди, в нього залишилось {self.hp} hp")
            return self.hp


class Skelet(Enemy):
    def __init__(self, hp):
        self.hp = hp

    def attack(self):
        damage = random.randint(7, 12)
        print(f"Скелет завдав вам {damage} шкоди")
        return damage

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print("Скелет розсипався")
            return 0
        else:
            print(f"Скелет отримав {amount} шкоди, в нього залишилось {self.hp} hp")
            return self.hp


class CreateEnemy(ABC):
    @abstractmethod
    def create_enemy(self):
        pass

class Create_Goblin(CreateEnemy):
    def create_enemy(self):
        return Goblin

class Create_Zombi(CreateEnemy):
    def create_enemy(self):
        return Zombi
class Create_Skelet(CreateEnemy):
    def create_enemy(self):
        return Skelet


if __name__ == "__main__":
    player_choose_enemy = None
    while player_choose_enemy != "Stop":

        player_hp = random.randint(80, 120)
        player_dmg = random.randint(7, 15)

        enemy_dict = {1: Create_Goblin,
                      2: Create_Zombi,
                      3: Create_Skelet
                      }

        enemy_hp_dict = {
            1: 10,
            2: 25,
            3: 50
        }
        print("Вибери з ким ти хочеш змагатись, 1 - це Гоблін, 2 - це Зомбі, 3 - це Скелет")
        player_choose_enemy = int(input())
        try:
            enemyClass = enemy_dict[player_choose_enemy]().create_enemy()
            enemy = enemyClass(enemy_hp_dict[player_choose_enemy])
        except Exception as e:
            print(e)
        while enemy.hp > 0 and player_hp > 0:
            player_hp -= enemy.attack()
            enemy.take_damage(player_dmg)
            if enemy.hp < 0 and player_hp > 0:
                print("Ви перемогли")
            if  enemy.hp > 0 and player_hp < 0:
                print("Ви програли")













