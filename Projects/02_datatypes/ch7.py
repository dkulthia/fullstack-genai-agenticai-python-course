Customer_name = "Darsh"
order = "Vadapaws"
order_quantity = 2


order_receipt = f"We have an order from {Customer_name}. " \
f"{Customer_name} has ordered {order_quantity} quantities of {order}."

receiptline_1 = f"We have an order from {Customer_name}. "
receiptline_2 = f"{Customer_name} has ordered {order_quantity} quantities of {order}."


receiptlenght_1 = len(receiptline_1)
receiptlenght_2 = len(receiptline_2)

print(f"{order_receipt[:receiptlenght_1]}")
print(f"{order_receipt[receiptlenght_1:]}")








