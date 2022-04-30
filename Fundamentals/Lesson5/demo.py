num_list = []
for n in range(1,7):
    num_list.append(n)


x = [True if n % 2 ==0 else False for n in num_list]
print(x)