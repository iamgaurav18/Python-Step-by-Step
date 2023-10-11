def appl(fx,value):   # here we can pass lambda function as an arguments
    return 10+fx(value)

sum=lambda a,b: a+b     # lambda functions with two parameters
square=lambda x: x*x    # Lambda function

print(sum(5,8))
print(square(3))
print(appl(square,5))