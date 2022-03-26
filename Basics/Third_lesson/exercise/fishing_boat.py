budget= int(input())
season = input()
number_fishers= int(input())
rent=0

if season == "Spring":
    rent = 3000
elif season =="Summer":
    rent = 4200
elif season == "Autumn":
    rent= 4200
elif season == "Winter":
    rent = 2600
if number_fishers <=6:
    rent=rent - rent *0.1
elif number_fishers >6 and number_fishers <=11:
    rent = rent - rent * 0.15
elif number_fishers >=12:
    rent= rent - rent * 0.25
if number_fishers % 2 == 0 and season != "Autumn":
    rent= rent - rent * 0.05
if budget >= rent:
    print (f"Yes! You have{budget-rent: .2f} leva left.")
elif rent > budget:
    print (f"Not enough money! You need{rent - budget: .2f} leva.")

