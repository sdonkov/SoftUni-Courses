# number = int(input())

# for _ in range (1,number+1):
#     number_as_string = str(_)
#     result = 0
#     for symbol in number_as_string:
#         result +=int(symbol)
#     if result == 5 or result == 7 or result ==11:
#         print(f"{_} -> True")
#     else:
#         print(f"{_} -> False")

# for n in range (1,number+1):
#     working_number = n
#     sum = 0
#     while working_number >0:
#         sum += working_number % 10
#         working_number = int(working_number/10)
#
#     is_special = sum == 5 or sum == 7 or sum == 11
#     print(f'{n} -> {is_special}')

year = int(input())
next_year = 0
while True:
    year+=1
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        print(year)
        break
