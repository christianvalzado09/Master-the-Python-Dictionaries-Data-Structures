# author_books_dict.py

# Create a dictionary of 8 authors and their famous books
author_books = {
    'J.K. Rowling': 'Harry Potter and the Sorcerer\'s Stone',
    'George Orwell': '1984',
    'J.R.R. Tolkien': 'The Hobbit',
    'F. Scott Fitzgerald': 'The Great Gatsby',
    'Mark Twain': 'Adventures of Huckleberry Finn',
    'Jane Austen': 'Pride and Prejudice',
    'Harper Lee': 'To Kill a Mockingbird',
    'Ernest Hemingway': 'The Old Man and the Sea'
}

# Print the entire dictionary
print("Authors and their famous books:", author_books)

# Access and print the book of the 5th author (Mark Twain)
print("Book of the 5th author (Mark Twain):", author_books['Mark Twain'])

# Update the book of the 7th author (Harper Lee)
author_books['Harper Lee'] = 'Go Set a Watchman'
print("Updated authors and their books:", author_books)

# Delete the 6th author (Jane Austen) from the dictionary
del author_books['Jane Austen']
print("Authors and their books after deletion:", author_books)

# Print the last key-value pair in the dictionary
last_author_book = list(author_books.items())[-1]
print("Last key-value pair:", last_author_book)
