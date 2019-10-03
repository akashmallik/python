import cusmodule
import testmodule as test # Naming a Module
# build in module
import platform

from cusmodule import info as i

cusmodule.info("Akash")
print(cusmodule.person["address"])

print(test.person["name"])

print(platform.system())


# Using the dir() Function
""" There is a built-in function to list all the function names (or variable names) in a module. 
    The dir() function """
print(dir(platform.system()))


i("Titu Roy")


