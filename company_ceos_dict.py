# company_ceos_dict.py

# Create a dictionary of 10 companies and their current CEOs
company_ceos = {
    'Apple': 'Tim Cook',
    'Microsoft': 'Satya Nadella',
    'Amazon': 'Andy Jassy',
    'Google': 'Sundar Pichai',
    'Facebook': 'Mark Zuckerberg',
    'Tesla': 'Elon Musk',
    'Berkshire Hathaway': 'Warren Buffett',
    'Coca-Cola': 'James Quincey',
    'Samsung': 'Jong-Hee Han',
    'Toyota': 'Akio Toyoda'
}

# Print the entire dictionary
print("Company CEOs Dictionary:", company_ceos)

# Access and print the CEO of the 6th company
print("CEO of the 6th company (Tesla):", company_ceos['Tesla'])

# Update the CEO of the 3rd company
company_ceos['Amazon'] = 'New CEO Name'  # Example update
print("Updated company CEOs dictionary:", company_ceos)

# Delete the 9th company from the dictionary
del company_ceos['Samsung']
print("Company CEOs dictionary after deletion:", company_ceos)

# Print the last key-value pair in the dictionary
last_company = list(company_ceos.items())[-1]
print("Last key-value pair:", last_company)
