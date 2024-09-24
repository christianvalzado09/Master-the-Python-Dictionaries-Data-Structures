# historical_events_dict.py

# Create a dictionary of 8 historical events and their years
historical_events = {
    'Moon Landing': 1969,
    'World War II Ends': 1945,
    'Fall of Berlin Wall': 1989,
    'Discovery of Penicillin': 1928,
    'Signing of Magna Carta': 1215,
    'American Revolution': 1776,
    'First Flight by Wright Brothers': 1903,
    'Invention of the Printing Press': 1440
}

# Print the entire dictionary
print("Historical events and their years:", historical_events)

# Access and print the year of the 2nd event (World War II Ends)
print("Year of the 2nd event (World War II Ends):", historical_events['World War II Ends'])

# Update the year of the 7th event (First Flight by Wright Brothers)
historical_events['First Flight by Wright Brothers'] = 1902  # Example update
print("Updated historical events dictionary:", historical_events)

# Delete the 5th event (Signing of Magna Carta) from the dictionary
del historical_events['Signing of Magna Carta']
print("Historical events dictionary after deletion:", historical_events)

# Print the last key-value pair in the dictionary
last_event_year = list(historical_events.items())[-1]
print("Last key-value pair:", last_event_year)
