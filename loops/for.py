# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry", "strawberry"]
for fruit in fruits:
  print(fruit)


# Looping Through a String
name = "Akash Mallik"
for x in name:
    print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry", "strawberry"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

print("\n")

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry", "strawberry"]
for fruit in fruits:
    if fruit == "cherry":
        continue
    print(fruit)


# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function.
for x in range(6):
    print(x)

for x in range(10,100,5):
    print(x)

# Else in For Loop
for x in range(5):
    print(x)
else:
    print("Exection finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for j in fruits:
        print(i + j)