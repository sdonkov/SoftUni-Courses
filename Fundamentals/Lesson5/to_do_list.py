command = input()
list = ["" for i in range (11)]
while command != "End":
    current_string = command.split("-")
    importance = int(current_string[0])
    note = current_string[1]
    list[importance] = note


    command = input()

result = [x for x in list if x !=""]
print(result)

