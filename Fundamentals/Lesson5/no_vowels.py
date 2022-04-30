vowels = ['a', 'o', 'e', 'u', 'i', "I"]
text =input()
no_vowels = [ch for ch in text if ch not in vowels]
print("".join (no_vowels))
# for ch in text:
#     if ch not in vowels:
#         no_vowels.append(ch)

# print("".join(no_vowels))

