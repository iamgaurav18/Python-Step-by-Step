# this operator allows you to assign values to a variable within a expression
a=[1,2,3,4,5]
while(n:=len(a)>0):    # here we are assigning the value to n within a expression
    print(a.pop())

b=[]
while (bi:=int(input("Enter a positive number : ")))>=0:  # now this will run the loop till the time we enter any negative number
    b.append(bi)

print(b)