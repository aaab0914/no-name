# Exercise 6-11: Cities
print("\n" + "=" * 50)
print("EXERCISE 6-11: CICIES")

# Create cities dictionary
cities = {
    'tokyo':{
        'country':'Japan',
        'population':37_400_000,
        'fact':'Tokyo is the most populous metropolitan area in the world.'
        },
    'paris':{
        'country':'France',
        'population':2_000_000,
        'fact':'Paris is known as the city of Light.'
        },
    'new_york':{
        'country':'United States',
        'population':8_400_000,
        'fact':'New York City has over 800 languages spoken.'
        }
    }

# Print each city's name and all stored information
for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"   Country:{info['country']}")
    print(f"   Population:{info['population']:,}")
    print(f"   Fact:{info['fact']}")
