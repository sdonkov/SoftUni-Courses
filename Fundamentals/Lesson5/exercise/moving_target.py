def moving_target(info):

    while True:
        input_command = input().split()
        command = input_command[0]

        if command == "End":
            break
        if command == "Shoot":
            index = int(input_command[1])
            differential = int(input_command[2])
            if 0 <= index < len(info):
                info[index] = info[index] - differential
                if info[index] <=0:
                    info.remove(info[index])
        if command == "Add":
            index = int(input_command[1])
            differential = int(input_command[2])
            if 0 <= index <len(info):
                info.insert(index,differential)
            else:
                print("Invalid placement!")

        if command == "Strike":
            index = int(input_command[1])
            differential = int(input_command[2])
            target_len = len(info)
            left = index - differential
            right = index + differential
            if left >=0 and right < target_len:
                info = info[:left] + info[right+1:]
            else:
                print("Strike missed!")
    info= [str(x) for x in info]
    print("|".join(info))


sequence = list(map(int,input().split(" ")))
moving_target(sequence)


