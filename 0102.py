# interactive version = ask friends for their favorite numbers
favorite_numbers = {}

print("Let's collect favorite numbers from your friends!")
print("Enter 'quit' to stop.\n")

while True:
    name = input("Enter your friends's name: ").strip()

    if name.lower() == 'quit':
        break

    try:
        number = int(input(f"Enter {name}'s favorite number: "))
        favorite_numbers[name] = number
        print(f"Added {name} with favorite number {number}\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Display the collected data
if favorite_numbers:
    print("\n" + "=" * 40)
    print("COLLECTED FAVORITE NUMBERS:")
    print("=" * 40)

    for name, number in favorite_numbers.items():
        print(f"{name:.<20} {number}")
else:
    print("No data collected.")
