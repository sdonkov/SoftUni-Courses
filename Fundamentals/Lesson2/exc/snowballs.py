snowballs_made = int(input())
highest_value = 0
highest_weight = 0
highest_time = 0
highest_quality = 0
for balls in range (1, snowballs_made + 1):
    snowball_weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (snowball_weight / time_needed) **quality
    if value > highest_value:
        highest_value = value
        highest_weight = snowball_weight
        highest_time = time_needed
        highest_quality = quality
print (f"{highest_weight} : {highest_time} = {highest_value:.0f} ({highest_quality})")
# print(highest_value)
# print(highest_weight)
# print(highest_time)
# print(highest_quality)