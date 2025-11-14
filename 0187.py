class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")

        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")

account1 = BankAccount("Alice Brown", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()
