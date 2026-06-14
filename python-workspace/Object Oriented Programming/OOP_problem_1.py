class programmer:
    company = "Open AI"

    def __init__(self, name, salary, pincode, city):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        self.city = city


p1 = programmer("Zarak khan", "2000$", 68283, "San Francisco"  )
print(p1.name, p1.salary, p1.pincode, p1.city, p1.company)

p2 = programmer("Nimra khan", "900$", 68288, "Chicago"  )
print(p2.name, p2.salary, p2.pincode, p2.city, p2.company)