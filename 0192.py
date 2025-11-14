class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount! Please enter positive number.")
        else:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdraw ${amount}. New balance: "
    f"${self.balance}")
            else:
                print("Insufficient funds! Withdraw failed.")
                
# Test
account1 = BankAccount("Mike", 1000)
account1.withdraw(500)
account1.withdraw(800)
account1.withdraw(-50)