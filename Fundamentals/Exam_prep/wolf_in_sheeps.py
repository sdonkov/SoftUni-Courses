animals = input()

animals_list = []
for animal in animals.split(","):
    animals_list.append(str(animal).strip())

farmer_position = len(animals_list) +1

if animals_list[-1].strip() == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    animal_postion = len(animals_list) - animals_list.index("wolf") - 1
    print(f'Oi! Sheep number {animal_postion}! You are about to be eaten by a wolf!')