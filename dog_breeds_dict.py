# dog_breeds_dict.py

# Create a dictionary of 10 dog breeds and their sizes (small, medium, large)
dog_breeds = {
    'Chihuahua': 'Small',
    'Bulldog': 'Medium',
    'Golden Retriever': 'Large',
    'Poodle': 'Medium',
    'Beagle': 'Medium',
    'Shih Tzu': 'Small',
    'German Shepherd': 'Large',
    'Dachshund': 'Small',
    'Rottweiler': 'Large',
    'Pomeranian': 'Small'
}

# Print the entire dictionary
print("Dog breeds and their sizes:", dog_breeds)

# Access and print the size of the 5th breed (Beagle)
print("Size of the 5th breed (Beagle):", dog_breeds['Beagle'])

# Update the size of the 8th breed (Dachshund)
dog_breeds['Dachshund'] = 'Medium'  # Example update
print("Updated dog breeds dictionary:", dog_breeds)

# Delete the 6th breed (Shih Tzu) from the dictionary
del dog_breeds['Shih Tzu']
print("Dog breeds dictionary after deletion:", dog_breeds)

# Print the last key-value pair in the dictionary
last_breed_size = list(dog_breeds.items())[-1]
print("Last key-value pair:", last_breed_size)
