from typing import Any


class Employee:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def __str__(self) -> str:                         # this is used when we want to print out an object
        return (f"This is an object for {self.name}")
    def __repr__(self) -> str:
        return (f"Employee('{self.name}',{self.age})") # this is used when you want to get string representation of an object that can recreate an object
    def __call__(self) -> Any:
        return "Hi, I am good"
    
e=Employee("Pandey",24)
print(e)    # by default it will show the result of __str__ if both repr and str are present 
print(str(e))
print(repr(e))
print(e())