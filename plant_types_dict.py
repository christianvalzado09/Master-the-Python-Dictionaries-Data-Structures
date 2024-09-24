# plant_types_dict.py

# Create a dictionary of 8 plants and their types
plant_types = {
    'Rose': 'Shrub',
    'Oak': 'Tree',
    'Basil': 'Herb',
    'Maple': 'Tree',
    'Lavender': 'Herb',
    'Cactus': 'Succulent',
    'Tulip': 'Bulb',
    'Fern': 'Fern'
}

# Print the entire dictionary
print("Plant types dictionary:", plant_types)

# Access and print the type of the 5th plant (Lavender)
print("The type of the 5th plant (Lavender):", plant_types['Lavender'])

# Update the type of the 2nd plant (Oak)
plant_types['Oak'] = 'Deciduous Tree'
print("Updated plant types dictionary:", plant_types)

# Delete the 6th plant (Cactus) from the dictionary
del plant_types['Cactus']
print("Plant types dictionary after deletion:", plant_types)

# Print the last key-value pair in the dictionary
last_plant_type = list(plant_types.items())[-1]
print("Last key-value pair:", last_plant_type)
