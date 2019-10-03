"""To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exis"""

f = open("blank.txt", "a")
f.write("Hello world")
f.close

f = open("blank.txt", "rt")
print(f.read())

f = open("demo.txt", "w")
f.write("Hi! I'm Akash Mallik. I'm a python developer. I love coding.... <3")
f.close()

f = open("demo.txt", "rt")
print(f.read())