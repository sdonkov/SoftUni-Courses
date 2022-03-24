budget = float (input())
number_videocards = int (input())
number_procesors = int (input())
number_ram = int (input())

videocard_price = 250
videocard_total = videocard_price * number_videocards
procesor_price = videocard_total * 0.35
procesor_total = procesor_price * number_procesors
ram_price = videocard_total * 0.1
ram_total = ram_price * number_ram
sum_total = videocard_total + procesor_total + ram_total
if number_videocards > number_procesors:
    sum_total = sum_total - (sum_total*0.15)
money_left = budget - sum_total
money_needed = abs (budget - sum_total)
if budget >= sum_total:
    print (f"You have{money_left: .2f} leva left!")
elif budget <= sum_total:
    print (f"Not enough money! You need{money_needed: .2f} leva more!")


