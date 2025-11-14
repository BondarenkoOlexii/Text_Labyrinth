from abc import ABC, abstractmethod


class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm):
        pass

    @abstractmethod
    def enter_pin(self, atm, pin):
        pass

    @abstractmethod
    def withdraw_cash(self, atm, amount):
        pass

    @abstractmethod
    def eject_card(self, atm):
        pass


class NoCardState(ATMState):
    def insert_card(self, atm):
        print("Картку вставлено.")
        atm.set_state(atm.has_card_state)

    def enter_pin(self, atm, pin):
        print("Спочатку вставте картку.")

    def withdraw_cash(self, atm, amount):
        print("Спочатку вставте картку.")

    def eject_card(self, atm):
        print("Немає картки для вилучення.")


class HasCardState(ATMState):
    def insert_card(self, atm):
        print("Картка вже вставлена.")

    def enter_pin(self, atm, pin):
        if pin == atm.correct_pin:
            print("Пін правильний.")
            atm.set_state(atm.correct_pin_state)
        else:
            print("Невірний пін. Картку вилучено.")
            atm.set_state(atm.no_card_state)

    def withdraw_cash(self, atm, amount):
        print("Спочатку введіть пін.")

    def eject_card(self, atm):
        print("Картку вилучено.")
        atm.set_state(atm.no_card_state)


class CorrectPinState(ATMState):
    def insert_card(self, atm):
        print("Картка вже вставлена.")

    def enter_pin(self, atm, pin):
        print("Пін уже підтверджено.")

    def withdraw_cash(self, atm, amount):
        if amount <= atm.cash:
            atm.cash -= amount
            print(f"Видано {amount} грн. Залишок: {atm.cash} грн.")
            if atm.cash == 0:
                print("Гроші закінчились. Банкомат недоступний.")
                atm.set_state(atm.no_cash_state)
        else:
            print("Недостатньо грошей у банкоматі.")

    def eject_card(self, atm):
        print("Картку вилучено.")
        atm.set_state(atm.no_card_state)


class NoCashState(ATMState):
    def insert_card(self, atm):
        print("Банкомат порожній. Використання неможливе.")

    def enter_pin(self, atm, pin):
        print("Банкомат порожній.")

    def withdraw_cash(self, atm, amount):
        print("Банкомат порожній.")

    def eject_card(self, atm):
        print("Картки немає.")



class ATM:
    def __init__(self, cash=1000):
        self.no_card_state = NoCardState()
        self.has_card_state = HasCardState()
        self.correct_pin_state = CorrectPinState()
        self.no_cash_state = NoCashState()

        self.state = self.no_card_state
        self.cash = cash
        self.correct_pin = 1234

    def set_state(self, state):
        self.state = state

    def insert_card(self):
        self.state.insert_card(self)

    def enter_pin(self, pin):
        self.state.enter_pin(self, pin)

    def withdraw_cash(self, amount):
        self.state.withdraw_cash(self, amount)

    def eject_card(self):
        self.state.eject_card(self)


if __name__ == "__main__":
    atm = ATM(500)

    atm.insert_card()
    atm.enter_pin(1234)
    atm.withdraw_cash(200)
    atm.withdraw_cash(300)
    atm.insert_card()
    atm.enter_pin(1234)
    atm.withdraw_cash(100)
