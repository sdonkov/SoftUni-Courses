n = int(input())
word = input()
all_words = []
specific_words = []

for _ in range (n):
    string = input()
    all_words.append(string)
    if word in string:
        specific_words.append(string)
print (all_words)
print (specific_words)