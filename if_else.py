a = 33
b = 44 
c = 33

# If
if a>b:
    print('a greater then b')

# Else
if a>b:
    print('a greater then b')
else:
    print('a less then b')

# Elif
if c>b:
    print("c greater then b")
elif c==b:
    print("c equal to b")
else:
    print("c is less then b")

# Short Hand If
if a>b: print('a greater then b')

# Short Hand If ... Else
print('a greater then b') if a>b else print('a less then b')

# logical operator
if a<b and b>c:
    print('AND Conditon Setisfied')

if a<b or c>b:
    print('OR Conditon Setisfied')

# Nested If

if a < b:
    if b > c:
        print("True")
    else:
        print("False")
