total_milk = 10
total_sugarcubes = 50
total_cookies = 20
total_coffee_sachets = 0
total_tea_leaves = 10

Coffee = bool(total_milk and total_coffee_sachets)
Tea = bool(total_milk and total_tea_leaves)




print(f"Can I get milk? :{bool(total_milk)}")
print(f"Can I get a coffee? :{bool(total_milk and total_coffee_sachets)}")
print(f"Can I get a Tea? :{bool(total_milk and total_tea_leaves)}")
print(f"Can I get some cookies? :{bool(total_cookies)}")


print(f"Can I get tea or coffee? :{bool(Coffee or Tea)}")
print(f"Can I get a coffee with some cookies? :{bool(Coffee and total_cookies)}")
print(f"Can I get a Tea with some cookies? :{bool(Tea and total_cookies)}")




