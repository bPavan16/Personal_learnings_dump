class Person:
    name = "Harry"
    occupation = "Senior Developer"
    netWorth =100000
    def info(self):
        print(f"{self.name} is a {self.occupation} and has Net Worth of Rs {self.netWorth}")
        # Self means woh object jiske liye yeah call kiya jaa raha hai

a = Person()
a.name = "Shubam"
a.occupation="Accountant"
a.netWorth="5000"
a.info()

print()
print()

b=Person()
b.info()








