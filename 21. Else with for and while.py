#else can be used with for and while loop also
#it will be executed only when loop will complete its all executions
#if loop gets break in between then else wont be executed

for i in range(5):
    print(f"Iteration number{i+1}")
else:
    print("Loop completed successfully")

for i in range(5):
    print(f"Iteration number{i+1}")
    if(i==3):
        break
else:
    print("Loop completed successfully")

i=1
while(i<5):
    print(i)
    i=i+1
    if(i==3):
        break
else:
    print("Loop completed successfully")