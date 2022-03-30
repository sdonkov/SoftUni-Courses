max_bad_scores=int(input())
name_of_exercise=input()

has_passed=True
bad_score=0
avg_score=0
score_sum=0
number_of_problems=0
last_problem=''
while name_of_exercise!="Enough":
    last_problem=name_of_exercise
    grade=float(input())
    number_of_problems+=1
    score_sum+=grade
    if grade<=4:
        bad_score+=1
        if bad_score==max_bad_scores:
            print(f"You need a break, {max_bad_scores} poor grades.")
            has_passed=False
            break
    name_of_exercise=input()

if has_passed == True:
    avg_score=score_sum/number_of_problems
    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")


