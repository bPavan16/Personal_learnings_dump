def fun():
    try:
        l=[1,5,6,7]
        i = int(input("Enter the index that you want to print : "))
        print(l[i])
        return 1
    except:
        print("Some Error Occoured")
        return 0
    finally:
        print("I am alsways Executed ")

a = fun()


# Even if the function Returns Than also it works the finally statementS 








        