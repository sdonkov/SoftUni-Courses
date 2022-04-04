painted_egss = int(input())
counter_for_red=0
orange_counter = 0
blue_counter = 0
green_counter = 0
max_eggs=0
color_max_eggs = ''
for eggs in range (painted_egss):
    color_of_egg = input()
    if color_of_egg == "red":
        counter_for_red +=1
        if counter_for_red > max_eggs:
            max_eggs=counter_for_red
            color_max_eggs = 'red'
    elif color_of_egg == 'orange':
        orange_counter +=1
        if orange_counter > max_eggs:
            max_eggs= orange_counter
            color_max_eggs = "orange"
    elif color_of_egg == 'blue':
        blue_counter +=1
        if blue_counter > max_eggs:
            max_eggs= blue_counter
            color_max_eggs = 'blue'
    elif color_of_egg == 'green':
        green_counter+=1
        if green_counter > max_eggs:
            max_eggs = green_counter
            color_max_eggs = "green"

print(f"Red eggs: {counter_for_red}")
print (f"Orange eggs: {orange_counter}")
print(f"Blue eggs: {blue_counter}")
print(f"Green eggs: {green_counter}")
print (f"Max eggs: {max_eggs} -> {color_max_eggs}")
