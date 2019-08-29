class Pet:
    @classmethod
    def from_keys(cls, kwargs):
        print(kwargs)
        print("tail" not in kwargs)
        print("speed" not in kwargs)
        print("name" not in kwargs)
        if "speed" or "name" or "tail" not in kwargs:
            print("error!")

        return cls()
    
    def __init__(self, name, speed, tail = False):
        self.name = name
        self.speed = speed
        self.tail = tail

    def __repr__(self):
        return f"{self.name} can run up to {self.speed} mph and have tail: {self.tail}."

p1 = Pet("Su", 20.0, True)

print(p1)

p2 = Pet.from_keys({"name": "Alex", "speed": 25.0, "tail": True})

print(p2)