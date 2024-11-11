class Employee:
    company= "Apple"

    def __init__(self,pname):
        self.pname = pname

    def show(self):
        print(f"The name is {self.pname} and he works in the company called {self.company}")

    @classmethod
    def ChangeCompany(cls,newCompany):
        cls.company = newCompany
    

e1 = Employee("Harry")
e1.show()
e1.ChangeCompany("Coca Cola")
e1.show()
print(Employee.company)

