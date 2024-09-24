# space_missions_dict.py

# Create a dictionary of 5 space missions and their corresponding years
space_missions = {
    'Apollo 11': 1969,
    'Voyager 1': 1977,
    'Mars Rover Opportunity': 2004,
    'Space Shuttle Discovery': 1984,
    'International Space Station': 1998
}

# Print the entire dictionary
print("Space Missions Dictionary:", space_missions)

# Access and print the year of the 3rd mission
print("Year of the 3rd mission (Mars Rover Opportunity):", space_missions['Mars Rover Opportunity'])

# Update the year of the 2nd mission
space_missions['Voyager 1'] = 1978  # Example update
print("Updated space missions dictionary:", space_missions)

# Delete the 4th mission from the dictionary
del space_missions['Space Shuttle Discovery']
print("Space missions dictionary after deletion:", space_missions)

# Print the last key-value pair in the dictionary
last_mission = list(space_missions.items())[-1]
print("Last key-value pair:", last_mission)
