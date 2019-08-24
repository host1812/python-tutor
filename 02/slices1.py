with open("./sample.txt") as f:
    sample = list()
    sample += f.read().split(" ")

print(sample)

# sample[:5] = ["REMOVED"]

sample = sample[-3:-10:-1]

print("\n" * 3)

print(sample)