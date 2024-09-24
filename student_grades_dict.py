# student_grades_dict.py

# Create a dictionary of 5 students and their corresponding grades
student_grades = {
    'Student1': 'A',
    'Student2': 'B',
    'Student3': 'C',
    'Student4': 'B',
    'Student5': 'A'
}

# Print the entire dictionary
print("Student Grades Dictionary:", student_grades)

# Access and print the grade of the 3rd student
print("Grade of third student:", student_grades['Student3'])

# Update the grade of the 2nd student
student_grades['Student2'] = 'A'
print("Updated grades dictionary:", student_grades)

# Delete the entry of the 5th student
del student_grades['Student5']
print("Grades dictionary after deletion:", student_grades)

# Print the last key-value pair in the dictionary
last_student = list(student_grades.items())[-1]
print("Last key-value pair:", last_student)
