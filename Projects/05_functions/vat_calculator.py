prices = [100, 877, 541, 864]

vat_rate = 5



def add_vat(price, vat_rate):
    vat = price * vat_rate / 100
    final_amount = price + vat
    print(f"base price = ${price}, vat = ${vat}, final price = ${final_amount}")





for price in prices:
    add_vat(price, vat_rate)




