# city_population_dict.py

# Create a dictionary of 10 cities and their corresponding population
city_population = {
    'New York': 8419600,
    'Los Angeles': 3980400,
    'Chicago': 2716000,
    'Houston': 2328000,
    'Phoenix': 1690000,
    'Philadelphia': 1584200,
    'San Antonio': 1547200,
    'San Diego': 1423800,
    'Dallas': 1340000,
    'San Jose': 1035400
}

# Print the entire dictionary
print("City Population Dictionary:", city_population)

# Access and print the population of the 6th city
print("Population of the 6th city (Philadelphia):", city_population['Philadelphia'])

# Update the population of the 3rd city
city_population['Chicago'] = 2800000  # Update population for Chicago
print("Updated city population dictionary:", city_population)

# Delete the 9th city from the dictionary
del city_population['Dallas']
print("City population dictionary after deletion:", city_population)

# Print the last key-value pair in the dictionary
last_city = list(city_population.items())[-1]
print("Last key-value pair:", last_city)
