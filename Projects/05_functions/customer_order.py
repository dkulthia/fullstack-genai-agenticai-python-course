customer_list = ["Srikant", "Darsh", "Neha"]

order_list = ["Tea", "coffee", "cookies"]

zip_list = zip(customer_list, order_list)

def print_order(customer_name, customer_order):
    print(f"{customer_name} has ordered {customer_order}")



for customer_name, customer_order in zip_list:
    print_order(customer_name, customer_order)




    