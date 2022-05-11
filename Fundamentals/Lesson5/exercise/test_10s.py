numbers = list(map(int, input().split(", ")))

border = 10
lst = []

while len(numbers) > 0:
    lst = ([num for num in numbers if num <= border])
    print(f"Group of {border}'s: {lst}")
    numbers = [num for num in numbers if num > border]
    border += 10