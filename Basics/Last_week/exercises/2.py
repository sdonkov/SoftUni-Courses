import math
processors_planned = int(input())
number_of_employee = int(input())
work_days = int (input())

hours_working = 8
price_of_one_proc = 110.10
hours_needed_for_one_proc = 3

working_hours_total = number_of_employee * work_days * 8
proc_made = working_hours_total / 3

# profit = (math.floor(proc_made) - processors_planned) * price_of_one_proc
# losses = (processors_planned - math.floor(proc_made)) * price_of_one_proc
if processors_planned <= proc_made:
    profit = (math.floor(proc_made) - processors_planned) * price_of_one_proc
    print (f"Profit: -> {abs(profit):.2f} BGN")
elif processors_planned > proc_made:
    losses = (processors_planned - math.floor(proc_made)) * price_of_one_proc
    print (f"Losses: -> {abs(losses):.2f} BGN")