
x = 4
y = 6
print(x)


def hello():
    global x 
    x = 5

    print("Hello")
    print(f"The value of x is = {x}")
    print(f"The value of y is = {y}")

print()
print()

hello()

print()
print()


print(f"The value of Global var x is : {x} ")
print(f"The value of Global var y is : {y} ")
