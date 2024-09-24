# artist_songs_dict.py

# Create a dictionary of 8 artists and their top songs
artist_songs = {
    'Taylor Swift': 'Blank Space',
    'Ed Sheeran': 'Shape of You',
    'Beyoncé': 'Halo',
    'Drake': 'God\'s Plan',
    'Adele': 'Hello',
    'Bruno Mars': 'Uptown Funk',
    'Billie Eilish': 'Bad Guy',
    'The Weeknd': 'Blinding Lights'
}

# Print the entire dictionary
print("Artists and their top songs:", artist_songs)

# Access and print the top song of the 3rd artist (Beyoncé)
print("Top song of the 3rd artist (Beyoncé):", artist_songs['Beyoncé'])

# Update the top song of the 6th artist (Bruno Mars)
artist_songs['Bruno Mars'] = '24K Magic'  # Example update
print("Updated artist-songs dictionary:", artist_songs)

# Delete the 7th artist (Billie Eilish) from the dictionary
del artist_songs['Billie Eilish']
print("Artist-songs dictionary after deletion:", artist_songs)

# Print the last key-value pair in the dictionary
last_artist_song = list(artist_songs.items())[-1]
print("Last key-value pair:", last_artist_song)
