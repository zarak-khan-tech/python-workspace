class Employee:
    a = 1 

    @classmethod  # this method will show the class attributes instead of intance attributes 
    def show(cls):
        print(f"The class attribute value is {cls.a}")

e = Employee()
e.a = 45
e.show()