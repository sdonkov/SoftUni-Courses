start = input().split("#")
water = int(input())
effort = 0
put_out_fire= []
total_fire = 0
for _ in start:
    new_list = _.split(" = ")
    type,value = _.split(" = ")
    value = int(value)
    # type = str(new_list[0])
    # value = int(new_list[1])
    if water >=value:
        if type == "High" and 81<=value<=125:
            water -=value
            effort += value *0.25
            put_out_fire.append(value)
            total_fire += value
        elif type == "Medium" and 51<=value<=80:
            water -=value
            effort += value * 0.25
            put_out_fire.append(value)
            total_fire += value
        elif type == "Low" and 1<=value <=50:
            water -=value
            effort += value * 0.25
            put_out_fire.append(value)
            total_fire += value
print("Cells:")
for every in put_out_fire:
    print(f" - {every}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_fire)}")
