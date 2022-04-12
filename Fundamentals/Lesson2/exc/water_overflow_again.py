number = int (input())
capacity = 255
liters_in_tank = 0
for n in range (number):
    water_poured = int(input())
    if liters_in_tank + water_poured > capacity:
        print ("Insufficient capacity!")
    else:
        liters_in_tank += water_poured
print(liters_in_tank)