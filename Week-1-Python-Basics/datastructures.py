# Data Structures in Python

# 1. Lists
# Lists are ordered, mutable collections of items.
# Example:
fruits = ["apple", "banana", "cherry"]
print(fruits)
# Output: ['apple', 'banana', 'cherry']

# Lists can contain items of different data types.
mixed_list = [1, "apple", 3.14]
print(mixed_list)
# Output: [1, 'apple', 3.14]

# Lists are mutable, meaning you can change their content.
fruits[1] = "blueberry"
print(fruits)
# Output: ['apple', 'blueberry', 'cherry']

# You can add items to a list using append() or extend() methods.
fruits.append("date")
print(fruits)
# Output: ['apple', 'blueberry', 'cherry', 'date']

# You can remove items from a list using remove() or pop() methods.
fruits.remove("blueberry")
print(fruits)
# Output: ['apple', 'cherry', 'date']

# 2. Tuples
# Tuples are ordered, immutable collections of items.
# Example:
coordinates = (10, 20)
print(coordinates)
# Output: (10, 20)

# 3. Sets
# Sets are unordered collections of unique items.
# Example:
unique_numbers = {1, 2, 3, 4, 4, 5}
print(unique_numbers)
# Output: {1, 2, 3, 4, 5}

# 4. Dictionaries
# Dictionaries are unordered collections of key-value pairs.
# Example:
person = {"name": "John", "age": 30}
print(person)
# Output: {'name': 'John', 'age': 30}

# You can access dictionary values by their keys.
print(person["name"])
# Output: John

# You can add or change dictionary entries.
person["age"] = 31
person["city"] = "New York"
print(person)
# Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# You can remove dictionary entries using the pop() method.
person.pop("age")
print(person)
# Output: {'name': 'John', 'city': 'New York'}

# You can iterate over dictionaries.
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: John
# city: New York

# 5. Strings
# Strings are ordered, immutable sequences of characters.
# Example:
greeting = "Hello, World!"
print(greeting)
# Output: Hello, World!
