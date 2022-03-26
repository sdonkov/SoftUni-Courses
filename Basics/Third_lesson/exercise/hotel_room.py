month= input()
nights= int (input())
price_of    _night = 0
studio_price=0
apartment_price=0
total_studio=0
total_apartment = 0
room_type = ''


if month == "May" or month == "October":
    studio_price= 50
    apartment_price=65
    total_studio = studio_price* nights
    total_apartment = apartment_price* nights
    if nights > 7 and nights <14:
        total_studio = total_studio - total_studio *0.05
    elif nights >14:
        total_studio = total_studio - total_studio * 0.3
        total_apartment = total_apartment - total_apartment* 0.1
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    total_studio = studio_price* nights
    total_apartment = apartment_price* nights
    if nights > 14:
        total_studio= total_studio - total_studio * 0.2
        total_apartment = total_apartment - total_apartment* 0.1
elif month == "July" or month == "August":
    studio_price = 76.00
    apartment_price = 77.00
    total_studio = studio_price * nights
    total_apartment = apartment_price * nights
    if nights > 14:
        total_apartment = total_apartment - total_apartment* 0.1
print (f"Apartment:{total_apartment: .2f} lv.")
print (f"Studio:{total_studio: .2f} lv.")
