#TiY 11-2
def city_country(city, country, population):
    string = f"{city.title()}, {country.title()}"
    string += f" -population {population}"
    return string

#optional parameter section
def city_country(city, country, population = 0):
    string = f"{city.title()}, {country.title()}"
    if population:
        string += f" - population {population}"
    return string


