rent = int(input())

statues = rent - (rent * 0.3)
food = statues -  (statues * 0.15)
sound = food / 2

total = rent + statues + food + sound

print(f"{total:.2f}")