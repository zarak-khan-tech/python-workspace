# Making single class inheritence 

class Employee():
    company = "TCS" 
    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")

# Now making single class inheritence from the parent class 

class Programmer(Employee):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The name of employee is {self.name} and he is good in {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company)