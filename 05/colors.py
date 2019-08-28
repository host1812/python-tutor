from termcolor import colored, COLORS

text = colored("Hello World", color="red")

print(text)

for c in COLORS:
    print(c)


def some():
    """Short function description.

    More detailed descript.
    This function is very important.
    Please do not delete this function.
    Please, please, please."""
    return 36

import pdb ; pdb.set_trace()
print(some())