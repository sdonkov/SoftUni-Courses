def new_function(data,last_postion_s):
    result = [x for x in data if x ==0]
    print(f"Cupid's last position was {last_postion_s}.")
    if len(result)!= len(data):
        diff = len(data) -len(result)
        print(f"Cupid has failed {diff} places.")
    else:
        print("Mission was successful.")
def heart_delivery (data):
    current_position = 0
    last_position = 0
    while True:
        command= input().split()
        if command[0] == "Love!":
            break
        index = int(command[1]) + current_position
        if index >= len(data):
            index = 0
        if -1 < index <=len(data):
            if data[index] > 0:
                data [index] -=2
                if data[index] ==0:
                    print (f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")
        last_position =index
        current_position=index
    new_function(data,last_position)

string = list(map(int,input().split("@")))
heart_delivery(string)