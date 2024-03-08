def city_country(city_name, country_name):
    """ Return a formatted string for city and country. """
    formatted_name = f"\"{city_name}, {country_name}\""
    return formatted_name.title()

city = city_country('santiago', 'chile')
print(city)
city = city_country('san fransico', 'united states of america')
print(city)
city = city_country('nassau', 'bahamas')
print(city)