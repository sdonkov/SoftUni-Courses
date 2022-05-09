def inventory(data):
    inventory_list = data
    while True:
        command = input().split(" - ")
        if command[0] == "Craft!":
            break
        item = command [1]
        if command [0] == "Collect":
            if item not in inventory_list:
             inventory_list.append(item)
        if command [0] == "Drop":
            if item in inventory_list:
                inventory_list.remove(item)
        if command [0] == "Combine Items":
            item=command[1].split(":")
            old_item = item[0]
            new_item = item[1]
            if old_item in inventory_list:
                index_old_element = inventory_list.index(old_item)
                inventory_list.insert(index_old_element + 1, new_item)
                # inventory_list.append(new_item[1])
            # if command[1] in inventory_list:
            #     inventory_list.append(command[2])
        if command [0] == "Renew":
            if item in inventory_list:
                inventory_list.remove(item)
                inventory_list.append(item)
    print(", ".join(inventory_list))





journal = input().split(", ")
# command = input().split(" - ")
inventory(journal)