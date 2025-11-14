# Exercise 6-8: Pets
print("\n" + "=" * 50)
print("EXERCISE 6-8: PETS")

# Create several pet dictionaries
pet1 = {
    'animal_type':'dog',
    'owner_name':'Alice'
    }

pet2 = {
    'animal_type':'cat',
    'owner_name':'Bob'
    }

pet3 = {
    'animal_type':'parrot',
    'owner_name':'Charlie'
    }

pet4 = {
    'animal_type':'hamster',
    'owner_name':'Diana'
    }

# Store in pets list
pets = [pet1, pet2, pet3, pet4]

# Loop throught and print all information
for pet in pets:
    print(f"\nAnimal Type: {pet['animal_type'].title()}")
    print(f"Owner: {pet['owner_name']}")
