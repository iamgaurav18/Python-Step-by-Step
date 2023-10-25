class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}")
class emp(person):
    def __init__(self, name, age, role) -> None:
        super().__init__(name, age)
        self.role=role
    def show(self):
        super().show()
        print(f"Role: {self.role}")
class teacher(emp):
    def __init__(self, name, age, role,subject) -> None:
        super().__init__(name, age, role)
        self.subject=subject
    def show(self):
        super().show()
        print(f"Subject: {self.subject}")

a=teacher("gaurav",24,"Teacher","Computer Science")
a.show()