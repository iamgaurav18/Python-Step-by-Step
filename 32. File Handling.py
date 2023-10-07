f=open("dummy.txt","r")  # this will open the file in reading mode. if you open the file in "w" write mode you will not be able to read it
# by default if you do not give the mode it will open in reading mode
# if a file doesn't exist, then if you want to write in that file then it will first cerate the file and then write

print(f) # this will not priint the content of the file

c=f.read()
print(c)  # this will print the content of the file

f.close()  # this will close the file

f=open("dummy.txt","a")  # this will open the file in append mode and add the new content in the existing file without clearing the exixsting content 

# x mode creates a file if it doesn't exist and throws an error if it does exist

# rt mode open the file in reading mode as text file
# rb mode open file in binary mode

f.close()
f=open("dummy.txt","w")
f.write("Hellow world")