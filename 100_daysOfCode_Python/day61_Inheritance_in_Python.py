class Employee:
    def __init__(self,name,ID):
        self.name = name
        self.ID=ID

    def showDetails(self):
        print(f"The name of Employee :{self.ID} is {self.name} ")

class Programmer(Employee):
    def ShowLang(self):
        print(f"The defaut Language is Python")

e1 = Employee("Rohan Ds",1231)
e1.showDetails()
e2 = Programmer("Harry",8698)
e2.showDetails()
e2.ShowLang()













