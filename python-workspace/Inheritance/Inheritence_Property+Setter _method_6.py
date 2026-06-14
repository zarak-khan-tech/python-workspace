class Employee:
    a = 1 

    @classmethod  # this method will show the class attributes instead of intance attributes 
    def show(cls):
        print(f"The class attribute value is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Zarak Khan"
print(e.fname , e.lname)

e.show()