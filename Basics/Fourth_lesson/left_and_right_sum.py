number_inp=int(input())
right_sum=0
left_sum=0
for number in range (2*number_inp):
    inp_number=int(input())
    if number < number_inp:
        left_sum+=inp_number
    else:
        right_sum+=inp_number
if left_sum == right_sum:
    print (f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(right_sum -left_sum) }")