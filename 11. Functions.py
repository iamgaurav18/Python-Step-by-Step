def whoisgreater(a=1,b=10):        #def is used to define a function in python
    if(a>b):
        print(a,"is greater than",b)
    elif(a==b):
        print(a,"is equal to",b)
    else:
        print(a,"is smaller than",b)

whoisgreater(89,323)
whoisgreater(4,4)

whoisgreater()   #this will take the default values mentioned in the function

whoisgreater(6) # this will assign value to inly a 

whoisgreater(b=6,a=38) # this way the order doesn't matter and values will get assigned to correct variable

#if you don't know the exact number of arguments you can use *variable name, this will take all inputs in form of a tuple and you can use that tuple in the function

#Similarly we can use **variable in function argument list to take dictionary as an input

#here we are  printing the result you can also return the value using return keyword