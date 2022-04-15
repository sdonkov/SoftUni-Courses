energy = 100
coins = 100
events = input().split("|")
closed= False

for type in events:
    current_command = type.split("-")
    current_event = current_command[0]
    current_coins = int(current_command[1])
    current_energy = int(current_command[1])
    if current_event == "rest":
        if energy + current_energy >100:
            print("You gained 0 energy.")
        elif energy + current_energy <100:
            energy += current_energy
            print(f"You gained {current_energy} energy.")
        print(f"Current energy: {energy}.")
    elif current_event == "order":
        if energy - 30 >=0:
            coins +=current_coins
            energy -= 30
            print(f"You earned {current_coins} coins.")
        else:
            energy +=50
            print("You had to rest!")
    else:
        coins -=current_coins
        if coins >0:
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            closed=True
            break
if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

# print(events)
# current_event = events[0]
# current_energy = events[1]
