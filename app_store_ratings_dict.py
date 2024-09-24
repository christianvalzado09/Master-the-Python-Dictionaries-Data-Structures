# app_store_ratings_dict.py

# Create a dictionary of 10 apps and their user ratings
app_store_ratings = {
    'Facebook': 4.2,
    'Instagram': 4.5,
    'Twitter': 4.1,
    'Snapchat': 4.3,
    'WhatsApp': 4.7,
    'YouTube': 4.6,
    'Spotify': 4.8,
    'TikTok': 4.4,
    'Pinterest': 4.0,
    'LinkedIn': 4.3
}

# Print the entire dictionary
print("App Store Ratings Dictionary:", app_store_ratings)

# Access and print the rating of the 6th app
print("Rating of the 6th app (YouTube):", app_store_ratings['YouTube'])

# Update the rating of the 8th app
app_store_ratings['TikTok'] = 4.9  # Example update
print("Updated app store ratings dictionary:", app_store_ratings)

# Delete the 9th app from the dictionary
del app_store_ratings['Pinterest']
print("App store ratings dictionary after deletion:", app_store_ratings)

# Print the last key-value pair in the dictionary
last_app = list(app_store_ratings.items())[-1]
print("Last key-value pair:", last_app)
