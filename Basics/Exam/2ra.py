shirt_price = float (input())
price_for_ball = float (input())

short_price = shirt_price *0.75
socks_price = short_price *0.2
shoes_price = 2* (shirt_price + short_price)

total_sum = shoes_price + short_price + shirt_price + socks_price
total_sum_with_discount = total_sum - (total_sum*0.15)
needed_money= price_for_ball - total_sum_with_discount
if total_sum_with_discount >=price_for_ball:
    print ("Yes, he will earn the world-cup replica ball!")
    print (f"His sum is {total_sum_with_discount:.2f} lv.")
else:
    print ("No, he will not earn the world-cup replica ball.")
    print (f"He needs {needed_money:.2f} lv. more.")
