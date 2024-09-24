# food_recipes_dict.py

# Create a dictionary of 8 foods and their recipes
food_recipes = {
    'Pasta': 'Boil pasta, add sauce, and serve.',
    'Pizza': 'Prepare dough, add toppings, bake until golden.',
    'Tacos': 'Fill tortillas with meat, cheese, and veggies.',
    'Salad': 'Mix greens, veggies, and dressing.',
    'Sushi': 'Roll rice, fish, and vegetables in seaweed.',
    'Curry': 'Cook meat and veggies with spices and coconut milk.',
    'Soup': 'Simmer ingredients in broth until tender.',
    'Brownies': 'Mix ingredients, bake, and cut into squares.'
}

# Print the entire dictionary
print("Food recipes dictionary:", food_recipes)

# Access and print the recipe of the 5th food (Sushi)
print("Recipe of the 5th food (Sushi):", food_recipes['Sushi'])

# Update the recipe of the 3rd food (Tacos)
food_recipes['Tacos'] = 'Fill tortillas with seasoned meat, cheese, and salsa.'
print("Updated food recipes dictionary:", food_recipes)

# Delete the 7th food (Soup) from the dictionary
del food_recipes['Soup']
print("Food recipes dictionary after deletion:", food_recipes)

# Print the last key-value pair in the dictionary
last_food_recipe = list(food_recipes.items())[-1]
print("Last key-value pair:", last_food_recipe)
