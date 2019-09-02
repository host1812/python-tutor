import os
from csv import DictReader, DictWriter

def update_users(old_first, old_last, new_first, new_last):
    updates = 0
    with open(os.path.dirname(os.path.realpath(__file__))+"/users.csv") as storage:
        data = list(DictReader(storage))

    for obj in data:
        if obj.get("First Name") == old_first and obj.get("Last Name") == old_last:
            obj["First Name"] = new_first
            obj["Last Name"] = new_last
            updates += 1

    with open("users.csv", "w") as storage:
        dw = DictWriter(storage, ["First Name", "Last Name"])
        dw.writeheader()
        for obj in data:
            dw.writerow(obj)

    return f"Users updated: {updates}."


print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.