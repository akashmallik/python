# Using for Loop
squares = []
for x in range(10):
    squares.append(x*x)

# List Comprehensive
squares = [x*x for x in range(10)]

# even squares using for loop
even_squares = []
for x in range(10):
    if x%2 == 0:
        even_squares.append(x*x)

# even squares using list comprehension
even_squares = [x*x for x in range(10) if x%2 == 0]

# preety code
even_squares = [x*x 
                for x in range(10)
                if x%2 == 0]

print(squares)
print(even_squares)