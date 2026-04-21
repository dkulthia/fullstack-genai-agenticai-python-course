menu = ["Tea", "coffee", "cookies", "discontinued", "out of order"]

for item in menu:
    if item == "discontinued":
        print(f"{item} is out of stock!!")
        continue
    elif item == "out of order":
        print(f"{item} is Discontinued!!")
        break
    else:
        print(f"{item} is available")
