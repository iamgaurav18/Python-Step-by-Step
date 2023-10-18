# In python we don't have public private protected like other languages but still we can implement these
class student:
    def __init__(self) -> None:
        self.name="Gaurav"
        self.__age=24   #to make a variable priavte use double underscore 
    
    def _show(self):                #use single underscore to make protected. rememer single underscore is just a name convention and if we want we can access variables using _
        print(self.name)

class child(student):
    pass

a=student()
print(a.name)
#print(a.__age)   this will throw and error
print(a._student__age)        # to print a private variable we can use _classname__private-variable-name
# this is called Name Mangling

b=child()
b._show()  # here though the method is protected but still it can be accessed by the child class object