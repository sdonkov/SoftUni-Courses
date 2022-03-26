hours_exam = int(input())
minutes_exam = int (input())
arriving_hours = int (input())
arriving_minutes = int (input())

time_for_exam_in_minutes = (hours_exam * 60) + minutes_exam
time_of_arriving = (arriving_hours*60) + arriving_minutes
diff = time_for_exam_in_minutes - time_of_arriving
if diff < 0 :
    print ("Late")
    diff=abs(diff)
    if diff >= 60:
        hours= diff//60
        minutes=diff%60
        print (f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{diff} minutes after the start")

elif 0 <= diff <=30:
    print("On time")
    if diff >0:
        print(f"{diff} minutes before the start")
elif diff> 30:
    print ("Early")
    if diff >= 60:
        hours = (time_for_exam_in_minutes - time_of_arriving) // 60
        minutes = (time_for_exam_in_minutes - time_of_arriving) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print (f"{diff} minutes before the start")



