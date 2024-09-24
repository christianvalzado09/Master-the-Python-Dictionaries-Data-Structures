# software_versions_dict.py

# Create a dictionary of 6 software programs and their latest versions
software_versions = {
    'Windows': '11.0',
    'macOS': '13.5',
    'Ubuntu': '22.04',
    'Python': '3.11.4',
    'Microsoft Office': '2021',
    'Adobe Photoshop': '24.5'
}

# Print the entire dictionary
print("Software Versions Dictionary:", software_versions)

# Access and print the version of the 4th software
print("Version of the 4th software (Python):", software_versions['Python'])

# Update the version of the 2nd software (macOS)
software_versions['macOS'] = '14.0'  # Example update
print("Updated software versions dictionary:", software_versions)

# Delete the 5th software (Microsoft Office) from the dictionary
del software_versions['Microsoft Office']
print("Software versions dictionary after deletion:", software_versions)

# Print the last key-value pair in the dictionary
last_software = list(software_versions.items())[-1]
print("Last key-value pair:", last_software)
