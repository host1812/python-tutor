def debug(preffix):
    print("in decorator")
    print(f"preffix: {preffix}")

    def inner(fn):
        print("in inner")
        print(f"func name to call is: {fn.__name__}")

        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return inner

@debug("df")
def cool_num(n):
    return n

print(cool_num(100))