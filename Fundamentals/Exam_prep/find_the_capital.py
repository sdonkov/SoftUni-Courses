string = input()
index =[]
for i in range(len(string)):
    if string[i].isupper():
        index.append(i)
    else:
        continue
print(index)