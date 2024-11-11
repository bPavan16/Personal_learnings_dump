class Person:
    def __init__(self,n,o,w):
        print("HEY I AM A PERSON")
        self.name = n
        self.occupation = o
        self.netWorth=w

    def info(self):
        print(f"{self.name} is a {self.occupation} and has Net Worth of Rs {self.netWorth}")
        # Self means woh object jiske liye yeah call kiya jaa raha hai


A = Person("Harry","Developer",10000)
B = Person("Divya","HR",1000)
A.info()

