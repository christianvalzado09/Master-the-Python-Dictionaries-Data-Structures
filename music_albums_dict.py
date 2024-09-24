# music_albums_dict.py

# Create a dictionary of 10 music albums and their release years
music_albums = {
    'Thriller': 1982,
    'Back in Black': 1980,
    'The Dark Side of the Moon': 1973,
    'Rumours': 1977,
    'The Wall': 1979,
    'Abbey Road': 1969,
    'Led Zeppelin IV': 1971,
    'Hotel California': 1976,
    'Born in the U.S.A.': 1984,
    'Sgt. Pepper’s Lonely Hearts Club Band': 1967
}

# Print the entire dictionary
print("Music albums dictionary:", music_albums)

# Access and print the release year of the 3rd album (The Dark Side of the Moon)
print("The release year of the 3rd album (The Dark Side of the Moon):", music_albums['The Dark Side of the Moon'])

# Update the release year of the 8th album (Hotel California)
music_albums['Hotel California'] = 1977
print("Updated music albums dictionary:", music_albums)

# Delete the 5th album (The Wall) from the dictionary
del music_albums['The Wall']
print("Music albums dictionary after deletion:", music_albums)

# Print the last key-value pair in the dictionary
last_album = list(music_albums.items())[-1]
print("Last key-value pair:", last_album)
