    

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks For USing This Function")
    return mfx


@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(f"The Sum of {a} and {b} = {a+b} ")
    
greet(hello())
add(5,4) 

















