quantity = int(input())
days= int(input())

spirit = 0
total_cost = 0
for day in range (1,days + 1):
    if day % 11 ==0:
        quantity +=2

    if day % 2 ==0:
        spirit += 5
        total_cost +=quantity *2

    if day % 3 ==0:
        spirit += 13
        total_cost += quantity * 3 + quantity * 5

    if day % 5==0:
        spirit += 17
        total_cost += quantity * 15
        if day % 3 ==0:
            spirit += 30
    if day % 10 == 0:
        spirit -=20
        total_cost += 23

        if day ==days:
            spirit -=30

print (f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")