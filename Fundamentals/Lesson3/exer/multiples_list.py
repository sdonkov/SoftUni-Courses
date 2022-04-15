# factor = int(input())
# count = int(input())
# list = []
#
# for number in range(1,count+1):
#     list_numbers = number * factor
#     list.append(list_numbers)
# print(list)

string = input().split()
opposite_numbers = []
for index in range (len(string)):
    opposite_number = -int(string[index])
    opposite_numbers.append(opposite_number)
print(opposite_numbers)