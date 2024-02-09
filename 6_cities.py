# 6-11 Cities

cities = {
    "fairfax": {
        "country": "united states of america",
        "population": "1000000000",
        "fact": "state bird is a cardinal",
    },
    "new york": {
        "country": "united states of america",
        "population": "10000000000",
        "fact": "home of the empire state building",
    },
    "versailles": {
        "country": "united states of america",
        "population": "500000",
        "fact": "is a suburb of lexington",
    },
}

for city, city_info in cities.items():
    print(f"{city.title()}")
    country = city_info["country"]
    print(f"\tIs in country: {country.title()}")
    population = city_info["population"]
    print(f"\tHas a population of: {population}")
    fact = city_info["fact"]
    print(f"\tFast Fact: {fact.capitalize()}")
