from Animal import Animal

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "dog")
        self.breed = breed

    def __repr__(self):
        return f"Dog with name of '{self.name}' and is of '{self.breed}' breed."

    def make_sound(self):
        return "Whoof"

    
