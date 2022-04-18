def calculation ():
    operation = input()
    num_a=int(input())
    num_b=int(input())

    if operation == "multiply":
        return (num_a * num_b)
    elif operation == "divide":
        return int(num_a / num_b)
    elif operation == "add":
        return (num_a + num_b)
    else:
        return (num_a - num_b)


print (calculation())