# company_founders_dict.py

# Create a dictionary of 8 companies and their founders
company_founders = {
    'Apple': 'Steve Jobs, Steve Wozniak, Ronald Wayne',
    'Microsoft': 'Bill Gates, Paul Allen',
    'Amazon': 'Jeff Bezos',
    'Google': 'Larry Page, Sergey Brin',
    'Facebook': 'Mark Zuckerberg',
    'Tesla': 'Elon Musk, JB Straubel, Martin Eberhard, Marc Tarpenning',
    'Alibaba': 'Jack Ma',
    'SpaceX': 'Elon Musk'
}

# Print the entire dictionary
print("Company Founders Dictionary:", company_founders)

# Access and print the founder of the 6th company (Tesla)
print("Founder of the 6th company (Tesla):", company_founders['Tesla'])

# Update the founder of the 2nd company (Microsoft)
company_founders['Microsoft'] = 'Bill Gates'  # Example update
print("Updated company founders dictionary:", company_founders)

# Delete the 8th company (SpaceX) from the dictionary
del company_founders['SpaceX']
print("Company founders dictionary after deletion:", company_founders)

# Print the last key-value pair in the dictionary
last_company = list(company_founders.items())[-1]
print("Last key-value pair:", last_company)
