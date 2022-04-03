number_of_floors = int(input())
number_of_rooms = int(input())
for floor in range (number_of_floors, 0 , -1):
    for rooms in range (number_of_rooms):
        if floor == number_of_floors:
            print (f'L{floor}{rooms}', end= " ")
        elif floor %2 !=0:
            print(f'A{floor}{rooms}', end=" ")
        else:
            print(f'O{floor}{rooms}', end=" ")
    print()

