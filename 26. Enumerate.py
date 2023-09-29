#enumerate is basically used to loop through the lists,tuple,strings while returning you the pair of values of index and value in form of a tuple

l=[1,56,223,22,7,3,9,12]

for v in enumerate(l):
    print(v[0],v[1])
    if(v[0]==4):
        print("Break")
        break

#this can also be written in the below way where we are just unpacking the values of tuple

for index,value in enumerate(l):
    print(index,value)
    if(index==4):
        print("Break")
        break

#you can also specify the index to start with. for ex if you want to start with 1 not 0

for index,value in enumerate(l,start=1):
    print(index,value)
    if(index==4):
        print("Break")
        break
