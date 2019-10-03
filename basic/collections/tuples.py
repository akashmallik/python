# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

testTuple = ("Akash", "Titu", "Arif","Ajoy","Lima")
print(type(testTuple))

# Single Tuple
sigleTuple = ("Akash",)
print(type(sigleTuple))
# String
sigleTuple = ("Akash")
print(type(sigleTuple))

# Access Tuple Items
print(testTuple[2])
print(testTuple[-1]) # Negative Indexing

# Range of Indexes
print(testTuple[1:4])
print(testTuple[-4:-2])

# Change Tuple Values
""" First convert to list then assign to the tuple """
x = ("Apple", "Banana", "Strawberry")
y = list(x)
y[0] = "Cherry"
x = tuple(y)
print(x)

# Loop Through a Tuple
for item in x:
    print(item)

# Check if Item Exists
if "Cherry" in x:
    print('Found')
else:
    print('Not found')

# Tuple Length
print(len(x))

# Add Items
# Tuples are unchangeable

# Remove Items
# You cannot remove items in a tuple

# Delete tuple
del x
try:
    print(x)
except:
    print('Not Found!')


# Join Two Tuples
x1 = ("Akash",)
x2 = ("Lima",)
x3 = x1 + x2
print(x3)

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)