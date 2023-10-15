class parent:
    def __init__(self,name,surname) -> None:
        self.name=name
        self.surname=surname
    
    def sname(self):
        print(f"The full of name is {self.name} {self.surname}")

class child(parent):    #this will create a child class of class parent
    def age(self):
        print("Default age is 25")

a=parent("Gaurav","Vishwakarma")

a.sname()
b=child("Major","Gaurav")     # as you can see by using inheritance we can use methods, properties and even constructors of parent class
b.sname()
b.age()