number = int(input())
capacity = 255
liters_in_tank = 0
for n in range (number):
    pour_liters= int(input())
    if pour_liters + liters_in_tank > capacity:
        print('Insufficient capacity!')
    else:
        liters_in_tank +=pour_liters

print(pour_liters)