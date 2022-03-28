count_nubmer = int(input())
odd_sum = 0
even_sum= 0
diff=0
for number in range (1, count_nubmer+1):
    current_number = int(input())
    if number % 2 ==0:
       even_sum = even_sum + current_number
    elif number % 2 !=0:
        odd_sum = odd_sum + current_number
if odd_sum == even_sum:
    print ("Yes")
    print (f"Sum = {odd_sum}")
elif odd_sum != even_sum:
    diff= odd_sum - even_sum
    diff= abs(diff)
    print ("No")
    print (f'Diff = {abs (odd_sum - even_sum)}')