clients= int(input())
total= 0

for current_clients in range (clients):
    current_sum = 0
    number_of_products = 0
    command = input()
    while command != "Finish":
        number_of_products+=1
        if command == 'basket':
            current_sum += 1.50
        elif command == 'wreath':
            current_sum += 3.80
        elif command == 'chocolate bunny':
            current_sum += 7
        command = input()
    if number_of_products %2 ==0:
        current_sum= current_sum - (current_sum * 0.2)
    print (f"You purchased {number_of_products} items for {current_sum:.2f} leva.")
    total += current_sum
avv = total / clients
print (f"Average bill per client is: {avv:.2f} leva.")

