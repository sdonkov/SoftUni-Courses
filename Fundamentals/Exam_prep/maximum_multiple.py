divisor = int(input())
boundary = int(input())

n=0
# for number in range (1,boundary+1):
#     if number % divisor == 0:
#         n = number
# print(n)

for number in range (boundary+1,0,-1):
    if number % divisor ==0:
        n=number
        break
print(n)

# divisor = int(input())
# bound = int(input())
#
# for num in range (bound,divisor-1, -1):
#     if num % divisor == 0:
#         print (num)
#         break