# sports_events_dict.py

# Create a dictionary of 7 sports events and their corresponding years
sports_events = {
    'FIFA World Cup': 2018,
    'Olympic Games': 2020,
    'Super Bowl': 2021,
    'UEFA Champions League': 2021,
    'NBA Finals': 2022,
    'Wimbledon': 2022,
    'Tour de France': 2023
}

# Print the entire dictionary
print("Sports Events and their years:", sports_events)

# Access and print the year of the 3rd sports event (Super Bowl)
print("Year of the 3rd sports event (Super Bowl):", sports_events['Super Bowl'])

# Update the year of the 6th sports event (Wimbledon)
sports_events['Wimbledon'] = 2023
print("Updated sports events and years:", sports_events)

# Delete the 5th sports event (NBA Finals) from the dictionary
del sports_events['NBA Finals']
print("Sports events and years after deletion:", sports_events)

# Print the last key-value pair in the dictionary
last_event_year = list(sports_events.items())[-1]
print("Last key-value pair:", last_event_year)
