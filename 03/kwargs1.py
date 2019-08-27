def somef(**kwargs):
    global argums
    kwargs["super"] = "duper"
    print(f"debug: {argums is kwargs}")
    return(kwargs)

argums = {"test" : "abra", "kadra" : "tyi"}

print(somef(**argums))
print(argums)