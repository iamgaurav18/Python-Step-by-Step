f=open("dummy.txt","r")
while True:
    l=f.readline() #this will read the file line by line and each time it will return a string
    if not l:
        break
    print(l)
f.close()

f=open("dummy2.txt","w")
line=["hello\n","World\n","!"]
f.writelines(line)  #this will write at once
f.close()

# or

f=open("dummy2.txt","w")
line=["hello","World","!"]
for a in line:
    f.write(a+"\n")   #this willl write one by one
f.close()