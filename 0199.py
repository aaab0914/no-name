# 2. Simple ATM
balance = 1000
while True:
    print(f"\n=== ATM Machine ===")
    print(f"Current Balance: ${balance}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    
    choice = input("Select option: ")
    
    if choice == '1':
        amount = float(input("Deposit amount: $"))
        balance += amount
        print(f"Deposited ${amount}. New balance: ${balance}")
    elif choice == '2':
        amount = float(input("Withdraw amount: $"))
        if amount <= balance:
            balance -= amount
            print(f"Withdrew ${amount}. New balance: ${balance}")
        else:
            print("Insufficient fujnds!")
    elif choice == '3':
        print("Thank you for using our ATM!")
        break
    else:
        print("Invilid option!")