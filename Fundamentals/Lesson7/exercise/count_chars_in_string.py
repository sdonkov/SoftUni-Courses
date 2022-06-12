data = input()

dict = {}

data_replaced = data.replace(" ","")

for x in data_replaced:
    if x not in dict:
        dict[x] = 0
    dict[x] +=1

for key,value in dict.items():
    print(f"{key} -> {value}")
