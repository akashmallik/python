x = 5
y = 6

if(x > y):
    print("x is greater then y")
else:
    print("x is lower then y")

print(bool(x))
x = ''
print(bool(''))
print(bool(()))
print(bool({}))
print(bool([]))
print(bool(None))
print(bool(False))

class MyClass():
    def __len__(self):
        return 0

myobj = MyClass()
print(bool(myobj))

x = "text"
print(isinstance(x, str))