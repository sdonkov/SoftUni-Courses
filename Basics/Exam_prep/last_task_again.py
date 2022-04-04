sweet = input()
purchased_sweets = int(input())
date_of_december = int(input())
cake_price = 0
souffle_price = 0
baklava_price = 0
sum = 0
discount_sum = 0
if sweet == "Cake":
    if date_of_december <=15:
        cake_price = 24
        sum = cake_price * purchased_sweets
    else:
        cake_price = 28.70
        sum = cake_price * purchased_sweets
elif sweet == "Souffle":
    if date_of_december <=15:
        souffle_price= 6.66
        sum = souffle_price * purchased_sweets
    else:
        souffle_price = 9.8
        sum = souffle_price * purchased_sweets
elif sweet == "Baklava":
    if date_of_december <=15:
        baklava_price = 12.60
        sum = baklava_price * purchased_sweets
    else:
        baklava_price = 16.98
        sum = baklava_price * purchased_sweets
if date_of_december <=22:
    if sum >= 100 and sum <= 200:
        discount_sum = sum - (sum*0.15)
    else:
        discount_sum = sum - (sum*0.25)
if date_of_december <= 15:
    bonus_discount = discount_sum - (discount_sum*0.1)
    print (f'{bonus_discount:.2f}')
elif date_of_december > 15 and date_of_december <= 22:
    print (f'{discount_sum:.2f}')
else:
    print(f'{sum:.2f}')
