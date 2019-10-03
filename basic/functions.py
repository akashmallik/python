# A function is a block of code which only runs when it is called.

def my_function():
    print("Hello World!")

my_function()

# Passing Parameters
def my_function_2(name):
    print("Hi I'm " + name)

my_function_2("Akash Mallik")

# Default Parameter Value
def my_function_2(name, country="Bangladesh"):
    print("Hi I'm " + name + " from " + country)

my_function_2("Akash Mallik",)
my_function_2("Akash Mallik","canada")

# Passing a List as a Parameter
def list_function(fruits):
    for fruit in fruits:
        print(fruit)

fruits = ["Apple","Mango","Banana","Strawberry"]
list_function(fruits)

# Return Values
def return_value(x):
    return x*2

result = return_value(3)
print(result)

# Arbitrary Arguments
"""If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition."""

def arbitrary_fuction(*fruits):
    print("Last item is " + fruits[-1])
    for fruits in fruits:
        print(fruits)

arbitrary_fuction("Mango", "Banana", "Grips","Apple")

# Recursion
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
def try_recursion(x):
    if (x>0):
        result = x + try_recursion(x-1)
        print(result)
    else:
        result = 0
    return result

try_recursion(6)