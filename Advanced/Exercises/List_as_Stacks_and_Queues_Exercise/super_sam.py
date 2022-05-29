from collections import deque

green_duration = int(input())
free_window = int(input())

command = input()
cars = deque()
passed_cars = 0
crashed = False

while command != "END":
    if command == 'green':
        if cars:
            current = cars.popleft()
            seconds_left = green_duration - len(current)
            while seconds_left > 0:
                passed_cars += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                passed_cars += 1
            if free_window >= abs(seconds_left):
                if seconds_left < 0:
                    passed_cars += 1
            else:
                index = free_window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[index]}.")
                crashed = True
                break

    else:
        cars.append(command)
    command = input()


if not crashed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")

