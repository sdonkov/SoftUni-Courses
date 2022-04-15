collection = input().split("|")
budget = float(input())
new_budget = 0
sell_items = []
sell_price = 0
profit = 0
total = 0
for _ in collection:
    new_split = _.split("->")
    type = new_split[0]
    price = float(new_split[1])
    if type == "Clothes" and price <=50 :
        if budget >=price:
            budget -= price
            new_budget += price+(price * 0.4)
            sell_price = (price + (price * 0.4))
            sell_items.append(sell_price)
            profit = sell_price - price
            total += profit
    if type == "Shoes" and price <= 35:
        if budget >=price:
            budget -=price
            new_budget +=price +(price *0.4)
            sell_price = price + (price *0.4)
            sell_items.append(sell_price)
            profit = sell_price - price
            total+= profit
    if type == "Accessories" and price <= 20.50:
        if budget >= price:
            budget-=price
            new_budget += price+ (price * 0.4)
            sell_price = float(price + (price * 0.4))
            sell_items.append(sell_price)
            profit = sell_price - price
            total+=profit
# print(sell_items)
for sth in sell_items:
    print(f"{sth:.2f} ", end="")
print()
print(f"Profit: {total:.2f}")
if profit + new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
