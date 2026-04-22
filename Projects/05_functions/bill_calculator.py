from random import randint

cups = [1,3,4,2,3,4,5]
price_per_cup = 10


def calculate_bill(cups, price_per_cup):
    bill_amount = cups * price_per_cup
    print(f"Total bill amount is {bill_amount}")


for item in cups:
    calculate_bill(item, price_per_cup)


