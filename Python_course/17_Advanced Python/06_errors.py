# while True:
#     try:
#         a = int(input("Enter the number 1: "))
#         b = int(input("Enter the number 2: "))

#         print(f" This is the sum of two number {a / b}")

#     except ValueError:
#         print("Please dont perform bad typecast")

#     except ZeroDivisionError:
#         print("Dont divide by zero")

#     except Exception as e:
#         print("Some error Occur", e)



a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))

if b == 0:
    raise ValueError("Please dont divide with zero")


print(f" This is the division 3of two number {a / b}")