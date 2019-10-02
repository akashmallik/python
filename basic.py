print('Hello World!')

# Indentation
if 5>2:
    print('five is greater then two')


# Variables
""" Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)"""
x = 5
y = 'text'
z = 5.5

A, B, C = "Apple", "Banana", "Cherry"
M = N = O = 'text'

# Global Variables
status = "awesome"
def myfunc():
    print("python is " + status)
myfunc()

# The global Keyword
def myfunc2():
    global myvari
    myvari = 'x'
myfunc2()
print("My variable is " + myvari)


# Comments
# this is a comment example
print('Python comment') # this is another python comment example

""" Multiline comments """
# As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.
multi_comment = """Mulitiline comments"""
print(multi_comment)


"""Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview"""

x = 5 #int
print(type(x))
x = "Hello World" #str
print(type(x))
x = .5 #float
x = True #bool
print(type(x))

print(type(x))
x = ["apple", "banana", "Cherry"] # list
print(type(x))
x = ("apple", "banana", "Cherry") # touple
print(type(x))
x = {"apple", "banana", "Cherry"} # set
print(type(x))
x = {"name": "Akash Mallik", "age": 25 } # dict
print(type(x))
x = frozenset({"apple", "banana", "Cherry"}) # frozenset
print(type(x))

print(type(x))
x = 1j #complex
x = b"Hello" # bytes
print(type(x))
x = bytearray(5) # bytearray
print(type(x))
x = memoryview(bytes(5)) # memoryview
print(type(x))


# python numbers
x = 1
y = 1.5
z = 1j
z = -87.7e100
print(z)

covert = complex(x)
print(covert)

# Random number
import random
x = random.randrange(1, 100)
print('Print random number')
print(x)


#Type Casting
print('Type casting example')
x = int(1)
print(x)
x = int(2.5)
print(x)
x = int("3")
print(x)
x = float(1)
print(x)
x = float(2.5)
print(x)
x = float("3.5")
print(x)
x = str(1)
print(x)
x = str(2.5)
print(x)
x = str("3.5")
print(x)
