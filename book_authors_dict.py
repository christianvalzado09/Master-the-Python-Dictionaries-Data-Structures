# book_authors_dict.py

# Create a dictionary of 12 books and their authors
book_authors = {
    'To Kill a Mockingbird': 'Harper Lee',
    '1984': 'George Orwell',
    'Pride and Prejudice': 'Jane Austen',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'Moby-Dick': 'Herman Melville',
    'War and Peace': 'Leo Tolstoy',
    'The Catcher in the Rye': 'J.D. Salinger',
    'The Hobbit': 'J.R.R. Tolkien',
    'Fahrenheit 451': 'Ray Bradbury',
    'Brave New World': 'Aldous Huxley',
    'The Grapes of Wrath': 'John Steinbeck',
    'Crime and Punishment': 'Fyodor Dostoevsky'
}

# Print the entire dictionary
print("Book Authors Dictionary:", book_authors)

# Access and print the author of the 9th book
print("Author of the 9th book (Fahrenheit 451):", book_authors['Fahrenheit 451'])

# Update the author of the 5th book
book_authors['Moby-Dick'] = 'Updated Author Name'  # Example update
print("Updated book authors dictionary:", book_authors)

# Delete the 3rd book from the dictionary
del book_authors['Pride and Prejudice']
print("Book authors dictionary after deletion:", book_authors)

# Print the last key-value pair in the dictionary
last_book = list(book_authors.items())[-1]
print("Last key-value pair:", last_book)
