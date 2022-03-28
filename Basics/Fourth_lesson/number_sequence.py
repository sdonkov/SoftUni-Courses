import sys
smallest = sys.maxsize
biggest = -sys.maxsize
input_number = int(input())
for number in range (1,input_number+1):
    input_number_again = int(input())
    if input_number_again < smallest:
        smallest=input_number_again
    if input_number_again > biggest:
        biggest = input_number_again
print (f"Max number: {biggest}")
print(f"Min number: {smallest}")