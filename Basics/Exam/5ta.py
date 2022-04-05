player_name = input()
most_goals = 0
player_with_most_goals = ''
player_with_hattrick = ''
best_player = ''
while player_name != "END":
    goals_score= int(input())
    if goals_score > most_goals:
        most_goals = goals_score
        best_player = player_name
    if goals_score >= 3 and goals_score<10:
        player_with_hattrick == player_name
    if goals_score >=10:
        break
    player_name = input()


print (f"{best_player} is the best player!")
if goals_score>=10 or goals_score>=3:
    print (f"He has scored {most_goals} goals and made a hat-trick !!!")
if goals_score <3:
    print (f"He has scored {most_goals} goals.")

