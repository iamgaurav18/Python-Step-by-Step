class stu:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def show(self):
        print(f"{self.name} is a student of {self.age}")
    @classmethod
    def altcons(cls,string):                                   #this will now act as a constructor which will assign values to a object of class and return it
        return cls(string.split("-")[0],string.split("-")[1])

a=stu("Gaurav",24)
a.show()
b=stu.altcons("Suraj-25")
b.show()