num = int(input())
stack = []

for x in range(num):
    command = input()
    if command.startswith("1"):
        new_cmd = command.split(' ')
        stack.append(int(new_cmd[1]))
    elif command.startswith("2"):
        if stack:
            stack.pop()
    elif command.startswith("3"):
        if stack:
            print(max(stack))
    elif command.startswith("4"):
        if stack:
            print(min(stack))

result = []
for x in range (len(stack)):
    result.append(str(stack.pop()))
print(", ".join(result))
