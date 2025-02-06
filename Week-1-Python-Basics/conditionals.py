
# Let's say we have a condition to meet. If we fulfill the condition, then output will be "true". If we don't fulfill the condition, then output will be "false".

# Example

if 12 > 7:
    print("True")
else:
    print("False")
    
# Output: True
#This is a simple example of a condition.

# In Python, we have the following conditional statements:

# if statement: An if statement is a programming conditional statement that, if proved true, performs a function or displays information.
# if...else statement: An if statement can be followed by an optional else statement, which executes when the condition is false.
# if...elif...else statement: An if statement can be followed by an optional elif statement and then by an optional else statement. The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions is TRUE. 
# if...else statement and then...else statement and then...else statement and so on. This is known as a nested if statement.

# Example

x = 10

if x > 5:
    print("x is greater than 5")
else:
    if x == 5:
        print("x is equal to 5")
    else:
        print("x is less than or equal to 5")
        
# Output: x is greater than 5

# In the above example, we have used a nested if statement. We can also use the elif statement to avoid nested if statements.

# Example

x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than or equal to 5")
    
# Output: x is greater than 5

# In the above example, we have used the elif statement to avoid nested if statements.

# We can also use the logical operators in the conditional statements.

# Example

x = 10
y = 5

if x > 5 and y == 5:
    print("Both conditions are true")
    
# Output: Both conditions are true


# Example

x = 10
y = 5

if x > 5 or y == 5:
    print("At least one condition is true")

# Output: At least one condition is true

# In the above example, we have used the logical operators in the conditional statements.

# Conditional Expressions

# Conditional expressions are also known as the ternary operator. It is a one-liner statement that evaluates an expression and returns a value based on the result of the expression.
# Syntax : X if condition else Y

# Example
num = 10
x = 5
y= 8

max_num = x if x > y else y
print(max_num)

# Output: 8

min_num = x if x < y else y
print(min_num)

# Output: 5