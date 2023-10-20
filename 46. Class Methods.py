class Emp:
    company="Accenture"
    def __init__(self) -> None:
        self.name="Gaurav"
    
    def show(self):
        print(f"{self.name} is a employee of {self.company}")
    
    @classmethod                                   #by adding the class method decorrator a method will get bound to the class and not the object of the class. They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    def changecompany(cls,comp):
        cls.company=comp

a=Emp()

a.show()
a.changecompany("Microsoft")    # here it will change  the class variable which will effect all objects and methods
a.show()
print(Emp.company)