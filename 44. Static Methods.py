class math:
    def __init__(self,n) -> None:
        self.num=n
    def result(self):
        print(self.num)

    @staticmethod
    def multi(a,b):       #these methods can be called without using object of the class
        print(a*b)

a=math(6)
a.result()

a.multi(2,3)             # you can either use an object or name of the class to access static method
math.multi(10,6)