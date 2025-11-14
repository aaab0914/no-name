class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = self._generate_account_number()

    def _generate_account_number(self):
        import random
        return f"ACC{random.randint(10000,99999)}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"

    def get_balance(self):
        return f"Current balance: ${self.balance}"

account = BankAccount("John Doe", 1000)
print(account.account_number)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
    
