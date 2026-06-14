class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand 
        self.speed = speed

    def show_info(self):
        print(f"The Brand of the vehicle is {self.brand} and its speed is {self.speed}")

class Car(Vehicle):

    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def show_fuel(self):
        print(f"Fuel Type : {self.fuel_type}")

c = Car("BMW", 220, "Patrol")

c.show_info()
c.show_fuel()