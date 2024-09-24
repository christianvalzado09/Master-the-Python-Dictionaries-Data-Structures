# coffee_types_dict.py

# Create a dictionary of 10 types of coffee and their descriptions
coffee_types = {
    'Espresso': 'A concentrated coffee brewed by forcing hot water through finely-ground coffee.',
    'Latte': 'A creamy coffee drink made with espresso and steamed milk.',
    'Cappuccino': 'A coffee drink that consists of espresso mixed with steamed milk and topped with foamed milk.',
    'Americano': 'A diluted espresso made by adding hot water, giving it a similar strength to drip coffee.',
    'Macchiato': 'An espresso with a small amount of steamed milk or milk foam.',
    'Mocha': 'A chocolate-flavored variant of a latte, made with espresso, steamed milk, and chocolate syrup.',
    'Flat White': 'A coffee drink made with espresso and microfoam, similar to a latte but with less milk.',
    'Affogato': 'A dessert made with a scoop of vanilla ice cream topped with a shot of hot espresso.',
    'Cold Brew': 'Coffee brewed with cold water over an extended period, resulting in a smooth, less acidic flavor.',
    'Turkish Coffee': 'A traditional coffee preparation method involving finely ground coffee boiled in water with sugar and spices.'
}

# Print the entire dictionary
print("Coffee types and their descriptions dictionary:", coffee_types)

# Access and print the description of the 4th type of coffee (Americano)
print("Description of the 4th type of coffee (Americano):", coffee_types['Americano'])

# Update the description of the 8th type of coffee (Affogato)
coffee_types['Affogato'] = 'A dessert made with espresso poured over a scoop of ice cream or gelato.'
print("Updated coffee types and their descriptions dictionary:", coffee_types)

# Delete the 5th type of coffee (Macchiato) from the dictionary
del coffee_types['Macchiato']
print("Coffee types and their descriptions dictionary after deletion:", coffee_types)

# Print the last key-value pair in the dictionary
last_coffee_type = list(coffee_types.items())[-1]
print("Last key-value pair:", last_coffee_type)
