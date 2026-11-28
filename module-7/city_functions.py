# Francisco Villa           11/27/2026
# Advanced Python           Module 7.2

def format_city_country(city, country, population= '', language= ''):
    # Return a neatly formatted 'City, Country, Population, Language' string.
    results = f"{city.title()}, {country.title()}"
    if population:
        results += f" - population {population}"
    if language:
       results += f", {language.title()}"
    return results

# Calling the function three times with different City, Country values
print(format_city_country("Santiago", "Chile", "5000000", "Spanish"))
print(format_city_country("Tokyo", "Japan"))
print(format_city_country("Bellevue", "United States", 65000))