#Getters are the methods in python that are basically used to return the value of property if an object
#they are defined using @property decorator

class shownum:
    def __init__(self) -> None:
        self.num=10
    
    def show(self):
        print(f"Value to be shown is {self.num}")
    
    @property                     #this is how a getter is defined
    def tenx(self):
        return 10*self.num
    
    @tenx.setter                  #this is how you define a setter
    def tenx(self,value):
        self.num=value/10
    
a=shownum()
a.show()
print(a.tenx)           # a getter can be used like a property of an object rather than a method. although you can assign any values using getters, it will throw error
a.tenx=10000            # a setter is basically used to set the value of a property of an object
a.show()