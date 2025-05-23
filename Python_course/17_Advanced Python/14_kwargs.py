def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")


marks(shubham=65,ranveer=78,hardik=69,karthik=91)