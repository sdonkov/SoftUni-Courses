from collections import deque

cups = deque(map(int,input().split(" ")))
bottles = deque(map(int,input().split(" ")))
wasted_water = 0

while cups:
    if not bottles:
        print(f"Cups: {' '.join(str(n) for n in cups)}")
        break

    bottle = bottles.pop()
    if bottle >= cups[0]:
        wasted_water = wasted_water + bottle- cups[0]
        cups.popleft()
    else:
        cups[0] -= bottle


else:
    bottles = [str(bottles[x]) for x in range(len(bottles) -1,-1,-1)]
    print(f"Bottles: {' '.join(bottles)}")

print(f"Wasted litters of water: {wasted_water}")

