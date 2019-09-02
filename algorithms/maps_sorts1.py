from pprint import pprint
import json

def load_data(file):
    with open(file) as storage:
        data = json.load(storage)

    return data

data = load_data("sample.json")

sorted = sorted(data, key=lambda x: x.get("Age"))

pprint(sorted)