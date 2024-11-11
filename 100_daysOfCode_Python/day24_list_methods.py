li = [1,2,4,6]
print(li)
li.append(7)
print(li)

li=[43,52,12,14,67,8,92,556,1]
li.sort()
print(li)
print("reverse sorting")
li.sort(reverse=True)
print(li)

li=[43,52,12,14,67,8,92,556,1]
print(li)
li.reverse()
print(li)

li=[43,52,1,12,14,1,67,8,92,556,1]
print(li.index(1))
print(li.count(1))
m=li
m[0]=0
print("m",m)
print("li",li)

li=[43,52,1,12,14,1,67,8,92,556,1]
n=li.copy()
print(n) 

li.insert(1,899)
print(li)

k=[900,1001,3123]
# li.extend(k)
# print(li)

q=li+k
print(q)
