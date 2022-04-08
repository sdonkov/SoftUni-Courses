budget = float(input())
flour_price = float (input())

eggs_price = flour_price * 0.75
milk_price = flour_price + (flour_price* 0.25)
bread_price = flour_price + eggs_price + milk_price / 4
budget_left = 0
counter = 0
colored_eggs = 0

while budget >= bread_price:
    counter +=1
    colored_eggs+=3
    budget -= bread_price
    if counter % 3 ==0:
        colored_eggs = colored_eggs - (counter - 2)
print(f"You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
