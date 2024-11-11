import time
timestamp = time.strftime('%H:%M:%S')

print(timestamp)

hour = int(time.strftime('%H'))
# hour= int(input("Enter Hour"))
# print(hour)

name = input("Enter your Name :  ")


""" 
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

"""

if(hour>=0 and hour<12):
    print("Good Morning",name)

elif(hour>=12 and hour<17):
    print("Good AfterNoon",name)

elif(hour>=17 ):
    print("Good Night",name)









