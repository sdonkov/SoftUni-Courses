steps_sum=0
goal=10000
while True:
    steps_made=input()
    if steps_made == "Going home":
        steps_made = int(input())
        steps_sum+=steps_made
        if steps_sum >=goal:
            print("Goal reached! Good job!")
            print(f"{steps_sum-goal} steps over the goal!")
        else:
            print(f"{goal - steps_sum} more steps to reach goal.")
        break
    steps_sum+=int(steps_made)
    if steps_sum>=goal:
        print("Goal reached! Good job!")
        print(f"{steps_sum - goal} steps over the goal!")
        break

