import math
group_size = int(input())
days = int(input())
companions = 0
coins_spend = 0
coins = 0
companions = group_size
for n in range (1, days+1):
    # my_coins += 50
    # coins_spend += companions * 2
    if n % 10 == 0:
        companions = companions - 2
    if n % 15 == 0:
        companions = companions + 5

    coins += (50 - 2 * companions)

    if n % 3 == 0:
        coins -= companions * 3
    if n %5 == 0 :
        coins +=20 * companions
    if n % 3 == 0 and n % 5 == 0:
        coins -= companions * 2

    # coins_left = my_coins - coins_spend
    # total = int(coins / companions)
    # total_coins = my_coins + coins_spend
# coinz = (my_coins - coins_spend)/ companions
# print(coinz)
    # print(coins_spend)
print (f"{companions} companions received {math.floor(coins/companions)} coins each.")
