student_name = input()
bad_grade=0
grade=0
current_class=1
is_ejected = False
while current_class<=12:
    current_grade=float (input())
    if current_grade<4:
        bad_grade+=1
        if bad_grade == 2:
            is_ejected = True
            break
        continue
    current_class+=1
    grade+=current_grade
if is_ejected==True:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    avg_grade=grade/12
    print(f"{student_name} graduated. Average grade: {avg_grade:.2f}")



