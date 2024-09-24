# animal_habitats_dict.py

# Create a dictionary of 8 animals and their natural habitats
animal_habitats = {
    'Elephant': 'Savanna',
    'Polar Bear': 'Arctic',
    'Penguin': 'Antarctic',
    'Kangaroo': 'Grasslands',
    'Tiger': 'Rainforest',
    'Giraffe': 'Savanna',
    'Whale': 'Ocean',
    'Alligator': 'Wetlands'
}

# Print the entire dictionary
print("Animal Habitats Dictionary:", animal_habitats)

# Access and print the habitat of the 3rd animal
print("Habitat of the 3rd animal (Penguin):", animal_habitats['Penguin'])

# Update the habitat of the 5th animal
animal_habitats['Tiger'] = 'Forests'  # Example update
print("Updated animal habitats dictionary:", animal_habitats)

# Delete the 7th animal from the dictionary
del animal_habitats['Whale']
print("Animal habitats dictionary after deletion:", animal_habitats)

# Print the last key-value pair in the dictionary
last_animal = list(animal_habitats.items())[-1]
print("Last key-value pair:", last_animal)
