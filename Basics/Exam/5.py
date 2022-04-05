age = input()
sum = 0
adults_number =0
kids_number =0
toys_number = 0
sweaters_number =0
sum_for_toys = 0
sum_for_sweaters = 0
while age != 'Christmas':
    number_age = int(age)
    if number_age <= 16:
        kids_number+=1
        toys_number+=1
    elif number_age >16:
        adults_number+=1
        sweaters_number+=1
    age=input()
sum_for_toys = toys_number * 5
sum_for_sweaters = sweaters_number * 15
print (f"Number of adults: {adults_number}")
print (f"Number of kids: {kids_number}")
print (f"Money for toys: {sum_for_toys}")
print (f"Money for sweaters: {sum_for_sweaters}")