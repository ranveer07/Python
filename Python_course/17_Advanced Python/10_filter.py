# def number_greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False
    
number = [1,2,55,5,8,7,345,23,89,3445]

new  = list(filter(lambda x : x > 9, number))
print(new)