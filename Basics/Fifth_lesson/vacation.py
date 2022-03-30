money_needed_for_vacation=float(input())
available_money=float(input())

days_passed=0
spending_counter=0
while available_money<money_needed_for_vacation and spending_counter<5:
    desicion=input()
    money=float(input())
    days_passed+=1
    if desicion=="spend":
        available_money-=money
        spending_counter+=1
        if available_money<0:
            available_money=0

    elif desicion=="save":
        available_money+=money
        spending_counter=0



if spending_counter==5:
    print("You can't save the money.")
    print(days_passed)
if available_money>=money_needed_for_vacation:
    print(f"You saved the money for {days_passed} days.")
