# planet_distances_dict.py

# Create a dictionary of 8 planets and their distances from the sun (in million kilometers)
planet_distances = {
    'Mercury': 57.91,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.5,
    'Saturn': 1427,
    'Uranus': 2871,
    'Neptune': 4497.1
}

# Print the entire dictionary
print("Planet Distances Dictionary (in million kilometers):", planet_distances)

# Access and print the distance of the 3rd planet
print("Distance of the 3rd planet (Earth):", planet_distances['Earth'], "million kilometers")

# Update the distance of the 5th planet
planet_distances['Jupiter'] = 800.0  # Example update
print("Updated planet distances dictionary:", planet_distances)

# Delete the 7th planet from the dictionary
del planet_distances['Uranus']
print("Planet distances dictionary after deletion:", planet_distances)

# Print the last key-value pair in the dictionary
last_planet = list(planet_distances.items())[-1]
print("Last key-value pair:", last_planet)
