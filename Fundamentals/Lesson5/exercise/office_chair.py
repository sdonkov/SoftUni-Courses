rooms = int(input())
total = 0
opt = True
for x in range(1,rooms+1):
    explode = input().split(" ")
    chairs = len(explode[0])
    guest = int(explode[1])

    diff = abs (chairs-guest)
    if chairs < guest:
        opt= False
        print(f"{diff} more chairs needed in room {x}")
    elif chairs > guest:
        total = total+diff

if opt:
    print(f"Game On, {total} free chairs left")

