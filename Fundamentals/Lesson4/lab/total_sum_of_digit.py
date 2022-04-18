# number = int(input())
# number_str = str(number)
# total = 0
#
# for digit in number_str:
#     total += int(digit)
#
# print(total)


day = int(input())
hours = int(input())
minutes = int(input())
seconds = int(input())

total = 0

total = (day * 24 * 3600) + (hours * 3600) + (minutes * 60) + seconds
print(total)