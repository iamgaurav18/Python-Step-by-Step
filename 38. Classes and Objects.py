class Person:                       # class keyword is used to create a class in python
    name="Gaurav"                   # these variables are called data members of the class
    occupation="Software Engineer"
    age=24
    def display(self):              # these kind of functions are called member functions of a class
        print(f"Hi, I am {self.name}, I am a {self.age} year old {self.occupation}") # self is basically used to refer the current instance of the class. for example self will point to object a here.

a=Person()                          # this is how we create an object of a class
a.display()

b=Person()
b.name="Suraj"
b.occupation="Engineer"
b.age=25

b.display()                         # you will see that whichever object calls the method, self will take that object as a refernce
a.display()