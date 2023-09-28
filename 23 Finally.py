#Finally is used when we want to execute a certain set of instruction no matter what condition arises
def Sum(a,b):
    try:
        print(f"{int(a)}+{int(b)}={int(a+b)}")
        return int(a+b)
    except Exception as e:
        return(type(e).__name__)
    finally:
        print("I will get executed everytime")  #this could be usefuul when we want to perform certain task even if the main task fails
    print("This will not get executed as after finally it will return the value")

x=Sum('g',4)
print(x)
