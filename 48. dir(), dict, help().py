x=[1,2,3]
print(dir(x))
# dir methods retunrs the list of attributes and methods including dunder methods that are avialable for that object
print(x.__add__)  #this is a dunder methods acting as an attribute here

class stu:
    def __init__(self) -> None:
        self.name="gaurav"
        self.age=24

a=stu()
print(a.__dict__)  #this will return all the attributes of an object in form of an dictionary

print(help(stu))  # help method help you in getting information about the object and attributes and methods related to it.