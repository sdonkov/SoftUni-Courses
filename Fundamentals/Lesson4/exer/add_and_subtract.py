def sum (a,b,c):
    return a+b


def subtract (a,b,c):
    return sum(a,b,c) - c



num1,num2,num3 = int(input()), int(input()), int(input())
print (subtract(num1,num2,num3))


