# state_capitals_dict.py

# Create a dictionary of 10 states and their capitals
state_capitals = {
    'California': 'Sacramento',
    'Texas': 'Austin',
    'Florida': 'Tallahassee',
    'New York': 'Albany',
    'Illinois': 'Springfield',
    'Pennsylvania': 'Harrisburg',
    'Ohio': 'Columbus',
    'Georgia': 'Atlanta',
    'Michigan': 'Lansing',
    'Washington': 'Olympia'
}

# Print the entire dictionary
print("State capitals dictionary:", state_capitals)

# Access and print the capital of the 4th state (New York)
print("The capital of the 4th state (New York):", state_capitals['New York'])

# Update the capital of the 9th state (Michigan)
state_capitals['Michigan'] = 'Detroit'  # Example update
print("Updated state capitals dictionary:", state_capitals)

# Delete the 7th state (Ohio) from the dictionary
del state_capitals['Ohio']
print("State capitals dictionary after deletion:", state_capitals)

# Print the last key-value pair in the dictionary
last_state_capital = list(state_capitals.items())[-1]
print("Last key-value pair:", last_state_capital)
