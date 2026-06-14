# Making making multiple class inheritence 

class Employee():
    company = "TCS" 
    name = "Ali"
    salary = 10000
    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")

class Coder():
    language = "java"
    def printLanguage(self):
        print(f"out of all the languages the main language of the company is : {self.language}")

# Now making multiple class inheritence here 

class Programmer(Employee , Coder):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The name of employee is {self.name} and he is good in {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()