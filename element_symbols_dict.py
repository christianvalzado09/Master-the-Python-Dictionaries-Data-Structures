# element_symbols_dict.py

# Create a dictionary of 10 elements and their chemical symbols
element_symbols = {
    'Hydrogen': 'H',
    'Helium': 'He',
    'Lithium': 'Li',
    'Beryllium': 'Be',
    'Boron': 'B',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Fluorine': 'F',
    'Neon': 'Ne'
}

# Print the entire dictionary
print("Element Symbols Dictionary:", element_symbols)

# Access and print the symbol of the 6th element
print("Symbol of the 6th element (Carbon):", element_symbols['Carbon'])

# Update the symbol of the 8th element
element_symbols['Oxygen'] = 'O2'  # Example update
print("Updated element symbols dictionary:", element_symbols)

# Delete the 9th element from the dictionary
del element_symbols['Fluorine']
print("Element symbols dictionary after deletion:", element_symbols)

# Print the last key-value pair in the dictionary
last_element = list(element_symbols.items())[-1]
print("Last key-value pair:", last_element)
