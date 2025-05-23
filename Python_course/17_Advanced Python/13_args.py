def sum(*args):
    total = 0
    for item in args:
        total +=  item
    return total


print(sum(2,34,6,2))