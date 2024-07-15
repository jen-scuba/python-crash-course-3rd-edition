from city_functions import get_formatted_city_country_name


def test_city_country_name():
    formatted_city_country_name = get_formatted_city_country_name(
            'santigo',
            'chile'
        )
    assert formatted_city_country_name == 'Santigo, Chile'


def test_city_country_name_population():
    formatted_city_country_name = get_formatted_city_country_name(
            'santigo',
            'chile',
            '5000000'
        )
    assert formatted_city_country_name == 'Santigo, Chile - population 5000000'
