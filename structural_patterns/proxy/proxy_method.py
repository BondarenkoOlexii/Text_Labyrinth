from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount): pass

    @abstractmethod
    def withdraw(self, amount): pass



class RealBankAccount(BankAccount):
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}: внесено {amount} грн. Баланс = {self.balance} грн.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner}: знято {amount} грн. Баланс = {self.balance} грн.")
        else:
            print(f"{self.owner}: недостатньо коштів!")



class BankAccountProxy(BankAccount):
    def __init__(self, real_account, password):
        self._real_account = real_account
        self._password = password

    def authenticate(self):
        pwd = input("Введіть пароль: ")
        return pwd == self._password

    def deposit(self, amount):
        if self.authenticate():
            self._real_account.deposit(amount)
        else:
            print("Доступ заборонено!")

    def withdraw(self, amount):
        if self.authenticate():
            self._real_account.withdraw(amount)
        else:
            print("Доступ заборонено!")


if __name__ == "__main__":
    account = RealBankAccount("Олексій")
    proxy = BankAccountProxy(account, "1234")

    proxy.deposit(100)
    proxy.withdraw(50)
