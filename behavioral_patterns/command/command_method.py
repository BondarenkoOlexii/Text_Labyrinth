#Завод з робітниками
from abc import ABC, abstractmethod

class Worker:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def work(self):
        print(f"{self.name} зробив {self.speed} гвоздів")

    def rest(self):
        print(f"{self.name} відпочиває")

    def work_faster(self):
        print(f"{self.name} зробив {self.speed * 3} гвоздів і пішов відпичавити")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Work(Command):
    def __init__(self, object):
        self.object = object

    def execute(self):
        self.object.work()

class Reset(Command):
    def __init__(self, object):
        self.object = object

    def execute(self):
        self.object.rest()

class WorkOverTime(Command):
    def __init__(self, object):
        self.object = object

    def execute(self):
        self.object.work_faster()

class Director:
    def __init__(self):
        self.queue = []

    def take_command(self, command):
        self.queue.append(command)

    def run_commands(self):
        for cmd in self.queue:
            cmd.execute()

    def undo(self):
        if self.queue:
            print("Остання вказівка скасовується")
            self.queue.pop()

    def repeat_command(self, times):
        for _ in range(times):
            for cmd in self.queue:
                cmd.execute()
            print("-"* 25)


if __name__ == "__main__":
    directory = Director()
    Valeriy = Worker("Валерій", 5)
    Sergiy = Worker("Сергій", 10)
    Misha = Worker("Михайло", 2)

    directory.take_command(Work(Valeriy))
    directory.take_command(WorkOverTime(Misha))
    directory.take_command(Work(Sergiy))
    directory.take_command(Reset(Sergiy))
    directory.take_command(Reset(Valeriy))

    directory.repeat_command(3)
    directory.run_commands()