def sum_of_even (a):
    even_sum = 0
    odd_sum = 0
    for i in a:
        if i % 2 ==0:
            even_sum += i
        else:
            odd_sum+= i
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')



num =map(int, list(input()))
sum_of_even(num)