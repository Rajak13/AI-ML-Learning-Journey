# Loops in python can be described as commands to execute actions effectively

# For loop
# In Python, for loop is used to iterate over the items of any sequence including the Python list, string, tuple etc.

#Example
for i in range(5):
    print(i)
    
# Output: 0 1 2 3 4

# While loop
# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

#Example
i = 0
while i < 5:
    print(i)
    i += 1
    
# Output: 0 1 2 3 4

# Nested loop
# A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop".

# Example
for i in range(3):
    for j in range(3):
        print(i, j)
        
# Output:
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# A nested loop might be difficult to understand for beginners as they are complex. But they are very useful when you want to perform a repetitive task.
# The following example can be used to show how to use nested loops.

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to be printed: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")
    print()
    
# Run this command to print a rectangle of your size with any symbol.
