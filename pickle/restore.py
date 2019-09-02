import pickle

with open("dog.pickle", "rb") as file:
    dog = pickle.load(file)

print(type(dog))

print(dog)
print(dog.make_sound())
