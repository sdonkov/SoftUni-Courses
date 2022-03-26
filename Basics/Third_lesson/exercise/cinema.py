type_of_movie= input ()
number_of_rows = int(input())
number_of_collumns= int(input())
ticket_price = 0
income = 0
if type_of_movie == "Premiere":
    ticket_price = 12.00

if type_of_movie == "Normal":
    ticket_price = 7.50


if type_of_movie == "Discount":
    ticket_price = 5.00
income = ticket_price * number_of_collumns * number_of_rows
print (f"{income: .2f} leva")