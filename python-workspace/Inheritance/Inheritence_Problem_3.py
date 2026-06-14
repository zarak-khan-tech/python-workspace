class Employee:
    salary = 234
    increment = 20

    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.increment * (self.increment/100))
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100

e = Employee()
print(e.SalaryAfterIncrement)

e.SalaryAfterIncrement = 300
print(e.increment)
