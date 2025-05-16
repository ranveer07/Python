number = int(input("Enter your lucky number:"))

match number:
    case 1:
        print("You won 3 core")
    case 5:
        print("You won Car")
    case 7:
        print("You won a International Trip")
    case 45:
        print("You won 264 runs in ODI")
    case _:
        print("Better luck Next time")