counties = ("Spain", "Italy","India","England","Germany")

temp = list(counties)

temp.append("Russia")

temp.pop

temp[2] = "Finland"

counties = tuple(temp)

print(counties)

print()
print()
print()
print()

counties = ("paskistam" , "Afganistan", "Bangladesh", "ShriLanka")

counties2= ("Vietnam", "India" , "china")

southEastAsia = counties + counties2

print(southEastAsia)

tuple1= (0,1,2,3,3,3,4,5,6,1,3)

res= tuple1.count(3)
mes= tuple1.index(3)

print()
print()

print("The count of the number 3 in tuple 1 is",res)
print("The index of the number 3 in tuple 1 is",mes)




