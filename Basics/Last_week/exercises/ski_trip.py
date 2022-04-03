days_staying=int(input())
type_of_room = input()
rating= input()

total = 0
room_for_one_person = 18
apartment = 25
president_apartment = 35
nights_staying= days_staying - 1

if type_of_room == 'room for one person':
    total = nights_staying*room_for_one_person
elif type_of_room == 'apartment':
    if days_staying <10:
        total = (nights_staying * apartment)
        total = (nights_staying * apartment) - total * 0.3
    elif 10 < days_staying <=15:
        total = (nights_staying * apartment)
        total = (nights_staying * apartment) - total * 0.35
    elif days_staying >15:
        total = (nights_staying * apartment)
        total = (nights_staying * apartment) - total * 0.5
elif type_of_room == 'president apartment':
    if days_staying <10:
        total = (nights_staying*president_apartment)
        total = (nights_staying * president_apartment) - total * 0.1
    elif 10< days_staying <=15:
        total = (nights_staying * president_apartment)
        total = (nights_staying * president_apartment) - total * 0.15
    elif days_staying>15:
        total = (nights_staying * president_apartment)
        total = (nights_staying * president_apartment) - total * 0.2
if rating == "positive":
    total=total*0.25 + total
elif rating == "negative":
    total= total - total * 0.1
print (f"{total: .2f}")
