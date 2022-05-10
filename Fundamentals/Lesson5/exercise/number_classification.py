number = input().split(", ")
nums = list(map(int,number))
positive = [str(x) for x in nums if x >=0]
negative = [str(x) for x in nums if x<0]
even = [str(x) for x in nums if x % 2==0]
odd = [str(x) for x in nums if x % 2 !=0]


print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join (negative)}")
print(f"Even: {', '.join (even)}")
print(f"Odd: {', '.join (odd)}")