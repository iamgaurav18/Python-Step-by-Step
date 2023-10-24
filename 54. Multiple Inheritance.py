class person:
    def __init__(self,name,gender,age) -> None:
        self.gender=gender
        self.age=age
        self.name=name
    def show(self):
        print(f"{self.name} is a {self.gender} of age {self.age} years")
class Emp:
    def __init__(self,job) -> None:
        self.job=job
    def show(self):
        print(f"{self.job} is a job of above person")
class teacher(person,Emp):           # 
    def __init__(self, name, gender, age,job) -> None:
        person.__init__(self,name, gender, age)        # this is how we call constructors for multiple classes
        Emp.__init__(self,job)
        self.subject="maths"
    def show(self):
        print(f"{self.name} is a {self.job} of subject {self.subject}")

c=teacher("Gaurav","Male","24","Teacher")
c.show()
print(teacher.mro())   # this will print Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.