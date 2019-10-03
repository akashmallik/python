# Python Collections (Arrays)
"""There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members."""

# List

fruits = ["Apple", "Banana" , "Strawberry", "blackberry"]
print(type(fruits))
print(fruits)
print(fruits[0])

print(fruits[-1]) # Last item
print(fruits[-2]) # Second last item

# Range of Indexes
print(fruits[0:2])
print(fruits[-3:-2])
# Change Item Value
fruits[0] = "Cherry"
print(fruits) 

print('Loop')
# Loop Through a List
for fruit in fruits:
    print(fruit)

# Check if Item Exists
if 'Cherry' in fruits:
    print("found...")
else:
    print("Not found!")

# List Length
print(len(fruits))

# Add Items
""" To add an item to the end of the list, use the append() method:
 To add an item at the specified index, use the insert() method """


fruits.append("Cherry")
print(fruits)

fruits.insert(0, "Jackfruits")
print(fruits)

# Remove Item
# The pop() method removes the specified index, (or the last item if index is not specified)
fruits.remove("Cherry")
print("Remove Cherry" + str(fruits))
fruits.pop(1)
print(fruits)
fruits.pop()
print(fruits)

del fruits[0]  # specific index
print(fruits)
del fruits # Delete full list

try:
    print(fruits)
except NameError:
    print("No fruits found")


# Copy a List

List_01 = ["Akash", "Tuhin", "Arif","Golzar"]
List_02 = ["Ajoy", "Lima", "Titu"]
List_03 = []
print(List_03)
List_03 = List_01.copy()
print(List_03)
# Another way

List_04 = list(List_03)
print(List_04)

List_04 = List_01 + List_02
print(List_04)

# Append List
List_06 = ["test"]
for item in List_02:
    List_06.append(item)
print(List_06)

# extend
List_06.extend(List_01)
print(List_06)


#sort 
List_06.sort()
print(List_06)
List_06.reverse()
print(List_06)

# clear
List_06.clear()
print(List_06)
