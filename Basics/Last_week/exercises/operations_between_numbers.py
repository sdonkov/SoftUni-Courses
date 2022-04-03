n1= int(input())
n2= int (input())
operator = input ()
result=0
number_type = ''
if operator == "+" or operator== "-" or operator== "*":
    if operator == '+':
        result = n1 + n2
    elif operator=='-':
        result = n1 - n2
    elif operator == '*':
        result = n1*n2
elif operator == "/" or operator == "%":
    if n2== 0:
        print(f"Cannot divide {n1} by zero")
    elif operator == "/":
        result = n1/n2
        print(f"{n1} / {n2} ={result: .2f}")
    elif operator == '%':
        result= n1%n2
        print(f"{n1} % {n2} = {result}")
if result %2 != 0:
    number_type = "odd"
elif result %2 == 0:
    number_type= "even"
if operator == "+" or operator == "-" or operator == "*":
    print (f"{n1} {operator} {n2} = {result} - {number_type}")
