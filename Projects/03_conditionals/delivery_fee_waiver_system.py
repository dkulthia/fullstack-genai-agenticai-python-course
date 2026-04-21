from random import randint

order_amount = randint(0, 600)
delivery_charges = 30
print(f"Your order amount is : ${order_amount}")


if order_amount < 300:
    total_amount = order_amount + delivery_charges
    print(f"Your order amount is less than $300, so you'll have to pay the extra delivery charge of ${delivery_charges}")
    print(f"Your total due amount is : ${total_amount}")

if order_amount > 300:
    total_amount = order_amount
    print(f"Congratulations!! FREE DELIVERY unlocked for this order!!")
    print(f"Your total due amount is : ${total_amount}")
















