stratring_word = input()
str_2 = input()

result = ""
previous_str = stratring_word

for index in range(len(stratring_word)):
    for i in range(index + 1):
        result += str_2[i]
    for i in range(index + 1, len(str_2)):
        result += stratring_word[i]
    if not result == previous_str:
        print(result)
    previous_str = result
    result = ""
