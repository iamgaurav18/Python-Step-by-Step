#while loop
a=0
while(a<5):
    print(a,end=" ")
    a+=1
else:
    print("We are out of while loop")

# how to emulate do while loop

while True:
    a=int(input("print a number greater than 10 : "))
    if(a>10):
        break
    else:
        continue