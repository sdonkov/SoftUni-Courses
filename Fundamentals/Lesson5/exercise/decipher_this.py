sicret = input().split()
final_string = []
for word in sicret:
    numbers = [num for num in word if num.isnumeric()]
    value_chr = int("".join(numbers))
    characters =[char for char in word if char.isalpha()]
    characters [0], characters[-1] = characters[-1],characters[0]
    characters = "".join(characters)
    word = chr(value_chr) + characters
    final_string.append(chr(value_chr) + characters)

print(" ".join(final_string))


# new_str = str[:1] + str[-1:] + str[2:-1] + str[1:1]
# print(new_str)
#
#
# str = input().split()
# new_str = str[:1] + str[-1] + str[2:-1] + str[1]
# print(new_str)
#
# # str = input("Enter a string : ")
# # new_str = str[-1:] + str[1:-1] + str[:1]
# # print(new_str)