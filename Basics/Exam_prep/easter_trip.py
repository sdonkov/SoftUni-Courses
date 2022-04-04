destionation = input()
dates = input()
nights_staying = int (input())
price_for_one_night = 0
if destionation == "France":
    if dates == "21-23":
        price_for_one_night= 30
    elif dates == "24-27":
        price_for_one_night = 35
    elif dates == "28-31":
        price_for_one_night = 40
elif destionation == "Italy":
    if dates == "21-23":
        price_for_one_night= 28
    elif dates == "24-27":
        price_for_one_night = 32
    elif dates == "28-31":
        price_for_one_night = 39
elif destionation == "Germany":
    if dates == "21-23":
        price_for_one_night= 32
    elif dates == "24-27":
        price_for_one_night = 37
    elif dates == "28-31":
        price_for_one_night = 43

total = nights_staying * price_for_one_night
print (f"Easter trip to {destionation} : {total:.2f} leva.")