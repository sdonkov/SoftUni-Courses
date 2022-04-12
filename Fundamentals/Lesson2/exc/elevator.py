import math
people = int(input())
capacity = int(input())

# courses = int(people / capacity)
# people_left = people - (courses * capacity)
courses = math.ceil (people / capacity)
print(courses)
# if people_left !=0:
#     courses+=1
#
# print(courses)