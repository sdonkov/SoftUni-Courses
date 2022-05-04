names = input().split(", ")

sorted_names = sorted(names)
sorted_names = sorted(sorted_names, key= lambda name: - len(name))

print(sorted_names)

# names = input().split(", ")
#
# sorted_list = sorted(names, key=lambda x: (-len(x),x))
#
# print(sorted_list)