words = input().split(" ")
search_palindrome = input()
palindrome_list = []
count =words.count(search_palindrome)

for word in words:
    rev_list = reversed(word)
    rev_words = "".join(rev_list)
    if rev_words == word:
        palindrome_list.append(rev_words)

print(palindrome_list)
print(f'Found palindrome {count} times')
