record_in_sec = float (input())
meters = float (input())
sec_for_one_meter = float (input())
swim_distance = meters * sec_for_one_meter
suprotivlenie =  (meters // 15) * 12.5
total_time = swim_distance + suprotivlenie
needed_time = record_in_sec - total_time
if total_time < record_in_sec:
  print (f"Yes, he succeeded! The new world record is{abs(total_time): .2f} seconds.")
elif total_time >=record_in_sec:
    print (f"No, he failed! He was{abs (needed_time): .2f} seconds slower.")





