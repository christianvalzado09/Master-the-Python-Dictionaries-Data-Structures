# car_brands_dict.py

# Create a dictionary of 10 car brands and their country of origin
car_brands = {
    'Toyota': 'Japan',
    'Ford': 'United States',
    'Volkswagen': 'Germany',
    'Hyundai': 'South Korea',
    'Fiat': 'Italy',
    'Nissan': 'Japan',
    'BMW': 'Germany',
    'Chevrolet': 'United States',
    'Kia': 'South Korea',
    'Peugeot': 'France'
}

# Print the entire dictionary
print("Car Brands Dictionary:", car_brands)

# Access and print the country of origin of the 3rd car brand
print("Country of origin of the 3rd car brand (Volkswagen):", car_brands['Volkswagen'])

# Update the country of origin of the 7th car brand
car_brands['BMW'] = 'Germany (updated)'  # Example update
print("Updated car brands dictionary:", car_brands)

# Delete the 8th car brand from the dictionary
del car_brands['Chevrolet']
print("Car brands dictionary after deletion:", car_brands)

# Print the last key-value pair in the dictionary
last_brand = list(car_brands.items())[-1]
print("Last key-value pair:", last_brand)
