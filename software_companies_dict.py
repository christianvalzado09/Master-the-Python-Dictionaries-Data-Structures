# software_companies_dict.py

# Create a dictionary of 10 software companies and their headquarters
software_companies = {
    'Microsoft': 'Redmond, Washington, USA',
    'Apple': 'Cupertino, California, USA',
    'Google': 'Mountain View, California, USA',
    'Amazon': 'Seattle, Washington, USA',
    'Facebook': 'Menlo Park, California, USA',
    'IBM': 'Armonk, New York, USA',
    'Oracle': 'Austin, Texas, USA',
    'SAP': 'Walldorf, Germany',
    'Adobe': 'San Jose, California, USA',
    'Salesforce': 'San Francisco, California, USA'
}

# Print the entire dictionary
print("Software Companies Dictionary:", software_companies)

# Access and print the headquarters of the 3rd company
print("Headquarters of the 3rd company (Google):", software_companies['Google'])

# Update the headquarters of the 8th company
software_companies['SAP'] = 'Updated Headquarters Name'  # Example update
print("Updated software companies dictionary:", software_companies)

# Delete the 9th company from the dictionary
del software_companies['Adobe']
print("Software companies dictionary after deletion:", software_companies)

# Print the last key-value pair in the dictionary
last_company = list(software_companies.items())[-1]
print("Last key-value pair:", last_company)
