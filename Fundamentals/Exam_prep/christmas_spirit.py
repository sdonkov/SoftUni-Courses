quantity = int(input())
days_left = int (input())
days_count = 0
spirit = 0
total_cost = 0
while days_left >0:
    days_left -= 1
    days_count +=1
    if days_count % 11 ==0:
        quantity +=2
    if days_count % 2 == 0:
        total_cost += quantity * 2
        spirit += 5
    if days_count % 3 == 0:
        total_cost += quantity * 5 + quantity * 3
        spirit += 13
    if days_count % 5 ==0:
        total_cost += quantity *15
        spirit += 17
        if days_count % 3 == 0 and days_count % 5 == 0 :
            spirit +=30
        if days_count % 10 ==0:
            spirit -=20
            total_cost +=23
        if days_count == days_left:
            spirit-=30

print (f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
