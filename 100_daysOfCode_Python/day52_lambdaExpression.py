def double(x):
    return x*2


def apply(fx, value):
    return 6 + fx(value)


def double2(x): return x*2
def cube(x): return x*x*x


print(double(5))
print(double2(5))
print(cube(5))

print(apply(lambda x: x *x *x, 2))
