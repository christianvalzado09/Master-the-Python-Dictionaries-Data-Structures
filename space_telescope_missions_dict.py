# space_telescope_missions_dict.py

# Create a dictionary of 5 space telescopes and their missions
space_telescope_missions = {
    'Hubble Space Telescope': 'Observing deep space and distant galaxies',
    'Chandra X-ray Observatory': 'X-ray astronomy and studying high-energy phenomena',
    'Kepler Space Telescope': 'Searching for exoplanets',
    'James Webb Space Telescope': 'Studying the formation of stars and galaxies',
    'Spitzer Space Telescope': 'Infrared astronomy and studying dust clouds and cooler objects'
}

# Print the entire dictionary
print("Space telescope missions dictionary:", space_telescope_missions)

# Access and print the mission of the 3rd telescope (Kepler Space Telescope)
print("Mission of the 3rd telescope (Kepler):", space_telescope_missions['Kepler Space Telescope'])

# Update the mission of the 1st telescope (Hubble Space Telescope)
space_telescope_missions['Hubble Space Telescope'] = 'Studying the universe and its evolution'
print("Updated space telescope missions dictionary:", space_telescope_missions)

# Delete the 4th telescope (James Webb Space Telescope) from the dictionary
del space_telescope_missions['James Webb Space Telescope']
print("Space telescope missions dictionary after deletion:", space_telescope_missions)

# Print the last key-value pair in the dictionary
last_telescope_mission = list(space_telescope_missions.items())[-1]
print("Last key-value pair:", last_telescope_mission)
