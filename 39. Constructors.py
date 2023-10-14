class student:
     def __init__(self,name,age,stream) -> None:  # __init__ is used to create a constructor of a class, which returns none by default
          self.name=name                          # this is a parameterized constructor you can also make one without paramter
          self.age=age
          self.stream=stream
     def disp(self):
          print(f"Hi, {self.name} is a student of {self.age} year old, and studies in {self.stream}")

a=student("Gaurav",18,"Science")
a.disp()