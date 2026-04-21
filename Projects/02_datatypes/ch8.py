from random import random
from random import shuffle

ingredients = ["Coffee Beans", "Tea leaves", "whey protein"]
print(f"Default: {ingredients}")

ingredients.append("Sattu")
print(f"Added Sattu: {ingredients}")


ingredients.remove("Sattu")
print(f"Removed Sattu: {ingredients}")

ingredients.append("Sattu")
print(f"Again added Sattu: {ingredients}")

ingredients.sort()
print(f"Sorted: {ingredients}")


ingredients.reverse()
print(f"Reversed: {ingredients}")


ingredients = ingredients[::-1]
print(f"Reversed: {ingredients}")


ingredients = list(reversed(ingredients))
print(f"Reversed: {ingredients}")


shuffle(ingredients)
print(f"Random : {ingredients}")

shuffle(ingredients)
print(f"Random : {ingredients}")











last_ingredient = ingredients.pop()
print(f"last ingredients: {last_ingredient}")
ingredients.append(f"{last_ingredient}")


sugar_levels = ["1", "2", "3", "4", "5"]

max_sugar_level = max(sugar_levels)
min_sugar_level = min(sugar_levels)

print(f"Max Sugar level : {max_sugar_level}")
print(f"Min Sugar level : {min_sugar_level}")




basic_drinks = ["Water", "Milk"]
special_drinks = ["Coffee", "Tea", "Protien Drink", "Sattu"]

all_drinks = basic_drinks + special_drinks

print(f"All Drinks : {all_drinks}")

















ingredients.reverse()
print(f"Reversed: {ingredients}")

ingredients.clear()
print(f"Clear: {ingredients}")














