# animal_sounds_dict.py

# Create a dictionary of 8 animals and their corresponding sounds
animal_sounds = {
    'Dog': 'Bark',
    'Cat': 'Meow',
    'Cow': 'Moo',
    'Lion': 'Roar',
    'Sheep': 'Baa',
    'Duck': 'Quack',
    'Elephant': 'Trumpet',
    'Frog': 'Ribbit'
}

# Print the entire dictionary
print("Animal Sounds Dictionary:", animal_sounds)

# Access and print the sound of the 4th animal
print("Sound of fourth animal:", animal_sounds['Lion'])

# Update the sound of the 7th animal
animal_sounds['Elephant'] = 'Pawoo'
print("Updated animal sounds dictionary:", animal_sounds)

# Delete the 5th animal from the dictionary
del animal_sounds['Sheep']
print("Animal sounds dictionary after deletion:", animal_sounds)

# Print the last key-value pair in the dictionary
last_animal = list(animal_sounds.items())[-1]
print("Last key-value pair:", last_animal)
