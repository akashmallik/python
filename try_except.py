# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    print(x)
except TypeError:
    print("TypeError occered")
except NameError:
    print("NameError occered")
except:
    print("Something else went wrong")

print("\n")

try:
    print("Akash Mallik")
except TypeError:
    print("TypeError occered")
except NameError:
    print("NameError occered")
except:
    print("Something else went wrong")
else:
    print("no error occered")
finally:
  print("The 'try except' is finished")


try:
    f = open("info.txt")
    f.write("Recursion is a common mathematical and programming concept.It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result")
except:
    print("Something went wrong")
finally:
    f.close()
