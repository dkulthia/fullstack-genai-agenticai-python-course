customer_name = ["Srikant", "Darsh", "Neha"]
customer_bill = ["$100", "$200", "$300"]

zip_list = zip(customer_name, customer_bill)

for name, bill in zip_list:
    print(f"{name} paid {bill}")

