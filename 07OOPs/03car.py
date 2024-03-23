
# SAMPLE CODE
class Car:
    no_of_tyres = 4
    no_of_stearing = 1
    no_of_gears = 5

    def __init__(self, name, color, fuel_type):
        self.name = name
        self.color = color
        self.fuel_type = fuel_type

    def get_details(self):
        return f"Name: {self.name}, Color: {self.color}, Fuel Type: {self.fuel_type}, Tyres: {self.no_of_tyres}, Stearing: {self.no_of_stearing}, Gears: {self.no_of_gears}"
    
car1 = Car("Audi", "Black", "Petrol")
car2 = Car("BMW", "White", "Diesel")
car3 = Car("Mercedes", "Red", "Petrol")

print(car1.get_details())
print(car2.get_details())
print(car3.get_details())
