def get_city_country(city, country, population=''):
    if population:
        city_country = f"{city}, {country} - population {population}"
        return city_country.title()
    else:
        city_country = f"{city}, {country}"
        return city_country.title()

