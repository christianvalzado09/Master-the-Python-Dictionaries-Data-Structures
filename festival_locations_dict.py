# festival_locations_dict.py

# Create a dictionary of 8 festivals and their locations
festival_locations = {
    'Diwali': 'India',
    'Oktoberfest': 'Germany',
    'Carnival': 'Brazil',
    'Holi': 'India',
    'Mardi Gras': 'USA',
    'La Tomatina': 'Spain',
    'Gion Matsuri': 'Japan',
    'Burning Man': 'USA'
}

# Print the entire dictionary
print("Festival locations dictionary:", festival_locations)

# Access and print the location of the 4th festival (Holi)
print("Location of the 4th festival (Holi):", festival_locations['Holi'])

# Update the location of the 6th festival (La Tomatina)
festival_locations['La Tomatina'] = 'Buñol, Spain'
print("Updated festival locations dictionary:", festival_locations)

# Delete the 2nd festival (Oktoberfest) from the dictionary
del festival_locations['Oktoberfest']
print("Festival locations dictionary after deletion:", festival_locations)

# Print the last key-value pair in the dictionary
last_festival_location = list(festival_locations.items())[-1]
print("Last key-value pair:", last_festival_location)
