number_of_model_computers = int(input())
possible_sales = 0
sales_made = 0
total_sales = 0
rating = 0
avg_rating = 0
for n in range (number_of_model_computers):
    number=int(input())
    if number % 10 == 2:
        possible_sales= number //10
        sales_made = possible_sales*0
        rating+= 2
    elif number % 10 ==3:
        possible_sales = number // 10
        sales_made = possible_sales *0.5
        total_sales+=sales_made
        rating += 3
    elif number % 10 ==4:
        possible_sales = number //10
        sales_made = possible_sales * 0.7
        total_sales+=sales_made
        rating +=4
    elif number % 10 == 5:
        possible_sales = number //10
        sales_made = possible_sales *0.85
        total_sales+=sales_made
        rating += 5
    elif number % 10 == 6:
        possible_sales = number // 10
        sales_made = possible_sales * 1
        total_sales+=sales_made
        rating += 6

avg_rating = rating / number_of_model_computers

print (f'{total_sales:.2f}')
print (f'{avg_rating:.2f}')


