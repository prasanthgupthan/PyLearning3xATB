# mulitple condition

n1 = int(input("Enter number: "))
match n1:
    case 1:
        print("Hello 1")
    case 2:
        print("Hello 2")
    case 3:
        print("Hello 3")
    case 4:
        print("Hello 4")
    case _:
        print("No idea")