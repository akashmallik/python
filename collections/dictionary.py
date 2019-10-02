# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

info = {
    "name": "Akash Mallik",
    "mobile": "+88 01777-334628",
    "email": "toakashmallik@gmail.com",
    "address": "Dhaka, Bangladesh"
}
# Accessing Items
print(info)
print(info["name"])
print(info.get("name"))

# Change Values
info["mobile"] = "+88 01916-659114"
print(info)

# Loop Through a Dictionary
# return key
for x in info:
    print(x)
# return value
for x in info:
    print(info[x])
for x in info.values():
    print(x)
# Loop through both keys and values, by using the items() function:
for x,y in info.items():
    print(x + ": " + y)
for x in info:
    print(x + ": " + info[x])


# Check if Key Exists
if "mobile" in info:
    print('Mobile found')
else:
    print('Mobile not found')

# Dictionary Length
print("Dictionary length is: " + str(len(info)))

# Adding Items
info["sex"] = "Male"
print(info)

# Removing Items
info.pop("sex")
print(info)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
info.popitem()
print(info)

del info["name"]
print(info)

del info
try:
    print(info)
except:
    print("No dictionay found")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
thisdict.clear()
print(thisdict)

# The dict() Constructor
test = dict(name="akash", email= "toakashmallik@gmail.com")
print(test)
print(type(test))





# Nested Dictionaries
babys = {
    "baby_01" : {
        "name" : "Hablu",
        "sex" : "male"
    },
    "baby_02" : {
        "name" : "Dablu",
        "sex" : "male"
    },
    "baby_03" : {
        "name" : "Tuktuki",
        "sex" : "Female"
    },
}

print(babys)




