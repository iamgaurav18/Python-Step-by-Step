# we can raise custom error in our program
a=input("enter a number :")
print(type(a))
if(type(a)=="<class 'str'>"):
    raise ValueError("Input is not a number, it is a string")
elif(a<0):
    raise ValueError("It is a negative number")