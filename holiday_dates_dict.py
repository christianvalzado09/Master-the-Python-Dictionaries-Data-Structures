# holiday_dates_dict.py

# Create a dictionary of 10 holidays and their corresponding dates
holiday_dates = {
    'New Year\'s Day': 'January 1',
    'Valentine\'s Day': 'February 14',
    'Easter': 'April 9',
    'Independence Day': 'July 4',
    'Halloween': 'October 31',
    'Thanksgiving': 'November 23',
    'Christmas': 'December 25',
    'New Year's Eve': 'December 31',
    'Labor Day': 'September 4',
    'Memorial Day': 'May 27'
}

# Print the entire dictionary
print("Holiday Dates Dictionary:", holiday_dates)

# Access and print the date of the 4th holiday
print("Date of the 4th holiday (Independence Day):", holiday_dates['Independence Day'])

# Update the date of the 9th holiday
holiday_dates['Labor Day'] = 'September 5'  # Example update
print("Updated holiday dates dictionary:", holiday_dates)

# Delete the 2nd holiday from the dictionary
del holiday_dates['Valentine\'s Day']
print("Holiday dates dictionary after deletion:", holiday_dates)

# Print the last key-value pair in the dictionary
last_holiday = list(holiday_dates.items())[-1]
print("Last key-value pair:", last_holiday)
