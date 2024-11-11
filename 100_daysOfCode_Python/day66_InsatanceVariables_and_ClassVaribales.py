
class Employee:
    companyName = "Apple"
    def __init__(self,name):
        self.name = name
        self.raise_amt = 0.01

    def showDetails(self):
        print(f"The name of the Employee is : {self.name} and The rasie amount is {self.raise_amt} in Company : {self.companyName}")
    

emp1 = Employee("Hatr")
emp1.showDetails()        
emp2 = Employee("Hatifr")
emp2.raise_amt=0.5
emp2.companyName="Apple India"
emp2.showDetails()        

# Employee.showDetails(emp1)

























