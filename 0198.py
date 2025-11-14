# 1. Number Counter
while True:
    print("\n=== Number Counter ===")
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        print("Counter stopped. Goodbye!")
        break
    elif number > 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is negative")
        
    print(f"Square of {number} is {number * number}")
    