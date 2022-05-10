def next_version(num):
    num = int(''.join(num)) +1
    result = [str(num) for num in str(num)]
    print(".".join(result))

data = input().split(".")
next_version(data)