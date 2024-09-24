# city_landmarks_dict.py

# Create a dictionary of 8 cities and their famous landmarks
city_landmarks = {
    'Paris': 'Eiffel Tower',
    'New York': 'Statue of Liberty',
    'London': 'Big Ben',
    'Rome': 'Colosseum',
    'Tokyo': 'Tokyo Tower',
    'Sydney': 'Sydney Opera House',
    'Berlin': 'Brandenburg Gate',
    'Beijing': 'Great Wall of China'
}

# Print the entire dictionary
print("City landmarks dictionary:", city_landmarks)

# Access and print the landmark of the 6th city (Sydney)
print("The landmark of the 6th city (Sydney):", city_landmarks['Sydney'])

# Update the landmark of the 2nd city (New York)
city_landmarks['New York'] = 'One World Trade Center'
print("Updated city landmarks dictionary:", city_landmarks)

# Delete the 7th city (Berlin) from the dictionary
del city_landmarks['Berlin']
print("City landmarks dictionary after deletion:", city_landmarks)

# Print the last key-value pair in the dictionary
last_city_landmark = list(city_landmarks.items())[-1]
print("Last key-value pair:", last_city_landmark)
