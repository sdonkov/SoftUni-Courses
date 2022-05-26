from collections import deque

quantity = int(input())
name = input()
line = deque()

while name != "Start":
    line.append(name)
    name = input()

command = input()
while not command == "End":
    if 'refill' in command:
        new_cmd = command.split(' ')
        refill_amount = int(new_cmd[1])
        quantity += refill_amount
    elif int(command) <= quantity:
        print(f"{line.popleft()} got water")
        quantity -= int(command)
    else:
        print(f"{line.popleft()} must wait")
    command = input()

print(f"{quantity} liters left")
