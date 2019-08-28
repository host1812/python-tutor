def divide(a,b):
    result = 0
    try:
        result = a/b
    except ZeroDivisionError as err:
        return "Please do not divide by zero"
    except TypeError as err:
        return "Please provide two integers or floats"
    else: return result

print(divide(3,"a"))