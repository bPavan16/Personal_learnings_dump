
class Math:
    def __init__(self,num):
        self.num = num

    def addtoNum(self,n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a+b
    
""" 
result = Math.add(2,1)
print(result)
"""

a= Math(5)
print(a.num)

a.addtoNum(6)
print(a.num)

print(Math.add(1,2))

















