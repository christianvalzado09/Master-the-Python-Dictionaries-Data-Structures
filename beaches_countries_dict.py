# beaches_countries_dict.py

# Create a dictionary of 8 beaches and the countries they are located in
beaches_countries = {
    'Bondi Beach': 'Australia',
    'Maui Beach': 'USA',
    'Copacabana Beach': 'Brazil',
    'Kuta Beach': 'Indonesia',
    'Waikiki Beach': 'USA',
    'Anse Source d’Argent': 'Seychelles',
    'Seven Mile Beach': 'Jamaica',
    'Navagio Beach': 'Greece'
}

# Print the entire dictionary
print("Beaches and their countries:", beaches_countries)

# Access and print the country of the 3rd beach (Copacabana Beach)
print("Country of the 3rd beach (Copacabana Beach):", beaches_countries['Copacabana Beach'])

# Update the country of the 6th beach (Anse Source d’Argent)
beaches_countries['Anse Source d’Argent'] = 'Seychelles, Indian Ocean'
print("Updated beaches and countries:", beaches_countries)

# Delete the 5th beach (Waikiki Beach) from the dictionary
del beaches_countries['Waikiki Beach']
print("Beaches and countries after deletion:", beaches_countries)

# Print the last key-value pair in the dictionary
last_beach_country = list(beaches_countries.items())[-1]
print("Last key-value pair:", last_beach_country)
