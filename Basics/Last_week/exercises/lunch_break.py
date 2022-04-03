import math
name_of_serial = input()
lenght_of_episode = int (input())
break_lenght = int(input())
time_for_lunch = break_lenght / 8
time_for_breath = break_lenght / 4
timeleft_forserial = break_lenght - (time_for_breath+time_for_lunch)
time_needed= lenght_of_episode - timeleft_forserial
left_minutes= timeleft_forserial - lenght_of_episode
if lenght_of_episode > timeleft_forserial:
    print (f"You don't have enough time to watch {name_of_serial}, you need {math.ceil (time_needed)} more minutes.")
elif lenght_of_episode <= timeleft_forserial:
    print (f"You have enough time to watch {name_of_serial} and left with {math. ceil(left_minutes)} minutes free time.")