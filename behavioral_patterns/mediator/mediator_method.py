from abc import ABC, abstractmethod



class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user):
        pass

    @abstractmethod
    def add_user(self, user):
        pass



class ChatRoom(ChatMediator):
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def send_message(self, message: str, sender):
        for user in self._users:
            if user != sender:
                user.receive(message, sender)



class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    def send(self, message: str):
        print(f"{self.name} відправляє: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message: str, sender):
        print(f"{self.name} отримав від {sender.name}: {message}")



from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user):
        pass

    @abstractmethod
    def add_user(self, user):
        pass


class ChatRoom(ChatMediator):
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def send_message(self, message: str, sender):
        for user in self._users:
            if user != sender:
                user.receive(message, sender)


class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    def send(self, message: str):
        print(f"{self.name} відправляє: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message: str, sender):
        print(f"{self.name} отримав від {sender.name}: {message}")


if __name__ == "__main__":
    chat = ChatRoom()

    user1 = User("Аня", chat)
    user2 = User("Ігор", chat)

    current_user = user1  # починає Аня
    print("Почнемо чат! Введи '!' щоб змінити користувача, або 'exit' щоб вийти.\n")

    while True:
        message = input(f"{current_user.name}: ")

        if message.lower() == "exit":
            print("Чат завершено.")
            break

        if message == "!":
            current_user = user2 if current_user == user1 else user1
            print(f"Тепер пише {current_user.name}")
            continue

        current_user.send(message)
