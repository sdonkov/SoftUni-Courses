number_of_groups=int(input())
p1=0
p2=0
p3=0
p4=0
p5=0
total=0
for i in range (number_of_groups):
    people_in_one_group=int(input())
    total+=people_in_one_group
    if people_in_one_group <=5:
       p1+=people_in_one_group
    elif people_in_one_group <=12:
        p2+=people_in_one_group
    elif people_in_one_group <=25:
        p3+=people_in_one_group
    elif people_in_one_group <=40:
        p4+=people_in_one_group
    else:
        p5+=people_in_one_group

p1 = p1/total * 100
p2 = p2/total * 100
p3 = p3/total * 100
p4 = p4/total * 100
p5 = p5/total * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
