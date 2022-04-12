import math
party_size = int(input())
days = int(input())
coins = 0
for day in range (1,days +1):
    if day % 10 ==0:
        party_size -=2
    if day % 15 == 0 :
        party_size += 5
    coins += (50-2*party_size)
    if day % 3 == 0:
        coins -=party_size * 3
    if day % 5 ==0:
        coins += 20 * party_size
    if day % 3 ==0 and day % 5 ==0:
        coins -= 2 * party_size

print (f'{party_size} companions received {math.floor(coins/party_size)} coins each.')