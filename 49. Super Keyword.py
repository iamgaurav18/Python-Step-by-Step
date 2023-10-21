class stu:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def disp(self):
        print("this is super class")

class sub(stu):
    def __init__(self, name, age,course) -> None:
        super().__init__(name, age)             #this is how we can use the super keyword to call constructor of parent class
        self.course=course
        print(f"COnstructors od super class have been used")
    def disp(self):
        print("this is child class")
        super().disp()       # this super method will call the disp method of parent class

s=sub("gaurav",24,"CSE")
s.disp()