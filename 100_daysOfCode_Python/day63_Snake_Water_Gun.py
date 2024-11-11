import random


def compare(comp, user):
    if (comp == user):
        return 0
    if (comp == 1 and user == 0):
        return -1
    if (comp == 1 and user == 2):
        return -1
    if (comp == 2 and user == 1):
        return -1

    return 1


comp = (random.randint(0, 2))

user = int(input("Enter 1 for Snake \nEnter 0 for Water \nEnter 2 for Gun\nYOUR INPUT IS : "))

print("\n\n")

print("The computer choose :")
if (comp == 0):
    print(" Water \n")

elif (comp == 1):
    print(" SNAKE \n")

elif (comp == 1):
    print(" GUN \n")

print("The Player Choose :")
if (user == 0):
    print(" Water \n")

elif (user == 1):
    print(" SNAKE \n")

elif (user == 2):
    print(" GUN \n")


score = compare(comp, user)
if (score == 0):
    print(" DRAW ")

elif (score == -1):
    print(" YOU LOOSE ")

elif (score == 1):
    print(" YOU WIN")

print("\n\n")
