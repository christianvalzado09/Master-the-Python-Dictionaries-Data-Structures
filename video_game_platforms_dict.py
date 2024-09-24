# video_game_platforms_dict.py

# Create a dictionary of 8 video games and their platforms
video_game_platforms = {
    'The Legend of Zelda: Breath of the Wild': 'Nintendo Switch',
    'God of War': 'PlayStation 4',
    'Halo Infinite': 'Xbox Series X',
    'Super Mario Odyssey': 'Nintendo Switch',
    'The Witcher 3: Wild Hunt': 'PC',
    'Minecraft': 'Multi-platform',
    'Fortnite': 'Multi-platform',
    'Cyberpunk 2077': 'PC, PS4, Xbox One'
}

# Print the entire dictionary
print("Video Game Platforms Dictionary:", video_game_platforms)

# Access and print the platform of the 2nd video game
print("Platform of the 2nd video game (God of War):", video_game_platforms['God of War'])

# Update the platform of the 6th video game
video_game_platforms['Minecraft'] = 'Xbox, PlayStation, Nintendo Switch, PC'  # Example update
print("Updated video game platforms dictionary:", video_game_platforms)

# Delete the 4th video game from the dictionary
del video_game_platforms['Super Mario Odyssey']
print("Video game platforms dictionary after deletion:", video_game_platforms)

# Print the last key-value pair in the dictionary
last_game = list(video_game_platforms.items())[-1]
print("Last key-value pair:", last_game)
