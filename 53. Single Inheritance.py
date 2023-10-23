class people:
    def __init__(self,name,gender) -> None:
        self.name=name
        self.gender=gender
    def feature(self):
        if(self.gender=="M"):
            print("Men have more patience")
        else:
            print("Woemen have more emapathy and emotions")

class student(people):
    def __init__(self, name, gender,std) -> None:
        super().__init__(name, gender)
        self.std=std
    
    def feature(self):
        if(self.gender=="M"):
            print(f"{self.name} will opt for Defence services")
        else:
            print(f"{self.name} will opt for medical services")

a=student("Guarav","M",12)
b=people("Anjali","F")
a.feature()
b.feature()

#this is called single inheritance where only one class inherits from parent class