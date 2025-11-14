from abc import ABC, abstractmethod

class AbstractHandler(ABC):
    def __init__(self):
        self._next_handler = None

    def next_step(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handler(self, message):
        pass


class AdminCommand(AbstractHandler):
    def handler(self, message):
        if message.startswith("/admin"):
            print("Панель адміна")
        elif self._next_handler:
            self._next_handler.handler(message)
        else:
            print("Щось все поламалось")

class UserCommand(AbstractHandler):
    def handler(self, message):
        if message.startswith("/"):
            if message.startswith("/start"):
                print("Команда старт")
            elif message.startswith("/help"):
                print("Команда хелп")
            elif message.startswith("/photo"):
                print("Вивести фото бота")

        elif self._next_handler:
            self._next_handler.handler(message)

        else:
            print("Щось зламалось")

class UserMessage(AbstractHandler):
    def handler(self, message):
        if not message.startswith("/"):
            match message:
                case "Привіт":
                    print("Привіт")
                    return
                case "Як справи":
                    print("Все чудово, а в тебе як?")
                    return
            if self._next_handler:
                self._next_handler.handler(message)
                return
        elif self._next_handler:
            self._next_handler.handler(message)
        else:
            print("Щось зломалось")


class FinalHandler(AbstractHandler):
    def handler(self, message):
        print("Я не знаю що тобі відповісти")


if __name__ == "__main__":
    admin_commands = AdminCommand()
    user_command = UserCommand()
    user_message = UserMessage()
    final_message = FinalHandler()

    admin_commands.next_step(user_command).next_step(user_message).next_step(final_message)

    message = [
        '/admin',
        '/start',
        '/help',
        'Привіт',
        'ай донт ноу',
        '/photo'
    ]

    for msg in message:
        print("-" * 25)
        admin_commands.handler(msg)