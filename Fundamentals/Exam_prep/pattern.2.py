number = int(input())

for xm in range (number):
    for mx in range (xm+1):
        print("*", end = "")
    print()

for i in range (number):
    for j in range (number-1,i,-1):
        print("*", end="")
    print()