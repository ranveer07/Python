def add(a,b):
    c = a + b
    global z    # modified gloabl variable by using global function
    z = 7 
    return c



z = 4    # gloabl variable
print(add(4,2))
print(z)
