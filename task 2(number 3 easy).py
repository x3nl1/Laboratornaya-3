class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder
        self._balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        return self._balance
    
    def get_balance(self):
        return self._balance
    
    def get_account_holder(self):
        return self._account_holder
    
    def __str__(self):
        return f"Владелец: {self._account_holder}, Баланс: {self._balance}"

if __name__ == "__main__":
    account = BankAccount("Иван Иванов", 1000)
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(50)
    print(account)
    print(f"Текущий баланс: {account.get_balance()}")
