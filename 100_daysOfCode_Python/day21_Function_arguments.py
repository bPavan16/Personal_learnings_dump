def average(a=9, b=1):
    print("a =", a)
    print("b =", b)
    print("The average is", (a+b)/2)


def name(fname, mname="light", lname="libert"):
    print("HELLO", fname, mname, lname)


def average2(*numbers):
    sum = 0
    print("The type of num is", type(numbers))
    for i in numbers:
        sum = sum+i
    # print("The average is : ", sum/len(numbers))

    return sum/len(numbers)


average(b=5)
average(b=45, a=9)


name("amy")
name("Amy", "Jain")

c = average2(5, 2, 35, 52, 25)
print("The avg is", c)
