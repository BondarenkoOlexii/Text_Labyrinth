class BankSystem:

    _instance = None


    def __new__(cls):
        if cls._instance is None:

            cls._instance = super(BankSystem, cls).__new__(cls)

            cls._instance.accounts = {}

            cls._instance.next_account_number = 1

        return cls._instance


    def open_account(self, owner_name, initial_deposit=0):
        account_number = self.next_account_number
        self.accounts[account_number] = {
            "name": owner_name,
            'balance': initial_deposit
        }
        self.next_account_number += 1
        print(f"Рахунок №{account_number} для {owner_name} відкрито. Баланс: {initial_deposit} грн.")
        return account_number


    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(
                f"Рахунок №{account_number} поповнено на {amount} грн. Новий баланс: {self.accounts[account_number]['balance']} грн.")
        else:
            print(f"Помилка: Рахунок №{account_number} не знайдено.")


    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        return None


if __name__ == "__main__":
    bank_system_1 = BankSystem()

    account_1 = bank_system_1.open_account("Іван Петренко", 1000)

    bank_system_1.deposit(account_1, 666)

    current_balance = bank_system_1.get_account_balance(account_1)
    print(f"Поточний баланс рахунку №{account_1}: {current_balance} грн.")