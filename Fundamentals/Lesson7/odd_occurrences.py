data = input().lower().split()

dictionary = {}
for x in data:
    if x not in dictionary:
        dictionary[x] = 0
    dictionary[x] += 1

for key,value in dictionary.items():
    if value % 2 !=0:
        print(key, end=" ")