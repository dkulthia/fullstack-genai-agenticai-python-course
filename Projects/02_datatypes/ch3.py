#integers
servings = 4
total_milk = 10
milk_per_serving = total_milk / servings

print(f"Milk per serving is {milk_per_serving} litres")

total_sugarcubes = 7
sugarcubes_per_serving = total_sugarcubes // servings

    
print(f"There will be {sugarcubes_per_serving} sugarcubes per serving")

total_coffee_sachets = 10
coffee_sachets_per_serving = 2
leftover_coffee_sachets = total_coffee_sachets % (coffee_sachets_per_serving * servings)


print(f"There will be {coffee_sachets_per_serving} Coffee Sachets per serving")
print(f"There will be {leftover_coffee_sachets} leftover Coffee Sachets")

