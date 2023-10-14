def greet(fx):
    def rfx(*args,**kwargs):
        print("Oh hi, Good morning")
        fx(*args,**kwargs)
        print("Have a nice day")
    return rfx

@greet                       # this is a decorater which basically modifies an existing function. it would take a funxtion as an argument do some changes in it and return a function.
def hello():
    print("How are you ?")

hello()

# you can also use greet(hello)() to do the same, but in this you dont have to write greet before function definition

@greet
def name(name):
    print(f"My name is {name}")

name("Gaurav")