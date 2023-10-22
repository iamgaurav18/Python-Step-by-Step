class shape:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b

class circle(shape):
    def __init__(self, a) -> None:
        self.a=a
        super().__init__(a,a)
    def area(self):                          # overriding is when method of child class overrides the method of same name of parent class
        return 3.14*super().area()
    
s=shape(2,4)
print(s.area())
c=circle(5)
print(c.area())