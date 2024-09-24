# product_prices_dict.py

# Create a dictionary of 10 products and their prices
product_prices = {
    'Laptop': 1200.00,
    'Smartphone': 800.00,
    'Tablet': 400.00,
    'Headphones': 150.00,
    'Smartwatch': 250.00,
    'Camera': 600.00,
    'Printer': 300.00,
    'Monitor': 350.00,
    'External Hard Drive': 120.00,
    'Keyboard': 50.00
}

# Print the entire dictionary
print("Product Prices Dictionary:", product_prices)

# Access and print the price of the 4th product
print("Price of the 4th product (Headphones):", product_prices['Headphones'])

# Update the price of the 9th product
product_prices['External Hard Drive'] = 110.00  # Example update
print("Updated product prices dictionary:", product_prices)

# Delete the 6th product from the dictionary
del product_prices['Camera']
print("Product prices dictionary after deletion:", product_prices)

# Print the last key-value pair in the dictionary
last_product = list(product_prices.items())[-1]
print("Last key-value pair:", last_product)
