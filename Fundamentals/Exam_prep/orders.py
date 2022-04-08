# orders = int(input())

total = 0
#
# while True:
#     price_per_capsule = float(input())
#     days = int(input())
#     capsules_counter = int(input())
#     total = price_per_capsule * days * capsules_counter
#     print (f"The price for the coffee is: ${total:.2f}")


orders = int(input())
total_price = 0
for number in range (orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_counter = int(input())
    total = price_per_capsule * days * capsules_counter
    print (f"The price for the coffee is: ${total:.2f}")
    total_price += total
print (f"Total: ${total_price:.2f}")