menu = ["Coffee", "Tea", "Cookies", "Coffee", "Coffee", "Tea", "Cookies", "Coffee", "Coffee", "Tea", "Cookies", "Coffee"]

filter_coffee = list(filter(lambda items : items == "Coffee", menu))
filter_rest = list(filter(lambda items : items != "Coffee", menu))

full_menu = filter_coffee + filter_rest

print(f"Filter Coffee: {filter_coffee}")
print(f"Filter Rest: {filter_rest}")
print(f"Full menu = {full_menu}")



