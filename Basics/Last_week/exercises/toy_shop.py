price_of_travel = float (input())
number_of_puzzles = int (input())
number_of_talking_dolls = int (input())
number_of_teddy_bears = int (input())
number_of_minions = int (input())
number_of_trucks = int (input())
earnings = 0
total_number_of_toys = number_of_trucks + number_of_minions + number_of_puzzles \
                       + number_of_teddy_bears + number_of_talking_dolls
total_price = (number_of_puzzles * 2.60) + (number_of_talking_dolls * 3.00) + (number_of_teddy_bears * 4.10) + \
              (number_of_minions * 8.20) + (number_of_trucks * 2.00)
if total_number_of_toys >=50:
    total_price = total_price - (25 * total_price / 100)
    earnings = total_price - (10* total_price/100)

else:
    earnings = total_price - (10*total_price/100)
money_left = earnings - price_of_travel
money_needed = price_of_travel - earnings
puzzle = 2.60
talking_doll = 3.00
teddy_bear = 4.10
minion = 8.20
truck = 2.00
if price_of_travel <= earnings:
    print (f"Yes!{money_left: .2f} lv left.")
else:
    print (f"Not enough money! {abs (money_needed):.2f} lv needed.")
