# technology_innovators_dict.py

# Create a dictionary of 8 technologies and their innovators
technology_innovators = {
    'Internet': 'Tim Berners-Lee',
    'Smartphone': 'Steve Jobs',
    'Electric Vehicle': 'Nikola Tesla',
    'Artificial Intelligence': 'Alan Turing',
    'Blockchain': 'Satoshi Nakamoto',
    'Virtual Reality': 'Jaron Lanier',
    '3D Printing': 'Chuck Hull',
    'Cloud Computing': 'Marc Andreessen'
}

# Print the entire dictionary
print("Technology Innovators:", technology_innovators)

# Access and print the innovator of the 4th technology (Artificial Intelligence)
print("Innovator of the 4th technology (Artificial Intelligence):", technology_innovators['Artificial Intelligence'])

# Update the innovator of the 2nd technology (Smartphone)
technology_innovators['Smartphone'] = 'John Sculley'
print("Updated Technology Innovators:", technology_innovators)

# Delete the 6th technology (Virtual Reality) from the dictionary
del technology_innovators['Virtual Reality']
print("Technology Innovators after deletion:", technology_innovators)

# Print the last key-value pair in the dictionary
last_technology_innovator = list(technology_innovators.items())[-1]
print("Last key-value pair:", last_technology_innovator)
