number_of_people=int(input())
nights_staying = int(input())
travel_cards = int(input())
tickets_for_museum = int(input())

one_night = 20
travel_cards_sum = 1.60
tickets_for_museum_sum = 6.00

total_night = nights_staying * one_night
travel_cards_total = travel_cards * travel_cards_sum
museum_total = tickets_for_museum * tickets_for_museum_sum
one_person_total = total_night + travel_cards_total + museum_total
total_whole = one_person_total * number_of_people
total_with_exp = total_whole + (total_whole*0.25)
print (f'{total_with_exp:.2f}')