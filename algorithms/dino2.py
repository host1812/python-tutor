from csv import DictReader
from pprint import pprint

class Dino:
    def __init__(self, name=None, legs=0, speed=0, weight=None, strength=None):
        self.name = name
        self.legs = legs
        self.speed = speed
        self.weight = weight
        self.strength = strength

    def __repr__(self):
        return f"name: {self.name}, legs: {self.legs}, speed: {self.speed}, weight = {self.weight}, strength = {self.strength}"

def load_data(file1, file2):
    result = []
    with open(file1) as storage1, open(file2) as storage2:
        dr1 = DictReader(storage1)
        dr2 = list(DictReader(storage2))

        result = []
        for row in dr1:
            dino = Dino(row.get("name"), int(row.get("legs")), float(row.get("speed")))
            for row2 in dr2:
                if row2.get("name") == dino.name:
                    dino.weight = float(row2.get("weight"))
                    dino.strength = int(row2.get("strength"))
            result.append(dino)

        

    return result

data = load_data("dino_f.csv", "dino_s.csv")

# pprint(data)

pprint(sorted(filter(lambda x: x.legs == 2 ,data), key = lambda x: x.strength, reverse = True))
