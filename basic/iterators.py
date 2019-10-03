# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


name = "Akash"
iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Looping Through an Iterator
# The for loop actually creates an iterator object and executes the next() method for each loop.

for i in mytuple:
    print(i)
for i in name:
    print(i)

class CustomIterator:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        a = self.x
        self.x += 1
        return a

obj = CustomIterator()
create_iter = iter(obj)

print(next(create_iter))
print(next(create_iter))
print(next(create_iter))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

obj2 = MyNumbers()
my_iter = iter(obj2)

for i in my_iter:
    print(i)

    