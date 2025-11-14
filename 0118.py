# Exercise 6-9: Favorite Places
print("\n" + "=" * 50)
print("EXERCISE 6-9: FAVORITE PLACES")

# Create favotie_places dictionary
favorite_places = {
    'alice':['Paris', 'Toyko', 'New York'],
    'bob':['London', 'Syndey'],
    'charlie':['Rome', 'Barcelona', 'Berlin']
    }

# Loop through and print each person's name and favorite places
for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places:")
    for place in places:
        print(f"   - {place}")
          
