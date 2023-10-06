#OS module is python helps you to perform many taks through the code like creating multiple folders and file, accessing those files and many more

import os

if (not os.path.exists("Python")):  #this will check python folder already exists or not
    os.mkdir("Python") #this will create a folder name python in current directory

for i in range(10):
    if (not os.path.exists(f"Python/Topic{i+1}")):
        os.mkdir(f"Python/Topic{i+1}") #this will create 10 folders at once with name Topic 1, Topic 2...
    else:
        os.rename(f"Python/Topic{i+1}",f"Python/Day {i+1}") # this will rename the existing folder to a new name

folders=os.listdir("Python")
print(os.listdir("Python"))  #this will return the "list" of folders inside the specified path
for f in folders:
    print(f)

print(os.getcwd())  # this will return the name of current working directory

os.chdir("/Python")  #this will change the working directory to specified path

print(os.getcwd())  