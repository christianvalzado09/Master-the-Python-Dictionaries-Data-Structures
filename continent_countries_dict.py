# continent_countries_dict.py

# Create a dictionary of 6 continents and a list of 3 countries for each
continent_countries = {
    'Africa': ['Nigeria', 'Egypt', 'South Africa'],
    'Asia': ['China', 'India', 'Japan'],
    'Europe': ['Germany', 'France', 'United Kingdom'],
    'North America': ['USA', 'Canada', 'Mexico'],
    'Oceania': ['Australia', 'New Zealand', 'Fiji'],
    'South America': ['Brazil', 'Argentina', 'Chile']
}

# Print the entire dictionary
print("Continent Countries Dictionary:", continent_countries)

# Access and print the countries of the 4th continent
print("Countries of the 4th continent (North America):", continent_countries['North America'])

# Update the countries of the 5th continent
continent_countries['Oceania'] = ['Australia', 'New Zealand', 'Papua New Guinea']  # Example update
print("Updated continent countries dictionary:", continent_countries)

# Delete the 6th continent from the dictionary
del continent_countries['South America']
print("Continent countries dictionary after deletion:", continent_countries)

# Print the last key-value pair in the dictionary
last_continent = list(continent_countries.items())[-1]
print("Last key-value pair:", last_continent)
