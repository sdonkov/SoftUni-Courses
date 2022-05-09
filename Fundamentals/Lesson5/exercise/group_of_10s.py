string_nums = list(map(int,input().split(", ")))
max_group_value = 0
boundary = 10
while True:
    if len(string_nums) == 0:
        break

    current_list = [x for x in string_nums if x <= boundary]
    for y in current_list:
        string_nums.remove(y)

    print(f"Group of {boundary}'s: {current_list}")
    boundary += 10







