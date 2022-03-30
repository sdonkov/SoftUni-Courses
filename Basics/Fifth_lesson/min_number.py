import sys

text=input()
min_number=sys.maxsize
while text !="Stop":
    new_number=int(text)
    if new_number < min_number:
        min_number=new_number
    text=input()
print(min_number)

# -10
# 20
# -30
# Stop