my_super = {k: k**2 for k in range(6)}

print(my_super)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {k:v for k,v in zip(list1,list2)}

print(answer)