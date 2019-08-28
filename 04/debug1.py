class Person:
    def __init__(self):
        self.name = "Default"
        self.age = 0
        self.skin_color = "Default"


a = 100
b = 3

c = a + b

print(c)

p = Person()
import pdb ; pdb.set_trace()
print(p.name)