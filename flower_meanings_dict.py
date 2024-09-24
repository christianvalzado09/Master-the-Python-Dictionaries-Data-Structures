# flower_meanings_dict.py

# Create a dictionary of 8 flowers and their symbolic meanings
flower_meanings = {
    'Rose': 'Love and passion',
    'Lily': 'Purity and refined beauty',
    'Tulip': 'Perfect love',
    'Daisy': 'Innocence and purity',
    'Sunflower': 'Adoration and loyalty',
    'Orchid': 'Exotic beauty',
    'Chrysanthemum': 'Cheerfulness and optimism',
    'Lavender': 'Calmness and devotion'
}

# Print the entire dictionary
print("Flower Meanings Dictionary:", flower_meanings)

# Access and print the meaning of the 5th flower
print("Meaning of the 5th flower (Sunflower):", flower_meanings['Sunflower'])

# Update the meaning of the 7th flower
flower_meanings['Chrysanthemum'] = 'Friendship and happiness'  # Example update
print("Updated flower meanings dictionary:", flower_meanings)

# Delete the 6th flower from the dictionary
del flower_meanings['Orchid']
print("Flower meanings dictionary after deletion:", flower_meanings)

# Print the last key-value pair in the dictionary
last_flower = list(flower_meanings.items())[-1]
print("Last key-value pair:", last_flower)
