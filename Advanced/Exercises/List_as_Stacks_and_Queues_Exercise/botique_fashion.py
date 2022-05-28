initial_clothes = list(map(int, input().split(' ')))
capacity = int(input())
used_racks = 1
total = 0

while initial_clothes:
    current_clothes = initial_clothes[-1]
    total += current_clothes
    if total > capacity:
        used_racks += 1
        total = 0
    else:
        initial_clothes.pop()


print(used_racks)

