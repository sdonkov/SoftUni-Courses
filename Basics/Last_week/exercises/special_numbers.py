number = int(input())

for numb in range (1111,10000):
    is_special = True
    for digit in str (numb):
        if int(digit) == 0 or number % int(digit) !=0:
            is_special = False
            break
    if is_special:
        print (numb , end = " ")