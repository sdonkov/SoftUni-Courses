number= int(input())
first_number = number % 10
second_number = number //10 %10
third_number = number // 100
for n in range (1, first_number +1):
    for n2 in range (1,second_number+1):
        for n3 in range (1, third_number+1):
            result = n * n2 * n3
            print(f"{n} * {n2} * {n3} = {result};")
