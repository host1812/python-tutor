import os

def read_data(f):
    FILE_PATH = os.path.dirname(os.path.realpath(__file__))+"/"+f
    with open(FILE_PATH) as file:
        data = file.read()
        print(type(data))

    return data

def copy(source, destination):
    FILE_PATH = os.path.dirname(os.path.realpath(__file__))+"/"
    with open(FILE_PATH + source) as s, open(FILE_PATH + destination, "w") as d:
        data = s.read()
        d.write(data)

def copy_and_reverse(source, destination):
    with open(source) as s, open(destination, "w") as d:
        d.write(reversed(s.read()))

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(file):
    with open(file) as f:
        data = f.readlines()

    result = {}

    result["lines"] = len(data)
    result["words"] = sum((len(x.split(" ")) for x in data))
    result["characters"] = sum((len(x) for x in data))

    return result

def find_and_replace(file, value, new_value):
    with open(file, "r+") as f:
        data = f.read()
        new_data = data.replace(value, new_value)
        f.write(new_data)

# data = read_data("sample.csv")

# print(data[0])

# copy("sample.csv", "copy.csv")

FILE_PATH = os.path.dirname(os.path.realpath(__file__))+"/"
print(statistics(FILE_PATH + "story.txt"))

# print("hello"[::-1])