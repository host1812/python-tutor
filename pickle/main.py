import pickle
from Dog import Dog

class Abra:
    def __init__(self, a, b):
        self.a = a
        self.b = b

dog = Dog("Char", "Anita")

with open("dog.pickle", "wb") as file:
    pickle.dump(dog, file)
