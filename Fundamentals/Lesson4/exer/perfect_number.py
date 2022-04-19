def perfect_num(a):
    sum = 0
    for x in range (1,a):
        if a % x == 0:
            sum+=x
    return sum == a

num= int(input())
if perfect_num(num) == True:
        print("We have a perfect number!")
else:
        print("It's not so perfect.")

# num= int(input())
perfect_num(num)



