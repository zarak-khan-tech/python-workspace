# Employee is a Class
class Employee:
    language = "Python" # This is the class attribute
    salary = 10000 # This is the class attribute

    def __init__(self, name, salary, language): # this is a constructor method which will run as soon as object is created
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # def greet(self):                    #here in place of this self we also use one method named @staticmethod
    #     print("HEY Good Morning")

    @staticmethod
    def greet():
        print("HEY Good Morning")

# zarak is an object
zarak = Employee("Zarak khan", 200000, "Rust")
zarak.greet()
print(zarak.name, zarak.salary, zarak.language)
