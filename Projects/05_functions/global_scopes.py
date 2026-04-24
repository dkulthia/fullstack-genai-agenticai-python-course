order = "coffee"

def reception():
    def counter():
        global order
        print(f"Global order = {order}")       
        order = "Tea"
        print(f"order at counter = {order}")       
    counter()
    print(f"last order = {order}")       

reception()