def reception():
    order = "Coffee"
    def counter():
        nonlocal order
        print(f"order at reception = {order}")       
        order = "Tea"
        print(f"order at counter = {order}")       
    counter()
    print(f"order = {order}")       

reception()



# print(f"order = {order}")



# def update_order():
#     chai_type = "Elaichi"
#     def kitchen():
#         nonlocal chai_type
#         print(f"{chai_type}")
#         chai_type = "kesar"
#         print(f"{chai_type}")
#     kitchen()



# update_order()










