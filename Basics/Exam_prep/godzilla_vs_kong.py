
time_for_pics = int(input())
scenes = int(input())
time_for_one_scene = int(input())

preparation = time_for_pics *0.15
time_needed = preparation + (scenes*time_for_one_scene)

time_left = time_for_pics - time_needed
if time_for_pics >=time_needed:
    print (f"You managed to finish the movie on time! You have {time_left:.0f} minutes left!")
else:
    print (f"Time is up! To complete the movie you need {(time_needed - time_for_pics):.0f} minutes.")