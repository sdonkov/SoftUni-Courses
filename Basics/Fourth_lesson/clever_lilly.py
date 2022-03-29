age = int(input())
price_of_laundry = float(input())
price_of_toy = int(input())

odd_birthday = 0
even_birthday = 0
amount=0
toy_total=0
total_sum=0
for number in range (1, age+1):
    if number %2==0:
        amount+=10
        even_birthday+=amount -1
    else:
        odd_birthday+=1
        toy_total=odd_birthday*price_of_toy
total_sum = even_birthday + toy_total
if total_sum >=price_of_laundry:
    print(f"Yes! {abs(total_sum-price_of_laundry):.2f}")
else:
    print(f"No! {abs(price_of_laundry-total_sum):.2f}")

