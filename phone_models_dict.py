# phone_models_dict.py

# Create a dictionary of 10 phone models and their manufacturers
phone_models = {
    'iPhone 14': 'Apple',
    'Galaxy S22': 'Samsung',
    'Pixel 6': 'Google',
    'OnePlus 9': 'OnePlus',
    'Xiaomi Mi 11': 'Xiaomi',
    'Sony Xperia 5': 'Sony',
    'Nokia G50': 'Nokia',
    'Galaxy Z Fold 4': 'Samsung',
    'Moto G Power': 'Motorola',
    'LG Velvet': 'LG'
}

# Print the entire dictionary
print("Phone Models Dictionary:", phone_models)

# Access and print the manufacturer of the 2nd phone model
print("Manufacturer of the 2nd phone model (Galaxy S22):", phone_models['Galaxy S22'])

# Update the manufacturer of the 8th phone model
phone_models['Galaxy Z Fold 4'] = 'Samsung Electronics'  # Example update
print("Updated phone models dictionary:", phone_models)

# Delete the 6th phone model from the dictionary
del phone_models['Sony Xperia 5']
print("Phone models dictionary after deletion:", phone_models)

# Print the last key-value pair in the dictionary
last_model = list(phone_models.items())[-1]
print("Last key-value pair:", last_model)
