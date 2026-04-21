serving_size = input("What serving size do you want to order?: ( Small / Medium / Large ): ").lower()


if serving_size == "small" :
    print(f"You have chose to order a {serving_size} cup of tea.")
    print(f"your order for a {serving_size} cup of tea will cost $10. Do you want to confirm this order!?")

elif serving_size == "medium" :
    print(f"You have chose to order a {serving_size} cup of tea.")
    print(f"your order for a {serving_size} cup of tea will cost $15. Do you want to confirm this order!?")

elif serving_size == "large" :
    print(f"You have chose to order a {serving_size} cup of tea.")
    print(f"your order for a {serving_size} cup of tea will cost $20. Do you want to confirm this order!?")

else:
    print(f"Invalid Input!!!!!!!")










