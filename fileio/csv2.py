'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

from csv import writer, reader
import os

def add_user(f, first, last):
    with open(f, "a") as file:
        csvw = writer(file)
        csvw.writerow([first, last])

def print_users():
    with open(os.path.dirname(os.path.realpath(__file__))+"/users.csv") as f:
        csvr = reader(f)
        next(csvr)
        for r in csvr:
            print(r)

from csv import DictReader

def find_user(first, last):
    with open(os.path.dirname(os.path.realpath(__file__))+"/users.csv") as file:
        dr = DictReader(file)
        
        # print(dr)
        # print(next(dr))

        i=1
        for r in dr:
            if r.get("First Name") == first and r.get("Last Name") == last:
                return i
            i += 1

        return "Not Here not found."


# FILE_PATH = os.path.dirname(os.path.realpath(__file__))+"/users.csv"
# add_user(FILE_PATH, "df", "dd")

# print_users()

result = find_user("Colt", "Steele")
print(result)