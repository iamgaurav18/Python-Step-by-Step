#matchcase statement are only present in python 3.10 and above version

a=int(input("Enter a number : "))

match a:
    case 0:                                        #will check if a is equal to 0
        print("It is Zero")      
    case _ if(a%2==0):                             # _ means default case. this one will check if a is even or not
        print("It is an even number")
    case 100:                                      # check if is 100
        print("It is hundred")
    case _ if(a%2!=0):                             # again a default case which will check if it is an odd number
        print("It is an Odd number")
    case _:                                        # this is also a default cae which will run when previous cases doesn't match
        print("Asambhav")