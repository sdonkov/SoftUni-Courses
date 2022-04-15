cents = input().split(", ")
beggars_count = int(input())
sum_per_beggar =[]
sum = 0
counter_of_index = 0
cents_as_int = []
for index in range(len(cents)):
    cents_as_int.append(int(cents[index]))
while counter_of_index < beggars_count:
    for beg in range (counter_of_index, len(cents_as_int),beggars_count):
            sum += cents_as_int[beg]
    sum_per_beggar.append(sum)
    sum = 0
    counter_of_index+=1
print(sum_per_beggar)
