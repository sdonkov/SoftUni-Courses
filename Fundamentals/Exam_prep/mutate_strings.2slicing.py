first_string = input()
second_string = input()
last_string = first_string

for i in range (len(first_string)):
    left_part = second_string[:i+1]
    right_part = first_string [i+1:]
    current_string = left_part +right_part
    if last_string == current_string:
        continue
    print (current_string)
    last_string=current_string
