class Employee:
    a = 1
    def __init__(self):
        print("Constructor of Employee")

class Programmer(Employee):
    b = 2
    def __init__(self):
        print("Constructor of Programmer")

class Manager(Programmer):
    c = 3
    def __init__(self):
        super().__init__() # It will call his parent also and its parent class is programmer
        print("Constructor of Manager")

# o = Employee()
# print(o.a) 

# o = Programmer()
# print(o.a , o.b) 

o = Manager()
print(o.a , o.b , o.c)