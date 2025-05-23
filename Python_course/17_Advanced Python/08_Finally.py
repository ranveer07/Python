# a = int(input("Enter the number 1: "))
# b = int(input("Enter the number 2: "))

# try:
#     c = a/b
#     print(c)
# except Exception as e:
#     print(e)

# finally:
#     print("Awesome it is executed !!")





def divide(a,b):
        try:
            c = a/b
            print(c)
        except Exception as e:
            print(e)

        finally:
            print("Awesome it is executed !!")





a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
divide(a,b)