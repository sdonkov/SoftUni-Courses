lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total = 0
counter = 0
for loss in range (1,lost_fights+1):
    if loss % 2 ==0:
        total += helmet_price
    if loss % 3 ==0:
        total += sword_price
    if loss % 2 ==0 and loss % 3 == 0 :
        counter += 1
        total += shield_price
        if counter % 2 == 0:
            total += armor_price
print (f"Gladiator expenses: {total:.2f} aureus")
