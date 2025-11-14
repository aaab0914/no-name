# Exercise 6-7: People
print("\n" + "=" * 50)
print("EXERCISE 6-7: PEOPLE")

# From exercise 6-1
person1 = {
    'first_name':'John',
    'last_name':'Smith',
    'age':30,
    'city':'New York'
    }

# Create two more people
person2 = {
    'first_name':'Emily',
    'last_name':'Johnson',
    'age':25,
    'city':'London'
    }

person3 = {
    'first_name':'Michael',
    'last_name':'Brown',
    'age':35,
    'city':'Chicago'
    }

# Store all dictionaries in a list called people
people = [person1,person2,person3]

# Loop through the list and print everything about each person
for person in people:
    print(f"\nName: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    
