""" Python has two primitive loop commands:
    while loops
    for loops """


# The while Loop
i = 1
while i < 5:
    print(i)
    i += 1

print('\n')
# Break
# With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

# continue
# With the continue statement we can stop the current iteration, and continue with the next
x = 20
while x < 25:
    print(x)
    x += 1
    if x == 22:
        continue

# The else Statement
x = 1
while x < 3:
    print(x)
    x += 1
else:
    print("No more data found...")


# Python For Loops
