import os
import csv

def read_data(f):
    with open(f) as file:
        # data = list(csv.reader(file))
        reader = csv.DictReader(file)
        # print(dir(reader))
        data = [x for x in reader]
    return data

FILE_PATH = os.path.dirname(os.path.realpath(__file__))+"/sample.csv"
data = read_data(FILE_PATH)
print(type(data))
print(data[0].get("policyID"))
