def palindrome(a):
    for n in num:
        if n == n[::-1]:
            print("True")
        else:
            print("False ")



num =input().split(", ")
palindrome(num)
