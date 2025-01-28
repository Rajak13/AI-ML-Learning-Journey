# Practice Questions

# 1. Variables and Data Types
# a. Declare a variable to store your name and print it.

name = "Rajak"
print(name)

# b. What is the output of the following code?
#    x = 5
#    y = "5"
#    print(x + y)

# The output would be an error since integer and string values are not compatible for addition.

# c. Convert the integer 10 to a string and concatenate it with the string " apples".

x = 10
y = "apples"
print(str(x) + " " + y)

# Output would be 10 opples.

# 2. Functions
# a. Write a function that takes two numbers as arguments and returns their product.

def product(a,b):
    return a*b
print(product(4,2))


# b. What is the difference between a user-defined function and an anonymous function?

#Answer: User-defined functions are declared using def keyword and have a name wherease an anonymous function is declared using lambda keyword and doesn't have a name.

# c. Write an anonymous function to find the square of a number.

square = lambda x: x*x
print(square(5))

# Output would be 25.

# 3. Data Structures
# a. Create a list of your favorite fruits and print the second item.

fruits = ["pomegrante", "grapes", "orange", "kiwi"]

print(fruits[1])

# Output would be grapes.

# b. What is the difference between a list and a tuple?

#Ans: A list is mutatble whereas a tuple is immutable. This means list can be changed after creation however tuple cannot be changed after creation.

# c. Create a dictionary to store information about a book (title, author, year) and print the author's name.

book ={"title": "Spring Snow", "author": "Yukio Mishima", "year": 1969}
print(book["author"])

# Output would be Yukio Mishima.

# 4. Loops
# a. Write a for loop to print numbers from 1 to 10.

for i in range(10):
    print(i+1)
    
# Output would be 1,2,3,4,5,6,7,8,9,10.

# b. Write a while loop to print the first 5 even numbers.

count = 10
i = 2

while (i <= count):
    print(i)  # Print the even number.
    i += 2  # Increase the number by 2.

# Output would be 2,4,6,8,10.

# c. Write a nested loop to print a 3x3 grid of asterisks (*).

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # Add a newline after each row to ensure proper grid formatting

# 5. Conditionals
# a. Write an if statement to check if a number is positive, negative, or zero.

num = 8

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")
    
# Output would be Positive.

# b. What is the output of the following code?
#    x = 10
#    if x > 5:
#        print("Greater than 5")
#    elif x == 5:
#        print("Equal to 5")
#    else:
#        print("Less than 5")

# The output would be Greater than 5.

# c. Write a conditional expression to find the minimum of two numbers.

x = 4
y= 7

min_num = x if x < y else y
print(min_num)

# Output would be 4.

# 6. Strings
#a. Reverse a string in Python

# Given string
a_string = "Carrot"

# Using slicing to reverse the string
reverse_string = a_string[::-1]

# Print the reversed string
print(reverse_string)

# Output: torraC

# b. How do you concatenate two strings in Python?

a = "Hello"
b ="World!"

print(a + " " + b)

# Output: Hello World!

# c. Write a program to count the number of vowels in a string.

string = "Hello World"
vowels = "aeiouAEIOU"  # Include uppercase vowels

count = 0

for char in string:
    if char in vowels:
        count += 1

print(count)

# Output: 3
