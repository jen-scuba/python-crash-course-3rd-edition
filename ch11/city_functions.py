def get_formatted_city_country_name(city, country, population=''):
    """Generate a neatly formatted name for city and country."""
    if population:
        formatted_city_country_name = f"{city.title()}, {country.title()}" \
                                      f" - population {population}"
    else:
        formatted_city_country_name = f"{city.title()}, {country.title()}"
    return formatted_city_country_name
