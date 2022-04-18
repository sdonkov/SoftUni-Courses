list = input().split()
final_list = []

for n in list:
    float_list = float(n)
    final_list.append(round(float_list))


print(final_list)
