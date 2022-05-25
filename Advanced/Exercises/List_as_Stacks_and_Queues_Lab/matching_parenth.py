task = input()

stack = []

for index in range(len(task)):
    if task[index] == "(":
        stack.append(index)
    elif task[index] == ")":
        start_index = stack.pop()
        print(task[start_index:index+1])

