
class Student:
    univ = "USD"
    department = 'CSE'

    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob 

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, DOB: {self.dob}, University: {self.univ}, Department: {self.department}"
    
s1 = Student("Chenchu", 26, "31-07-1998")
s2 = Student("Rajia", 28, "28-02-1996")

print(s1.get_details())
print(s2.get_details())

