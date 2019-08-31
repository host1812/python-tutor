def count_to_f(max):
    count = 1
    while count <= max:
        yield count
        count += 1

print(type(count_to_f))
print(type(count_to_f(5)))

# for x in count_to_f(10):
#     print(x)

# for x in count_to_f(10):
#     print(x)

c = count_to_f(10)

for x in c:
    print(x)

for x in c:
    print(x)
