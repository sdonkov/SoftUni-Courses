data = input().split(" ")
bakery = dict()

for x in range(0,len(data), 2):
    food = data[x]
    quantities = int(data[x+1])
    bakery[food] = quantities

print(bakery)