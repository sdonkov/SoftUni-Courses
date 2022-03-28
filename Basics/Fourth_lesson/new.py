count_number=int(input())
odd_sum=0
even_sum=0
for number in range (count_number):
    input_number=int(input())
    if number % 2==0:
        even_sum=even_sum+input_number
    else:
        odd_sum=odd_sum+input_number
if odd_sum == even_sum:
    print(f"Yes")
    print(f"Sum = {odd_sum}")
if odd_sum !=even_sum:
    print("No")
    print (f"Diff = {abs(odd_sum-even_sum)}")