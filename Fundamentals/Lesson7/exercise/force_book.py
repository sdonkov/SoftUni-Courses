def add_user(forces_dict, to_side, user_add):
    for side, users in forces_dict.items():
        if user_add in users:
            return forces_dict
    if to_side not in forces_dict:
        forces_dict[to_side] = [user_add]
    else:
        forces_dict[to_side].append(user_add)
    return forces_dict

def change_side(forces_dict, to_side, user_change):
    for side, users in forces_dict.items():
        if user_change in users:
            forces_dict[side].remove(user_change)
            return add_user(forces_dict, to_side, user_change)
    return add_user(forces_dict, to_side, user_change)



data = input()
force_book = {}

while data != "Lumpawaroo":
    if "|" in data:
        data = data.split(" | ")
        side = data[0]
        user = data[1]
        force_book = add_user(force_book, side, user)
    else:
        data = data.split(" -> ")
        user = data[0]
        side = data[1]
        force_book = change_side(force_book, side, user)



    data = input()
sorted_force = sorted(force_book.items(), key=lambda kvpt:(-len(kvpt[1]), kvpt[0]))
for side, users in sorted_force:
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {(user)}")
