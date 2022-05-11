first = input().split(", ")
second = input()

final = [x for x in first if x in second]

# for x in first:
#     if x in second:
#         final.append(x)

print(final)