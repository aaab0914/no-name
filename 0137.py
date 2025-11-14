# Exercise 6-11: Cities
print("=== Exercise 6-11: Cities ===")

cities = {
	'tokyo': {
		'country': 'japan',
		'population': 37_000_000,
		'fact': 'Tokyo is the most populous metropolitan area in the world.',
		'landmark': 'Toyko Tower',
		'famous_food': 'sushi'
	},
	'paris': {
		'country': 'frence',
		'population': 2_100_100,
		'fact': 'Paris is know as the city of light.',
		'landmark': 'Elffel Tower',
		'famous_food': 'croissant'
	},
	'new_york': {
		'country': 'united states',
		'population': 8_400_000,
		'fact': 'New York City has over 800 languages spoken.',
		'landmark': 'Statue of liberty',
		'famous_food': 'pizza'
	}
}

# Print information about each city
for city, info in cities.items():
	print(f"\n{city.title()}:")
	print(f" Country: {info['country'].title()}")
	print(f" Fact: {info['fact']}")
	print(f" Famous Landmark: {info['landmark']}")
	print(f" Famous Food: {info['famous_food'].title()}")
	
