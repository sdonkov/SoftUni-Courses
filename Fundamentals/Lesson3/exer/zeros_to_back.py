# letters = ['a', 'b', 'c']
# for letter in enumerate(letters):
#     print(letter[0], letter[1])

string = input().split()
opposite_numbers = []
for index in range (len(string)):
    opposite_number= - int(string[index])
    opposite_numbers.append(opposite_number)
print(opposite_numbers)




