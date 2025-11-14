# Ask user how many people are in their dinner group
while True:
    try:
        party_size = int(input("How many people are in your dinner group?"))
        break
    except ValueError:
        print("Please enter a valid number.")

# Check if they have to wait or if table is ready
if party_size > 8:
    print("I'm sorry, you'll have to wait for table.")
else:
    print("Your table is ready! Please follow me.")
