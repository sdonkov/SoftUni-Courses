start_nums = input().split(' ')
# stack = []
# while start_nums:
#     stack.append(start_nums.pop())
# print(" ".join(stack))
#--------------------------------------------

while start_nums:
    last_num = start_nums.pop()
    print(last_num, end = " ")
