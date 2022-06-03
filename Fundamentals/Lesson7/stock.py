inventory = input().split(" ")
looking_for = input().split(" ")
bakery = {}

for i in range (0,len(inventory), 2):
    food = inventory[i]
    quantity = int(inventory[i + 1])
    bakery[food] = quantity

for x in looking_for:
    if x in bakery.keys():
        print(f"We have {bakery[x]} of {x} left")
    else:
        print(f"Sorry we don't have {x}")