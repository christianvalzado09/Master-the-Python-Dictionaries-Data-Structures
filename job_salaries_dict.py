# job_salaries_dict.py

# Create a dictionary of 10 jobs and their average salaries
job_salaries = {
    'Software Engineer': 85000,
    'Data Scientist': 95000,
    'Web Developer': 75000,
    'Graphic Designer': 60000,
    'Project Manager': 90000,
    'Product Manager': 110000,
    'UX Designer': 80000,
    'Database Administrator': 78000,
    'Systems Analyst': 74000,
    'Network Engineer': 70000
}

# Print the entire dictionary
print("Job salaries dictionary:", job_salaries)

# Access and print the salary of the 3rd job (Web Developer)
print("Salary of the 3rd job (Web Developer):", job_salaries['Web Developer'])

# Update the salary of the 7th job (UX Designer)
job_salaries['UX Designer'] = 85000
print("Updated job salaries dictionary:", job_salaries)

# Delete the 9th job (Systems Analyst) from the dictionary
del job_salaries['Systems Analyst']
print("Job salaries dictionary after deletion:", job_salaries)

# Print the last key-value pair in the dictionary
last_job_salary = list(job_salaries.items())[-1]
print("Last key-value pair:", last_job_salary)
