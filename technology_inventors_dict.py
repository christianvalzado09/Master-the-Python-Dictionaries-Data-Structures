# technology_inventors_dict.py

# Create a dictionary of 6 technologies and their inventors
technology_inventors = {
    'Telephone': 'Alexander Graham Bell',
    'Light Bulb': 'Thomas Edison',
    'Computer': 'Charles Babbage',
    'Internet': 'Tim Berners-Lee',
    'Airplane': 'Wright Brothers',
    'Television': 'John Logie Baird'
}

# Print the entire dictionary
print("Technology Inventors Dictionary:", technology_inventors)

# Access and print the inventor of the 4th technology
print("Inventor of the 4th technology (Internet):", technology_inventors['Internet'])

# Update the inventor of the 2nd technology
technology_inventors['Light Bulb'] = 'Joseph Swan'  # Example update
print("Updated technology inventors dictionary:", technology_inventors)

# Delete the 6th technology from the dictionary
del technology_inventors['Television']
print("Technology inventors dictionary after deletion:", technology_inventors)

# Print the last key-value pair in the dictionary
last_technology = list(technology_inventors.items())[-1]
print("Last key-value pair:", last_technology)
