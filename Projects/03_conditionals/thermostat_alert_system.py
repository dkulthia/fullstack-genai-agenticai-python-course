from random import choice
from random import randint


device_status = choice(["Active", "Inactive"])


if device_status == "Active":
    print(f"Device Status : {device_status}")
    device_temperature = randint(30, 40)
    if device_temperature < 35:
        print(f"Temperature is normal!!")
        print(f"Device temperature :  {device_temperature}")
    
    elif device_temperature > 35:
        print(f"High temperature alert!!")
        print(f"Device temperature :  {device_temperature}")

elif device_status == "Inactive":
    print(f"Device Status: {device_status}")









