# Exercise 7-6: Three Exits
print("\n=== Exercise 7-6: Three Exits ===")

# Version 1: Conditional test in while statement
print("\nVersion 1 - Conditional in while:")
age = ""
while age != 'quit':
    age = input("Enter your age(or 'quit'):")
    if age != 'quit':
        age_num = int(age)
        if age_num < 3:
            print("Ticket: Free")
        elif age_num <= 12:
            print("Ticket: $10")
        else:
            print("Ticket: $15")
            
# Version 2: Active variable
print("Version 2 - Active variable:")
active = True
while active:
    age = input("Enter your age (or 'quit'):")
    if age == 'quit':
        active = False
    else:
        age_num = int(age)
        if age_num < 3:
            print("Ticket: Free")
        elif age_num <= 12:
            print("Ticket: $10")
        else:
            print("Ticked: $15")
            
# Version 3: Brake statement (same as 7-5)
print("\nVersion 3 - Break statement:")
while True:
    age = input("Enter your age (or 'quit'):")
    if age == 'quit':
        break
    age_num = int(age)
    if age_num < 3:
        print("Ticked: Free")
    elif age_num <= 12:
        print("Ticket: $10")
    else:
        print("Ticket: $15")