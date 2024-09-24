# fruit_colors_dict.py

# Create a dictionary of 8 fruits and their corresponding colors
fruit_colors = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Grape': 'Purple',
    'Orange': 'Orange',
    'Lemon': 'Yellow',
    'Watermelon': 'Green',
    'Blueberry': 'Blue',
    'Kiwi': 'Brown'
}

# Print the entire dictionary
print("Fruit Colors Dictionary:", fruit_colors)

# Access and print the color of the 6th fruit
print("Color of the 6th fruit (Watermelon):", fruit_colors['Watermelon'])

# Update the color of the 4th fruit
fruit_colors['Orange'] = 'Dark Orange'  # Example update
print("Updated fruit colors dictionary:", fruit_colors)

# Delete the 7th fruit from the dictionary
del fruit_colors['Blueberry']
print("Fruit colors dictionary after deletion:", fruit_colors)

# Print the last key-value pair in the dictionary
last_fruit = list(fruit_colors.items())[-1]
print("Last key-value pair:", last_fruit)
