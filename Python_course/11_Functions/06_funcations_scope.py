def add(a,b):
    c = a + b      # local variable
    z = 1
    return c


z = 3    # global variable
print(add(2,4))
print(z)


