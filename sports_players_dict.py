# sports_players_dict.py

# Create a dictionary of 10 sports and their most famous players
sports_players = {
    'Soccer': 'Lionel Messi',
    'Basketball': 'Michael Jordan',
    'Tennis': 'Roger Federer',
    'Cricket': 'Sachin Tendulkar',
    'Boxing': 'Muhammad Ali',
    'Golf': 'Tiger Woods',
    'Swimming': 'Michael Phelps',
    'Formula 1': 'Lewis Hamilton',
    'Baseball': 'Babe Ruth',
    'Hockey': 'Wayne Gretzky'
}

# Print the entire dictionary
print("Sports Players Dictionary:", sports_players)

# Access and print the player of the 4th sport
print("Famous player of the 4th sport (Cricket):", sports_players['Cricket'])

# Update the player of the 6th sport
sports_players['Golf'] = 'Updated Famous Player'  # Example update
print("Updated sports players dictionary:", sports_players)

# Delete the 10th sport from the dictionary
del sports_players['Hockey']
print("Sports players dictionary after deletion:", sports_players)

# Print the last key-value pair in the dictionary
last_sport = list(sports_players.items())[-1]
print("Last key-value pair:", last_sport)
