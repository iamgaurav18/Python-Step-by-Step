x=5  #Global variable: that can be accessed from anywhere in the program
y=100
print(f"Global value of x: {x}")  
print(f"Global value of y: {y}")

def hello():
    global y
    y=10
    x=10                #Local variable that can be used within the function and it gets destroyed as soon as the functions end
    print(f"Local value of x: {x}")
    print(f"Local value of y: {y} after using global keyword")

hello()

print(f"Global value of x: {x}")
print(f"Global value of y: {y}")
