number = int(input())
# for num in range (1, number+1):
#     number_as_string = str(num)
#     result = 0
#     for symbol in number_as_string:
#         result += int(symbol)
#     if result == 5 or result == 7 or result == 11:
#         print (f'{num} -> True')
#     else:
#         print (f'{num} -> False')
#

for num in range (1, number + 1 ):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = digits // 10
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print (f'{num} -> True')
    else:
        print (f'{num} -> False')
