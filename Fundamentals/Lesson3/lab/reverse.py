first = input()
result = ''
index = len(first) - 1

while index >= 0:
    result += first[index]
    index -= 1
print(result)

