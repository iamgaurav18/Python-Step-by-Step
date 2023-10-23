class vector:
    def __init__(self,x,y,z) -> None:
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self) -> str:
        return (f"{self.x}i+{self.y}j+{self.z}k")
    
    def __add__(self,a):      # this will overload the addition operator for this vector class
        return vector((self.x+a.x),(self.y+a.y),(self.z+a.z))
    
a=vector(1,2,3)
b=vector(4,5,6)
c=a+b
print(str(c))
print(type(a+b))              # it will result in a object of vector class
#similarly you can overloading various operator just go through offical document of python