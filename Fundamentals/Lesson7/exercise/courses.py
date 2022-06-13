command = input()
course_dict = {}

while command != "end":
    command = command.split(" : ")
    course_name = command[0]
    student_name = command[1]
    if course_name not in course_dict:
        course_dict[course_name] = []
    course_dict[course_name].append(student_name)

    command = input()

for key,value in course_dict.items():
    print(f"{key}: {len(course_dict[key])}")
    for x in range(len(course_dict[key])):
        print(f"-- {course_dict[key][x]}")