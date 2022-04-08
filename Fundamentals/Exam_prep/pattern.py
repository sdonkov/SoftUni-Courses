number = int(input())

for row in range (number):
    for arrow in range (row+1):
        print("*", end = "")
    print()
#
# for row in range (number-1, 0,-1):
#     for arrow in range (row):
#         print("*", end="")
#     print()
#

for i in range (number - 1):
    for j in range (number - 1, i , -1):
        print("*", end= "")
    print()