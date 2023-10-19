class Emp:
    company="Accenture"   
    noofemployees=0               #class Variables 
    def __init__(self,name) -> None:
        self.name=name                   #instance Varirable that are attached to instance of the class
        self.hike=10
        Emp.noofemployees=Emp.noofemployees+1      # this will make changes in the class variables no matter how many objects are created
    def show(self):
        print(f"Employee {self.name} is working in {self.company} which has {self.noofemployees} and gives {self.hike} in every six months")

a=Emp("Gaurav")
a.show()
#Emp.show(a) this will also work the same as a.show()
a.company="Delloite"
a.show()        #this will show the value of the instance variable company i.e Delloite and it wont affect class variable
b=Emp("Suraj")
b.show()        # this will show the value of the class variable
# to change class variable we can use
Emp.company="Microsoft"
b.show()