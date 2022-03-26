budget= float(input())
season = input()
destination=""
type_of_holiday = ""
total_money = 0
if season == "summer" and budget <=1000:
    type_of_holiday = "Camp"
elif season =='winter':
    type_of_holiday = "Hotel"
else:
    type_of_holiday= "Hotel"
if destination == "Europe":
    pass
if budget <=100:
    if season == "summer":
        total_money = budget *0.3

    elif season == "winter":
        total_money = budget * 0.7
    destination = "Bulgaria"
elif budget <= 1000:
    if season == "summer":
        total_money = budget *0.4
    elif season == "winter":
        total_money = budget * 0.8
    destination = "Balkans"
elif budget >1000:
    total_money = budget * 0.9
    destination = "Europe"
print (f"Somewhere in {destination}")
print (f"{type_of_holiday} - {total_money:.2f}")
