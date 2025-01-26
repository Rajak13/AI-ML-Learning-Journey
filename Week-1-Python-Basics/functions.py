# Functions in python are block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.
# Function definition begins with "def".

# Something to note is that all functions in python have a return value.
# If you do not specify a return value, the function will return None.

# Three types of functions in python
# 1. Built-in functions
# 2. User-defined functions
# 3. Anonymous functions

# Example of built-in functions
# Example
x = 10
print(abs(x))

#Here, print is a built-in function in python.
# Output: 10

# Example of user-defined functions
# Example
def add_numbers(a, b):
    return a + b

# Now we can call this user-defined function by passing arguments
add_numbers(3, 4)

# Output: 7

# Example of anonymous functions
# Example
add = lambda a, b: a + b
add(3, 4)

# Here, add is an anonymous function. They are called ananymous function as they are not declared with the standard def keyword.

# Output: 7