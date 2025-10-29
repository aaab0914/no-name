# Create a dictionary of favorite numbers
favorite_numbers = {
    'alice':7,
    'bob':42,
    'chalie':13,
    'diana':3,
    'edward':21
    }

# Print each person's name and their favorite number
print("Favorite Numbers:")
print("=" * 25)

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}")
