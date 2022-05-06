def el_distribution(electrons):
    filled =[]
    counter = 1
    while True:
        max_shell_number = 2 * (counter ** 2)
        if electrons > max_shell_number:
            electrons = electrons - max_shell_number
            filled.append(max_shell_number)
        else:
            filled.append(electrons)
            break
        counter+=1
    print(filled)




electron=int(input())
el_distribution(electron)