# country_capital_dict.py

# Create a dictionary of 12 countries and their capitals
country_capital = {
    'United States': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'United Kingdom': 'London',
    'Australia': 'Canberra',
    'India': 'New Delhi',
    'Brazil': 'Brasília',
    'Japan': 'Tokyo',
    'Germany': 'Berlin',
    'France': 'Paris',
    'South Africa': 'Pretoria',
    'Italy': 'Rome',
    'Mexico': 'Mexico City'
}

# Print the entire dictionary
print("Country-Capital Dictionary:", country_capital)

# Access and print the capital of the 5th country
print("Capital of the 5th country (India):", country_capital['India'])

# Update the capital of the 8th country
country_capital['Germany'] = 'Berlin (updated)'  # Example update
print("Updated country-capital dictionary:", country_capital)

# Delete the 11th country from the dictionary
del country_capital['Italy']
print("Country-capital dictionary after deletion:", country_capital)

# Print the last key-value pair in the dictionary
last_country = list(country_capital.items())[-1]
print("Last key-value pair:", last_country)
