import copy
import uuid

class Enemies:

    def __init__(self, name, health, damage, inventory=None):
        self.name = name
        self.hp = health
        self.dm = damage


        self.id = uuid.uuid4()

        self.inventory = inventory if inventory is not None else []

    def __str__(self):
        return (f"Name --- {self.name}, Health - {self.hp}, Damage - {self.dm}, Id - {self.id}, Inventory - {self.inventory}")


    def clone(self):
        return copy.deepcopy(self)



class Axe(Enemies):
    def __init__(self, name, health, damage, inventory=None):
        super().__init__(name, health, damage, inventory)

        #Особливості класу
        self.type = "Axe"
        self.shouts = "Axe is ready"



class Drow_Ranger(Enemies):
    def __init__(self, name, health, damage, inventory=None):
        super().__init__(name, health, damage, inventory)

        self.type = "People"
        self.shouts = "We're all guilty of something"


if __name__ == "__main__":

    Axe_prototype = Axe("Axe", 2000, 50, ['Phase Boots', 'Blade Mail'])
    Drow_Ranger_prototype = Drow_Ranger("Drow_Ranger", 1650, 140, ['Dragon Lance', 'Yasha'])

    print(f"Початковий Акс = {Axe_prototype}\n Початкова Дровка = {Drow_Ranger_prototype}")

    print("Створюємо їх клонів\n","-" * 20)

    new_Axe = Axe_prototype.clone()
    new_Axe.health = 2100
    new_Axe.damage = 100
    new_Axe.inventory.append('Blink Dagger')

    new_Drow_Ranger = Drow_Ranger_prototype.clone()
    new_Drow_Ranger.damage = 280
    new_Drow_Ranger.inventory.append('Butterfly')


    print(f"Клон Акса = {new_Axe}")
    print(f"Клон Дровки = {new_Drow_Ranger}")

    print(f"Оригінальний Акс в порівнянні з Клоном ==\n {Axe_prototype} vs {new_Axe}")
    print(f"Оригінальна Дровки в порівнянні з Клоном ==\n {Drow_Ranger_prototype} vs {new_Drow_Ranger}")
    print(f"{Axe_prototype is new_Axe} і {Drow_Ranger_prototype is new_Drow_Ranger}")