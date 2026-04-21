menu = ["Tea", "coffee", "cookies"]

listed_menu = list(enumerate(menu, start=1))



for item_number, item_name in listed_menu:
    print(f"{item_number}. {item_name}")



