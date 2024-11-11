i = 0
while (i <= 10):
    print(i)
    i = i+1

print("Done with the loop")


num = int(input("enter a number to be reversed  :"))
rev = 0
while (num != 0):
    rev = rev*10+num % 10
    num = num//10

print(rev)

i = int(input("Enter the number: "))
while (i <= 38):
    i = int(input("Enter the number: "))
    print(i)


print("Done with the loop")


count = 5
while (count > 0):
    print(count)
    count = count-1
else:
    print("Now i am inside the body of else ")

# do{
#     loop body:

# }while(condition);
