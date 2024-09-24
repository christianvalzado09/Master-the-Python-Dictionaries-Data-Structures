# programming_languages_dict.py

# Create a dictionary of 7 programming languages and their developers
programming_languages = {
    'Python': 'Guido van Rossum',
    'Java': 'James Gosling',
    'C++': 'Bjarne Stroustrup',
    'JavaScript': 'Brendan Eich',
    'Ruby': 'Yukihiro Matsumoto',
    'Go': 'Robert Griesemer, Rob Pike, Ken Thompson',
    'Swift': 'Chris Lattner'
}

# Print the entire dictionary
print("Programming Languages Dictionary:", programming_languages)

# Access and print the developer of the 4th programming language
print("Developer of the 4th programming language (JavaScript):", programming_languages['JavaScript'])

# Update the developer of the 6th programming language
programming_languages['Go'] = 'Updated Developer Name'  # Example update
print("Updated programming languages dictionary:", programming_languages)

# Delete the 2nd programming language from the dictionary
del programming_languages['Java']
print("Programming languages dictionary after deletion:", programming_languages)

# Print the last key-value pair in the dictionary
last_language = list(programming_languages.items())[-1]
print("Last key-value pair:", last_language)
