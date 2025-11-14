def city_country(city, country):
    """ Return a formatted string of city and country. """
    return f"{city.title()}, {country.title()}"

# Call the function with three city-country pairs
print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('paris', 'france'))
