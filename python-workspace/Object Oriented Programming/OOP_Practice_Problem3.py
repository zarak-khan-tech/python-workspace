class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

s1 = Student("Zarak Khan", 90)
print(s1.name)
print(s1.marks)

s1.update_marks(100)
print(s1.marks)