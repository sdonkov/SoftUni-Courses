import re
emoji_dict = {}
text = input()
patter_treasure = r"\d"
treasure = re.findall(patter_treasure, text)
total_treasure = 1
treasure = list(map(int,treasure))
for number in treasure:
    total_treasure *= number

emoji_pattern = r"(::|\*{2})([A-Z][a-z]{2,})\1"
emojis = re.finditer(emoji_pattern, text)
emoji_list = []
for emoji in emojis:
    emoji_list.append(emoji.group())
counter = len(emoji_list)
emojis_str = " ".join(emoji_list)
value = 0
values_list = []
for x in emojis_str:
    if x == " ":
        values_list.append(value)
        value = 0
    elif x == ":" or x == "*":
        continue
    else:
        value += ord(x)
values_list.append(value)
final_emojis = {}
index = 0
for x in emoji_list:
    if int(values_list[index]) > total_treasure:
        final_emojis[x] = [values_list[index]]

    index +=1
# print(final_emojis)
# print(emoji_dict)
# print(values_list)
# print(cool_emojis)
# print(emoji_list)
print(f"Cool threshold: {total_treasure}")
print(f"{counter} emojis found in the text. The cool ones are:")
for k,v in final_emojis.items():
    print(f'{k}')

