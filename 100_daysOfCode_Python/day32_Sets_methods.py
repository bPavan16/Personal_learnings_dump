s1 = {1,2,5,6,8}
s2={3,6,7,8}

# Union of two Sets
print(s1.union(s2))

s1.update(s2)

print(s1,s2)

cities1 = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# print(cities1.union(cities2)) : Gives the intersection
# s1.update(s2) Updates the Set 1 with the values of Set 2

cities3 = cities1.union(cities2)
cities4 = cities1.intersection(cities2)
print(cities3)
print(cities4)

""" 

cities1.issubset()
cities1.issuperset()
cities1.isdisjoint()

 """

#  cities1.remove("somethind")
#  cities1.discard("somethind")

# del is a keyword used to delete Entire set
# Clear is a method used to clear all elements Out of the Set









