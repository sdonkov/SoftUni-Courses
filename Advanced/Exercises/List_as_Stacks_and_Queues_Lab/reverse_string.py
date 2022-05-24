# text = list(input())
#
# stack = []
#
# for x in range(len(text)):
#     stack.append(text.pop())
#
# print(''.join(stack))

#---------------------- solution 2----------------------------


text = list(input())

while text:
    print(text.pop(), end = "")