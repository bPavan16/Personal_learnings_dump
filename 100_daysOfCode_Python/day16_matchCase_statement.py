x=int(input("Enter the value of x :"))

match x:
    case 0:
        print("x is zero")

    case 4:
        print("case is four")

    case _:
        print(x)


