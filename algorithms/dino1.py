from csv import DictReader
from pprint import pprint

def load_data(file1, file2):
    result = []
    with open(file1) as storage1, open(file2) as storage2:
        dr1 = DictReader(storage1)
        dr2 = list(DictReader(storage2))

        for row1 in dr1:
            obj = {}
            obj["name"] = row1.get("name")
            obj["legs"] = int(row1.get("legs"))
            obj["speed"] = float(row1.get("speed"))
            
            result.append(obj)

            for row2 in dr2:
                if obj.get("name") == row2.get("name"):
                    obj["weight"] = float(row2.get("weight"))
                    obj["strength"] = int(row2.get("strength"))

        return result

data = load_data("dino_f.csv", "dino_s.csv")

# pprint(data)

# print(type(data[0].get("legs")))

pprint(sorted([x for x in data if x.get("legs") == 4], key = lambda x: x.get("strength"), reverse = True))