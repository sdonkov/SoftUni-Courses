list_number = input().split()
remove =int(input())
list_as_int = []
final = []
for _ in range(len(list_number)):
    list_as_int.append(int(list_number[_]))
for sth in range (remove):
    smallest = min(list_as_int)
    list_as_int.remove(smallest)
for n in range (len(list_as_int)):
    final.append(str(list_as_int[n]))
print(", ".join(final))
# for i in list_as_int:
#     if i > smallest:
#         smallest=i
#         list_as_int.remove(i)
# print(list_as_int)