# THE               
""" 
f =open('myfile.txt','r')
while True:
    line = f.readline()
    print(line)
    if not line:
        # print(line,type(line))
        break

 """

""" 

i =0
f = open('marks.txt','r')
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of the student {i} in Maths are : {m1}")
    print(f"Marks of the student {i} in Maths are : {m2}")
    print(f"Marks of the student {i} in Maths are : {m3}")

"""

""" 

f= open('LinesWrite.txt','w')
lines =['line1\n','line2\n','line3\n','line4\n']
f.writelines(lines)
f.close()

"""



    








