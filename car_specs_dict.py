# car_specs_dict.py

# Create a dictionary of 10 car models and their engine specifications
car_specs = {
    'Toyota Corolla': '1.8L 4-cylinder',
    'Honda Civic': '2.0L 4-cylinder',
    'Ford Mustang': '5.0L V8',
    'Chevrolet Camaro': '6.2L V8',
    'BMW 3 Series': '2.0L 4-cylinder',
    'Audi A4': '2.0L Turbocharged 4-cylinder',
    'Mercedes-Benz C-Class': '2.0L 4-cylinder',
    'Tesla Model S': 'Electric Motor',
    'Nissan GT-R': '3.8L Twin-Turbo V6',
    'Porsche 911': '3.0L Twin-Turbocharged Flat-6'
}

# Print the entire dictionary
print("Car Models and Engine Specifications:", car_specs)

# Access and print the specifications of the 4th car model (Chevrolet Camaro)
print("Specifications of the 4th car model (Chevrolet Camaro):", car_specs['Chevrolet Camaro'])

# Update the specifications of the 9th car model (Nissan GT-R)
car_specs['Nissan GT-R'] = '3.8L V6 Turbo'  # Example update
print("Updated car specifications dictionary:", car_specs)

# Delete the 5th car model (BMW 3 Series) from the dictionary
del car_specs['BMW 3 Series']
print("Car specifications dictionary after deletion:", car_specs)

# Print the last key-value pair in the dictionary
last_car = list(car_specs.items())[-1]
print("Last key-value pair:", last_car)
