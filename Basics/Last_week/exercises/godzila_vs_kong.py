film_budget = float (input())
statists = int (input())
price_of_clothes = float (input())
decor = 0.1 * film_budget
total_cloth = statists * price_of_clothes
total_sum = total_cloth + decor
money_left = film_budget - total_sum
money_needed = abs (film_budget - total_sum)
if statists >150:
    total_cloth = total_cloth - (total_cloth *10/100)

total_sum = total_cloth + decor
money_needed = abs (film_budget - total_sum)
money_left = film_budget - total_sum
if total_sum > film_budget:
    print ("Not enough money!")
    print (f"Wingard needs{money_needed: .2f} leva more.")
elif total_sum <= film_budget:
    print ("Action!")
    print (f"Wingard starts filming with{money_left: .2f} leva left.")
