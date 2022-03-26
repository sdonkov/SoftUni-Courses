flower_type = input()
number_flowers = int(input())
budget = int(input())
roses_price = 5.00
dahlias_price= 3.80
tulips_price = 2.80
narcissus_price = 3.00
gladious_price = 2.50


total = 0
if flower_type == "Roses":
    total = roses_price* number_flowers
    if number_flowers > 80:
        total = total - total * 0.1
elif flower_type == "Dahlias":
    total = dahlias_price * number_flowers
    if number_flowers > 90:
        total = total - total * 0.15

elif  flower_type == "Tulips":
    total = tulips_price * number_flowers
    if number_flowers >80:
        total = total - total * 0.15

elif flower_type == "Narcissus":
    total = narcissus_price * number_flowers
    if number_flowers < 120:
        total= total + total * 0.15

elif flower_type == "Gladiolus":
    total = gladious_price*number_flowers
    if number_flowers < 80:
        total= total + total * 0.2
if budget >= total:
    print (f"Hey, you have a great garden with {number_flowers} {flower_type} and{budget - total: .2f} leva left.")
else:
    print (f"Not enough money, you need{total- budget: .2f} leva more.")

