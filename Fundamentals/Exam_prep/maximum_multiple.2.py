divisor = int(input())
bound = int(input())

# for num in range (bound,divisor-1, -1):
#     if num % divisor == 0:
#         print (num)
#         break

result = int(bound / divisor ) * divisor
print(result)