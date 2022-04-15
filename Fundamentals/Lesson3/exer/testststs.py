start = input().split("#")
water = int(input())
for _ in start:
    new_list = _.split("=")
    type = new_list[0]
    value = int(new_list[1])
    print(type)
    if type == "High" and value>=81:
        water -=value
    elif type == "Medium" and 51<=value<=80:
        water -=value
    elif type == "Low" and 1<=value <=50:
        water -=value
print(water)