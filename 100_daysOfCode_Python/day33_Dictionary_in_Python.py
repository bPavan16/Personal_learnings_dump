dict = {
    "Harry": "Human Being",
    "Spoon": "Object"
}

print(dict["Harry"])

# Dictionary is used for odered Collection of Data and items in a variable
# They Store Multiple Variables under a Single Variable
# They are Seperated by Commas and Enclosed Within Curley Braces

emp = {
    344: "Harry",
    56: "Subham",
    678: "Zakhir",
    567: "Neha"
}

info ={
    'name' : 'karan',
    'age' : 19,
    'eligible' : True,
}

print(info['name'])
print(info.get('name2')) 
# info.get("")  doent give an error but returns NULL

for key in info.keys():
    print(f"The value of the key {key} is {info[key]}")

print()
print()


for key,value in info.items():
    print(f"The value of the key {key} is {value}")









