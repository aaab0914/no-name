user_age = int(input("What is your age: "))

if user_age <= 2:
    print("have fun!")
elif user_age >= 3  and user_age < 12:
    print("you need to pay $10 to watch movie.")
elif user_age >= 12:
    print("you need to pay $15 to watch movie.")
    
print(user_age)
