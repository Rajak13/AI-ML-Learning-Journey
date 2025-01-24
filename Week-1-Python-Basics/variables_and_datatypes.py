# Variables = Variable is a reusable container for storing a value.
# Variables are used to store data, and data can be of any type. It behaves as if it were the value it contains.
# Variable behaves as if it were the value it contains


# Variable Declaration
age = 21 #Assigning an integer to a variable

print(age)

# Output: 21

#Seperating arguements
print("You are " + str(age) + " years old") #Here str is used to convert int to string.This is known as type casting.

# Output: You are 21 years old

#The most common way to print with different datatypes is provided below:
print(f"You are {age} years old") #This is known as f-string or formatted string.

# Output: You are 21 years old

# Data types
# Data types are defined as what type of data we are inserting. Following are the data types in Python:

# 1. Integer

# Integer is a whole number, positive or negative, without decimals, of unlimited length.

# Example
x = 1
y = 12
z = 123

print(x, y, z)

# Output: 1 12 123

# 2. Float

# Float is a number, positive or negative, containing one or more decimals.

# Example
x = 1.10
y = 12.345
z = 123.456789

print(x, y, z)

# Output: 1.1 12.345 123.456789

# 3. String

# String is a sequence of characters enclosed in single quotes (' ') or double quotes (" ").

# Example
x = "Hello"
y = "World"
z = "AI and ML"

print(x, y, z)

# Output: Hello World AI and ML

# 4. Boolean

# Boolean is a data type that can have only two values: True or False.

# Example
x = True
y = False

print(x, y)

# Output: True False

# 5. List

# List is a collection that is ordered and changeable. Allows duplicate members.

# Example
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry", "apple"]

print(x, y)

# Output: ['apple', 'banana', 'cherry'] ['apple', 'banana', 'cherry', 'apple']

# 6. Tuple

# Tuple is a collection that is ordered and unchangeable. Allows duplicate members.

# Example

x = ("apple", "banana", "cherry")
y = ("apple", "banana", "cherry", "apple")

print(x, y)

# Output: ('apple', 'banana', 'cherry') ('apple', 'banana', 'cherry', 'apple')