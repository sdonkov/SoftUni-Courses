player_name = input()
succses_shots = 0
start_points = 301
unsuccses_shots = 0
pole = input()
while pole != "Retire":
    points = int(input())
    if pole == 'Singe':
        points = points * 1
    elif pole == 'Double':
        points = points * 2
    elif pole == 'Triple':
        points = points * 3
    if points > start_points:
        unsuccses_shots+=1
    else:
        succses_shots+=1
        start_points-= points
    if start_points == 0:
        break
    pole = input()
if start_points ==0:
        print (f'{player_name} won the leg with {succses_shots} shots.')
else:
        print (f"{player_name} retired after {unsuccses_shots} unsuccessful shots.")
