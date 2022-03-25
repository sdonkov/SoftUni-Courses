hours = int (input())
day_of_week = input ()
if hours >=10 and hours <= 18 and day_of_week != "Sunday":
    print ("open")
else:
    print ("closed")