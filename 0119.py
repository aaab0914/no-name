# Exercise 6-10: Favorite Numbers
print("\n" + "=" * 50)
print("EXERCISE 6-10: FAVORITE NUMBERS")

# Modified from exercise 6-2 - each person can have multiple favotire numbers
favorite_numbers = {
    'alice':[7,13,21],
    'bob':[42,3],
    'charlie':[13,27,99],
    'diana':[3,7,11,23],
    'edward':[21,34,55]
    }

# Print each person's name and their favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers:{','.join(map(str,numbers))}")
