from collections import deque

total_quantity = int(input())
ordered_quantity = deque(map(int, input().split(' ')))
max_order = max(ordered_quantity)
index = 0

while ordered_quantity:
    if ordered_quantity[index] <= total_quantity:
        total_quantity -= ordered_quantity[index]
        ordered_quantity.popleft()
    else:
        break


print(max_order)
if not ordered_quantity:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, ordered_quantity))}")
