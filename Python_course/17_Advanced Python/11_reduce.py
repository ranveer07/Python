from functools import reduce
numbers = [1,2,4,7,2,5]
#         [3,4,7,2,5]                Program works like this
#         [7,7,2,5]
#         [14,2,5]
#         [16,5]
#         [21]

def sum(a,b):
    return a + b

c = reduce(sum,numbers)
print(c)
