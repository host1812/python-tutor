from functools import wraps

def only_ints(fn):
    def wrapper(*args, **kwargs):
        if any(type(i) != int for i in args):
            return "Please only invoke with integers."
        if any(type(v) != int for k,v in kwargs.items()):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return wrapper

@only_ints
def add(a,b):
    return a+b

print(add(1,2))
print(add(a=1,b=2.0))