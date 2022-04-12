number = int(input())
capacity = 255
capacity_left = 0
liters_in_tank =0
for n in range (number):
    pour_liters = int(input())
    if liters_in_tank + pour_liters > capacity:
        print('Insufficient capacity!')
    else:
        liters_in_tank += pour_liters
print(liters_in_tank)