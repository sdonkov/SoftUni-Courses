import sys
input_number = int(input())
sum=0
biggest_num = -sys.maxsize
for pp in range (input_number):
    current_input= int(input())
    sum += current_input
    if current_input > biggest_num:
        biggest_num=current_input
other_numb_sum = sum - biggest_num
if other_numb_sum == biggest_num:
    print ("Yes")
    print (f"Sum = {biggest_num}")
else:
    print ("No")
    print(f"Diff = {abs(biggest_num - other_numb_sum)}")
