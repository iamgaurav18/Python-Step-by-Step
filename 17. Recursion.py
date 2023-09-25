#recursion is way of defining a function in which it is calling itself
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
print(fibo(4))