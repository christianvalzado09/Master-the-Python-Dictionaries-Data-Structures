# movie_directors_dict.py

# Create a dictionary of 10 movies and their directors
movie_directors = {
    'Inception': 'Christopher Nolan',
    'The Godfather': 'Francis Ford Coppola',
    'Pulp Fiction': 'Quentin Tarantino',
    'The Dark Knight': 'Christopher Nolan',
    'Forrest Gump': 'Robert Zemeckis',
    'The Shawshank Redemption': 'Frank Darabont',
    'The Matrix': 'Lana and Lilly Wachowski',
    'Fight Club': 'David Fincher',
    'The Social Network': 'David Fincher',
    'Interstellar': 'Christopher Nolan'
}

# Print the entire dictionary
print("Movie Directors Dictionary:", movie_directors)

# Access and print the director of the 5th movie
print("Director of the 5th movie (Forrest Gump):", movie_directors['Forrest Gump'])

# Update the director of the 9th movie
movie_directors['The Social Network'] = 'Updated Director Name'  # Example update
print("Updated movie directors dictionary:", movie_directors)

# Delete the 7th movie from the dictionary
del movie_directors['The Matrix']
print("Movie directors dictionary after deletion:", movie_directors)

# Print the last key-value pair in the dictionary
last_movie = list(movie_directors.items())[-1]
print("Last key-value pair:", last_movie)
