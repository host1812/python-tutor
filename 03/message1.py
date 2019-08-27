'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(**kwargs):
    
    result = 0
    
    make_float = kwargs.get("make_float")
    operation = kwargs.get("operation")
    first = kwargs.get("first")
    second = kwargs.get("second")
    message = kwargs.get("message")
    print(f"debug: message = {message}")
    if not message:
        print(f"debug: setting message to default")
        message = "The result is"
    
    print(f"debug: message = {message}")

    if operation == "add":
        if make_float: return float(first + second)
        else: result = int(first + second)
    elif operation == "substract":
        if make_float: return float(first - second)
        else: result = int(first - second)
    elif operation == "multiply":
        if make_float: return float(first * second)
        else: result = int(first * second)
    elif operation == "divide":
        if make_float: return float(first / second)
        else: result = int(first / second)
    
    print(f"debug: message = {message}")
    return "{} {}".format(message, result)
    
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"
