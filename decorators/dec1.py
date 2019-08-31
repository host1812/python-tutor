def debug(fn):
    def wrapper(*args, **kwargs):
        print(f"DEBUG: {fn.__name__}: started")
        print(args)
        # print(*args)
        print(kwargs)
        # print(**kwargs)
        fn(*args, **kwargs)
        print(f"DEBUG: {fn.__name__}: started")
    return wrapper

@debug
def print_name(name):
    print(f"Hello, my dear {name}!")

print_name(name = "Alex")