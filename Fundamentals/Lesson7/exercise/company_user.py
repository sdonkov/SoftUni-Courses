command = input()
companies_dict = dict()

while command != "End":
    command = command.split(" -> ")
    company = command[0]
    id_user = command[1]

    if company not in companies_dict:
        companies_dict[company] = []
    if id_user in companies_dict[company]:
        command = input()
        continue
    #     continue
    companies_dict[company].append(id_user)

    command = input()
for k in companies_dict:
    print(f"{k}")
    for x in range(len(companies_dict[k])):
        print(f"-- {companies_dict[k][x]}")

