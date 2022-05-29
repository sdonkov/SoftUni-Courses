data = input()

stack = []
pairs = {
    '(':')',
    '{':'}',
    '[':']'
}
balanced = True
for x in data:
    if x in '({[':
        stack.append(x)
    elif not stack:
        balanced = False
    else:
        last_opening = stack.pop()
        if x != pairs[last_opening]:
            balanced = False

    if not balanced:
        break


if not balanced or stack:
    print("NO")
else:
    print("YES")