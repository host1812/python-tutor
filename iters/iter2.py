class Counter():
    def __init__(self, low, high):
        self.low = low
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.high:
            value = self.current
            self.current +=1
            return value
        
        raise StopIteration


c = Counter(0, 5)

iter(c)

for x in Counter(0, 2):
    print(x)

for y in c:
    print(y)