numbers = input().split(", ")
numbers = list(map(int,numbers))
even_list = []

# even_indexes = map(lambda x:)

for i in range (len(numbers)):
    if numbers[i] % 2 == 0:
        even_list.append(i)

print(even_list)
