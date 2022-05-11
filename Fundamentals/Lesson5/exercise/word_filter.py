text = input().split()
result = [x for x in text if len(x) % 2 ==0]
print('\n'.join(result))