factor = int(input())
count = int(input())
list = []

for num in range (1,count+1):
    list.append(int(num*factor))
print(list)