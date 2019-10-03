# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a class & object
class MyInfo:
    name = "Akash Mallik"

obj = MyInfo()
print(obj.name)

# The __init__() Function
"""Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

x = Person("Akash", 25)
print(x.name + str(x.age))

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

class StudentInfo:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_student_info(self):
        print("Student Name: " + self.name + "\nStudent Id: " + str(self.id))

obj = StudentInfo("Akash Mallik", 163015044)
obj.get_student_info()

# The self Parameter
"""The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class"""

class Person:
    def __init__(this, name, age):
        this.name = name
        this.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name)

o1 = Person("Akash Mallik", 25)
o1.myfunc()

# Modify Object Properties
o1.age = 25
print(o1.age)

# Delete Object Properties
del o1.age
print(o1.age)


