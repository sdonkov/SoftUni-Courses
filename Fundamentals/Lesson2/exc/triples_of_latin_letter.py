number = int(input())

for n in range (number):
    for k in range (number):
        for j in range (number):
            print (f'{chr(97 + n)}{chr(97+ k )}{chr(97+j)}')