# athlete_achievements_dict.py

# Create a dictionary of 8 athletes and their greatest achievements
athlete_achievements = {
    'Usain Bolt': 'World Record in 100m and 200m',
    'Michael Phelps': 'Most Olympic Gold Medals',
    'Serena Williams': 'Grand Slam Titles',
    'Lionel Messi': 'FIFA Ballon d\'Or Titles',
    'LeBron James': 'NBA Championships',
    'Roger Federer': 'Most Wimbledon Titles',
    'Tom Brady': 'Super Bowl Championships',
    'Simone Biles': 'World Championship Medals'
}

# Print the entire dictionary
print("Athlete Achievements Dictionary:", athlete_achievements)

# Access and print the achievement of the 5th athlete
print("Achievement of the 5th athlete (LeBron James):", athlete_achievements['LeBron James'])

# Update the achievement of the 3rd athlete
athlete_achievements['Serena Williams'] = 'Winning 23 Grand Slam Singles Titles'  # Example update
print("Updated athlete achievements dictionary:", athlete_achievements)

# Delete the 7th athlete from the dictionary
del athlete_achievements['Tom Brady']
print("Athlete achievements dictionary after deletion:", athlete_achievements)

# Print the last key-value pair in the dictionary
last_athlete = list(athlete_achievements.items())[-1]
print("Last key-value pair:", last_athlete)
