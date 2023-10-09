with open("dummy.txt","r") as f:
    print(type(f))
    f.seek(10)  #it will move the pointer to specified position in the file
    d=f.read(5)  # it will display next 5 characters from current position
    print(d)
    print(f.tell())  # this will  tell the corrent position in a file

with open("dummy.txt","w") as f:
    f.write("how are you ?")
    f.truncate(5)  #this will truncate the string after 5 characters from the start

with open("dummy.txt","r") as f:
    d=f.readline()
    print(d)