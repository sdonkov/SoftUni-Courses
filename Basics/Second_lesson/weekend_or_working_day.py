day_of_week = input()
type_of_the_day = ""
if day_of_week == "Monday":
    type_of_the_day = "Working day"
elif day_of_week == "Tuesday":
    type_of_the_day = "Working day"
elif day_of_week == "Wednesday":
    type_of_the_day = "Working day"
elif day_of_week == "Thursday":
    type_of_the_day = "Working day"
elif day_of_week == "Friday":
    type_of_the_day = "Working day"
elif day_of_week == "Saturday":
    type_of_the_day ="Weekend"
elif day_of_week == "Sunday":
    type_of_the_day = "Weekend"
else:
    print("Error")
print (type_of_the_day)