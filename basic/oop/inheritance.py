# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def get_name(self):
        print(self.firstname, self.lastname)

obj = Person("Akash", "Mallik")
obj.get_name()

# Create a Child Class
"""To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class"""
class Student(Person):
    pass
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

stud = Student("Md. Rana", "Islam")
stud.get_name()

class Employee(Person):
    def __init__(self, fname, lname, sallery):
        super().__init__(fname, lname)
        self.sallery = sallery # Add Properties


    def get_info(self):
        print(self.firstname, self.lastname , self.sallery)

emp = Employee("Akash", "Mallik", 25000)
emp.get_info()