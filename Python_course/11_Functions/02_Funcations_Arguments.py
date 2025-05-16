def add(a,b,plus=0):   
    x = a + b + plus       
    return x

c = add(3,4,1)     
print(c)                    # default aruguments


d = add(plus=1,a=3,b=4)     # keywords arguments
print(d) 