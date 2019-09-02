from pprint import pprint
import json

def load_data(file):
    with open(file) as storage:
        data = json.load(storage)

    return data

data = load_data("sample.json")

# sorted = sorted(data, key=lambda x: x.get("Age"))

sorted = sorted(data, key=lambda x: sum(child.get("age", 0) for child in x.get("Children", 0)))

# print(sorted(data, key = lambda x: len(x.get("Children", 0))))

# pprint(sorted)