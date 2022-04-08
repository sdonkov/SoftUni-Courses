budget = float(input())
price_of_1kg_flour = float(input())
bread_counter = 0
price_for_1pack_eggs = 0.75 * price_of_1kg_flour
price_for_1l_milk = price_of_1kg_flour + (price_of_1kg_flour *0.25)
budget_left = 0
colored_eggs = 0
one_bread_price = price_of_1kg_flour + price_for_1pack_eggs + price_for_1l_milk / 4
# milk needed for 1 bread is 250ml NOT 1L
# for every bread receive 3 colored eggs
# for every 3rd bread lose some colored eggs - ({current_bread_count} – 2
#  print "You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."
while budget >= one_bread_price:
    # print(f'{one_bread_price:.2f}')
    bread_counter += 1
    budget_left = budget - one_bread_price
    budget -= one_bread_price
    colored_eggs +=3
    if bread_counter % 3 == 0:
        colored_eggs -= (bread_counter - 2)
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
