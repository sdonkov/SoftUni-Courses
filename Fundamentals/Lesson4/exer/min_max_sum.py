def min_max_sum (nums):
    print(f"The minimum number is {min(nums)}")
    print(f"The maximum number is {max(nums)}")
    print(f"The sum number is: {sum(nums)}")


a = list(map(int, input().split(" ")))
min_max_sum(a)