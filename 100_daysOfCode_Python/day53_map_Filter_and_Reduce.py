
def cube(x):
    return x*x*x

print(cube(2))

l = [1,2,3,4,5]

""" 
newl =[]
for item in l:
    newl.append(cube(item))

print(newl) 
"""

newl = list(map(cube,l))
print(newl)

# FILTER 

def greater(x):
    return x>2

newnewl= list(filter(greater,l))
print(newnewl)

# REDUCE

from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y:x+y, numbers)
print(sum)

