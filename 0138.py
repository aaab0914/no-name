# Exercise 6-8: Pets
print("\n" + "=" * 50)
print("Exercise 6-8: Pets")

# Create several pet dictionaries
pets = [
	{
		'animal_type': 'dog',
		'owner_name': 'alice',
		'name': 'Buddy',
		'breed': 'Golden Retriever',
		'age': 3,
		'favorite_toy': 'tennis ball'
	},
	{
		'animal_type': 'cat',
		'owner_name': 'bob',
		'name': 'Whiskers',
		'breed': 'Siamese',
		'age': 2,
		'favorite_toy': 'laser pointer'
	},
	{
		'animal_type': 'parrot',
		'owner_name': 'charlie',
		'name': 'Rio',
		'breed': 'African Grey',
		'age': 5,
		'favorite_toy': 'mirror',
	},
	{
		'animal_type':'hamster',
		'owner_name': 'diana',
		'name': 'Nibbles',
		'breed': 'Syrian Hamaster',
		'age': 1,
		'favorite_toy': 'exercise wheel'
	}
]

# Loop through and print all information about each pet
print("PET DIRECTORY")
print("=" * 60)

for pet in pets:
	print(f"\nPet Name: {pet['name']}")
	print(f"Animal Type: {pet['animal_type']}")
	print(f"Owner: {pet['owner_name'].title()}")
	print(f"Breed: {pet['breed']}")
	print(f"Age: {pet['age']} years old")
	print(f"Favorite Toy: {pet['favorite_toy']}")
	print("-" * 40)
	
print(f"\nTotal pets in directory: {len(pets)}")
