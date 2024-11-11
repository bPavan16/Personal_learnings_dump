a = input("Enter The number :  ")
print(f"The Multiplication Table of {a} is : ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) *i}")
except:
    print("Invalid input")

try:
    num = int(input("Enter a Number : "))
    arr = [6,3]
    print(a[num])
except ValueError:
    print("The Number Entered is not an Integer")
except IndexError:
    print("Not an Valid Index")


print("Some Lines Of Code and ")
print("End of Program")
