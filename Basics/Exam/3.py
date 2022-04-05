sweet = input()
sweet_purchased = int(input())
december_date = int(input())

cake_price =0
souffle_price = 0
baklava_price = 0
sum =0
discount_sum = 0
if sweet == "Cake" and december_date <=15:
    sum = 24 * sweet_purchased
elif sweet == "Souffle" and december_date <=15:
    sum = 6.66 * sweet_purchased
elif sweet == "Baklava" and december_date <=15:
    sum= 12.6 *sweet_purchased
elif sweet == 'Cake' and december_date >15:
    sum = 28.7 *sweet_purchased
elif sweet == "Souffle" and december_date >15:
    sum = 9.8 * sweet_purchased
elif sweet == 'Baklava' and december_date >15:
    sum = 16.98 * sweet_purchased

if december_date <=22 and 100<=sum<=200:
    discount_sum = sum - (sum * 0.15)
elif december_date <=22 and sum > 200:
    discount_sum = sum - (sum * 0.25)
if december_date <= 15:
    bonus_discount = discount_sum - (discount_sum * 0.1)
    print (f'{bonus_discount:.2f}')
elif december_date > 15 and december_date <=22:
    print (f'{discount_sum:.2f}')
elif december_date>22:
    print(f'{sum:.2f}')
elif december_date > 24:
    print ( )