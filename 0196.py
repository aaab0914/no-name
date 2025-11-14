# 4. Temperature Converter
while True:
    print("\n=== Temperature Converter ===")
    print("1. Celsius to fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == '1':
        celsius = float(input("Enter Celsius temperature: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter Fahrenheit temperature: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")
    elif choice == '3':
        print("Thank you for using the converter!")
        break
    else:
        print("Invalid choice! Please enter 1-3.")
        