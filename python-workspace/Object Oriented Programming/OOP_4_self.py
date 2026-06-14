# Employee is a Class
class Employee:
    language = "Python" # This is the class attribute
    salary = 10000 # This is the class attribute

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # def greet(self):                    #here in place of this self we also use one method named @staticmethod
    #     print("HEY Good Morning")


    @staticmethod
    def greet():
        print("HEY Good Morning")

# zarak is an object
zarak = Employee()
zarak.language = "C++" # This is the object/instance attribute
zarak.greet()
zarak.getInfo() # call by this method also
Employee.getInfo(zarak) # call by this one also
