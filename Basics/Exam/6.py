location_number = int(input())
for number in range (location_number):
    average = 0
    total_gold = 0
    needed_gold = 0
    expected_value = float(input())
    days = int(input())
    for gold in range (days):
        gold_received_for_a_day = float(input())
        total_gold +=gold_received_for_a_day
        average = total_gold / days
    if average >= expected_value:
        print ( f"Good job! Average gold per day: {average:.2f}.")
        continue
    else:
        needed_gold = expected_value - average
        print (f"You need {needed_gold:.2f} gold.")
        continue