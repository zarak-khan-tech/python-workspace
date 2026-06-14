# Easy example of Multi Level inheritence 

class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) #here it will print only class employee attribute

o = Programmer()
print(o.a , o.b) # here it will print class employee + programmer attributes

o = Manager()
print(o.a , o.b , o.c) # here it will print all 3 classes attributes 