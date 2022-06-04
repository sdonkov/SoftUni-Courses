numbers = int(input())

words = {}

for x in range(numbers):
    word = input()
    synonym = input()
    if word not in words:
        words[word] = []
    words[word].append(synonym)

# for x,y in words.items():
#     print(f"{x} - {', '.join(y)}")

for word in words:
    print(f"{word} - {', '. join(words[word])}")