# currency_symbols_dict.py

# Create a dictionary of 10 currencies and their symbols
currency_symbols = {
    'United States Dollar': '$',
    'Euro': '€',
    'British Pound': '£',
    'Japanese Yen': '¥',
    'Australian Dollar': 'A$',
    'Canadian Dollar': 'C$',
    'Swiss Franc': 'CHF',
    'Chinese Yuan': '¥',
    'Indian Rupee': '₹',
    'South African Rand': 'R'
}

# Print the entire dictionary
print("Currency Symbols Dictionary:", currency_symbols)

# Access and print the symbol of the 5th currency
print("Symbol of the 5th currency (Australian Dollar):", currency_symbols['Australian Dollar'])

# Update the symbol of the 9th currency
currency_symbols['Indian Rupee'] = 'INR'  # Example update
print("Updated currency symbols dictionary:", currency_symbols)

# Delete the 3rd currency from the dictionary
del currency_symbols['British Pound']
print("Currency symbols dictionary after deletion:", currency_symbols)

# Print the last key-value pair in the dictionary
last_currency = list(currency_symbols.items())[-1]
print("Last key-value pair:", last_currency)
