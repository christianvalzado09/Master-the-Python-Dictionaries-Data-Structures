# festival_dates_dict.py

# Create a dictionary of 10 festivals and their celebration dates
festival_dates = {
    'Christmas': 'December 25',
    'Eid al-Fitr': 'Varies by lunar calendar',
    'Diwali': 'November 12',
    'Thanksgiving': 'November 28',
    'Chinese New Year': 'February 10',
    'Holi': 'March 29',
    'Hanukkah': 'December 7',
    'Oktoberfest': 'September 21',
    'Valentine’s Day': 'February 14',
    'Bastille Day': 'July 14'
}

# Print the entire dictionary
print("Festival Dates Dictionary:", festival_dates)

# Access and print the date of the 3rd festival (Diwali)
print("Date of the 3rd festival (Diwali):", festival_dates['Diwali'])

# Update the date of the 7th festival (Hanukkah)
festival_dates['Hanukkah'] = 'December 8'  # Example update
print("Updated festival dates dictionary:", festival_dates)

# Delete the 5th festival (Chinese New Year) from the dictionary
del festival_dates['Chinese New Year']
print("Festival dates dictionary after deletion:", festival_dates)

# Print the last key-value pair in the dictionary
last_festival = list(festival_dates.items())[-1]
print("Last key-value pair:", last_festival)
