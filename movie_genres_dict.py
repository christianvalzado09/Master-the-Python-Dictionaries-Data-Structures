# movie_genres_dict.py

# Create a dictionary of 8 movie genres and their corresponding example movies
movie_genres = {
    'Action': 'Mad Max: Fury Road',
    'Comedy': 'Superbad',
    'Drama': 'The Shawshank Redemption',
    'Horror': 'Get Out',
    'Science Fiction': 'Inception',
    'Fantasy': 'The Lord of the Rings',
    'Thriller': 'Gone Girl',
    'Romance': 'Pride and Prejudice'
}

# Print the entire dictionary
print("Movie Genres Dictionary:", movie_genres)

# Access and print the example movie of the 3rd genre
print("Example movie of the 3rd genre (Drama):", movie_genres['Drama'])

# Update the example movie of the 5th genre
movie_genres['Science Fiction'] = 'Interstellar'  # Example update
print("Updated movie genres dictionary:", movie_genres)

# Delete the 7th genre from the dictionary
del movie_genres['Thriller']
print("Movie genres dictionary after deletion:", movie_genres)

# Print the last key-value pair in the dictionary
last_genre = list(movie_genres.items())[-1]
print("Last key-value pair:", last_genre)
