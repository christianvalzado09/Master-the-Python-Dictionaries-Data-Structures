# dinosaur_fossils_dict.py

# Create a dictionary of 7 dinosaurs and where their fossils were found
dinosaur_fossils = {
    'Tyrannosaurus Rex': 'North America',
    'Triceratops': 'North America',
    'Brachiosaurus': 'North America',
    'Stegosaurus': 'North America',
    'Velociraptor': 'Asia',
    'Ankylosaurus': 'North America',
    'Spinosaurus': 'Africa'
}

# Print the entire dictionary
print("Dinosaur fossils dictionary:", dinosaur_fossils)

# Access and print the location of the 4th dinosaur's fossils (Stegosaurus)
print("Location of the 4th dinosaur's fossils (Stegosaurus):", dinosaur_fossils['Stegosaurus'])

# Update the location of the 2nd dinosaur's fossils (Triceratops)
dinosaur_fossils['Triceratops'] = 'Western North America'
print("Updated dinosaur fossils dictionary:", dinosaur_fossils)

# Delete the 6th dinosaur (Ankylosaurus) from the dictionary
del dinosaur_fossils['Ankylosaurus']
print("Dinosaur fossils dictionary after deletion:", dinosaur_fossils)

# Print the last key-value pair in the dictionary
last_dinosaur_fossil = list(dinosaur_fossils.items())[-1]
print("Last key-value pair:", last_dinosaur_fossil)
