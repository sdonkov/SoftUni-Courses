number_of_people= int(input())
season = input()
price=0
total = 0
if season == 'spring':
    if number_of_people <=5:
        price = 50.00
    else:
        price = 48
elif season == 'summer':
    if number_of_people <=5:
        price = 48.50
    else:
        price =45.00
elif season == 'autumn':
    if number_of_people <=5:
        price = 60
    else:
        price = 49.50
elif season == 'winter':
    if number_of_people <=5:
        price = 86
    else:
        price = 85
total = price *number_of_people
if season == 'summer':
    total = total - (total*0.15)
elif season == 'winter':
    total = total + (total*0.08)


print (f'{total:.2f} leva.')