name=input()
academy_points=float (input())
judges=int(input())

points_needed=1250.5

for n in range(judges):
    judge_name=input()
    points_from_judge=float(input())
    academy_points= academy_points + (len(judge_name)*points_from_judge) / 2
    if academy_points>=points_needed:
        print(f"Congratulations, {name} got a nominee for leading role with{academy_points: .1f}!")
        break
if academy_points <points_needed:
        print(f"Sorry, {name} you need {(points_needed-academy_points):.1f} more!")
