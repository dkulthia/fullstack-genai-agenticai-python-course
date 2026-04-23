def serve_order():
    order = "chai"
    print(f"order = {order}")


serve_order()

order = "coffee"
print(f"order = {order}")



def reception():
    def counter_one():
        order = "coffee"
        print(f"order at counter 1 = {order}")
    def counter_two():
        order = "Tea"
        print(f"order at counter 2 = {order}")
    counter_one()
    counter_two()


reception()










