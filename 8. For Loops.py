# For loops
a="gaurav"
for i in a:
    print(i,end=" ") #print the character within the double qoute at the end of print staement

for i in range(5):
    print(i)

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(1,8):        # it will start from 1 to 7 
    print(i)

for i in range(0,10,2):     # it will start from 0 to 9 with skipping 1 value 
    print(i)