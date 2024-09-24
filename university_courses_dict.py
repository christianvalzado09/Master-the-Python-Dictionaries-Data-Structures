# university_courses_dict.py

# Create a dictionary of 8 universities and their popular courses
university_courses = {
    'Harvard University': 'Law',
    'Stanford University': 'Business',
    'Massachusetts Institute of Technology': 'Engineering',
    'California Institute of Technology': 'Physics',
    'University of Cambridge': 'Mathematics',
    'University of Oxford': 'Philosophy',
    'University of Chicago': 'Economics',
    'Columbia University': 'Journalism'
}

# Print the entire dictionary
print("University Courses Dictionary:", university_courses)

# Access and print the course of the 3rd university
print("Popular course of the 3rd university (Massachusetts Institute of Technology):", university_courses['Massachusetts Institute of Technology'])

# Update the course of the 5th university
university_courses['University of Cambridge'] = 'Updated Popular Course'  # Example update
print("Updated university courses dictionary:", university_courses)

# Delete the 7th university from the dictionary
del university_courses['University of Chicago']
print("University courses dictionary after deletion:", university_courses)

# Print the last key-value pair in the dictionary
last_university = list(university_courses.items())[-1]
print("Last key-value pair:", last_university)
