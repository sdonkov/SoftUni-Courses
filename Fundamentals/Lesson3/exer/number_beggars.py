cents = input().split(", ")
beggars = int(input())
counter_of_index = 0
final_list = []
sum_per_beggar = 0
cents_as_int = []
for index in range(len(cents)):
    cents_as_int.append(int(cents[index]))
while counter_of_index < beggars:
    for element in range (counter_of_index, len(cents_as_int), beggars):
        sum_per_beggar += cents_as_int[element]
    final_list.append(sum_per_beggar)
    sum_per_beggar = 0
    counter_of_index +=1
print(final_list)

