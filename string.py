# python string
print('Akash Mallik')
print("Akash Mallik")

# Multiline string
print("""
    Name: Akash Mallik
    Age: 25
    """)

# Strings are Arrays
x = "Hello World"
print(x[0])

# Slicing
print(x[0:2])
# Negative Indexing
print(x[-3:])
# String Length
print(len(x))

# String Methods| lower | upper | replace
# The strip() method removes any whitespace from the beginning or the end

name = "  Akash Mallik  "
print(name.strip())
print(name.lower())
print(name.upper())
print(name.replace("A", "B"))

# Check String
text = "Hi I'm Akash Mallik. I am a student of Green university of Bangladesh."
_isExist = "Akash" in text
_isNotExist = "Akash" not in text
print(_isExist)
print(_isNotExist)

# String Concatenation
first_name = "Akash"
last_name = "Mallik"
surname = "Arnob"

full_name = first_name + " " + last_name + " " + surname
print(full_name)

# String Format
name = "Akash Mallik"
age = 25
height = 5.45
info = "Hi, I'm {}. I'm {} age & height {} inch."
print(info.format(name,age,height))










