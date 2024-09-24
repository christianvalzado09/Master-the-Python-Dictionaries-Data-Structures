# river_lengths_dict.py

# Create a dictionary of 6 rivers and their lengths in kilometers
river_lengths = {
    'Nile': 6650,
    'Amazon': 6400,
    'Yangtze': 6300,
    'Mississippi': 3730,
    'Yenisei': 5539,
    'Yellow River': 5464
}

# Print the entire dictionary
print("River Lengths Dictionary:", river_lengths)

# Access and print the length of the 2nd river
print("Length of the 2nd river (Amazon):", river_lengths['Amazon'], "km")

# Update the length of the 5th river
river_lengths['Yenisei'] = 5800  # Example update
print("Updated river lengths dictionary:", river_lengths)

# Delete the 4th river from the dictionary
del river_lengths['Mississippi']
print("River lengths dictionary after deletion:", river_lengths)

# Print the last key-value pair in the dictionary
last_river = list(river_lengths.items())[-1]
print("Last key-value pair:", last_river)
