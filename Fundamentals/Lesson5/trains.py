num_of_wagoons = int(input())
train = [0 for x in range (num_of_wagoons)]
# for x in range (num_of_wagoons):
#     train.append(0)

command = input()
while command!= "End":
    split_list_commands = command.split(" ")
    current_command = split_list_commands[0]
    if current_command == "add":
        number = int(split_list_commands[1])
        train[-1] +=number
    if current_command == "insert":
        index = int(split_list_commands[1])
        number = int(split_list_commands[2])
        train[index] += number
    if current_command == "leave":
        index = int(split_list_commands[1])
        number = int(split_list_commands[2])
        train[index] -=number

    command=input()

print(train)
