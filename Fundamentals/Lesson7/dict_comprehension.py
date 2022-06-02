# people = {'Peter': 21, 'George': 45, 'John': 18}

# print({key:value for key,value in people.items() if value % 2 ==0})

# print ({y:x for x,y in people.items() if y%2 ==0})

nums = [1,2,3]
cubes = {num:num **3 for num in nums}
print(cubes)