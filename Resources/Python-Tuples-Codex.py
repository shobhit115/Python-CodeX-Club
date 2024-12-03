'''
  ______            __             _          ____        __  __              
 /_  __/_  ______  / /__  _____   (_)___     / __ \__  __/ /_/ /_  ____  ____ 
  / / / / / / __ \/ / _ \/ ___/  / / __ \   / /_/ / / / / __/ __ \/ __ \/ __ |
 / / / /_/ / /_/ / /  __(__  )  / / / / /  / ____/ /_/ / /_/ / / / /_/ / / / /
/_/  \__,_/ .___/_/\___/____/  /_/_/ /_/  /_/    \__, /\__/_/ /_/\____/_/ /_/ 
         /_/                                    /____/                        
Notes prepared by Codex Club, Quantum University – "Code, Collaborate, Create – Building a Better Tomorrow, One Line of Code at a Time."
'''

'''
Python Tuple is a collection of objects separated by commas. A tuple is similar to a Python list in terms of indexing, nested objects, and 
repetition but the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.
'''

### In case of list, we use square brackets []. Here we use round brackets ()

# t = (10, 20, 30)
# print(t)
# print(type(t))

### tuples can be created without parentheses (comma-separated values).
# point = 1, 2, 3  # Tuple creation without parentheses
# print(point)  # Output: (1, 2, 3)

### Accessing elements in a tuple is done using indexing (like lists).
# key = ("Doe", "John")
# lastname = key[0]
# print(lastname)  # Output: 'Doe'

### A single-element tuple requires a trailing comma; otherwise, it is treated as a value in parentheses.
# not_a_tuple = (1)  # Treated as an integer
# singleton = (1,)   # Single-element tuple
# print(singleton)   # Output: (1,)

### An empty tuple is created using parentheses.
# empty = ()
# print(empty)  # Output: ()

'''
Unlike Python lists, tuples are immutable. Some Characteristics of Tuples in Python.

Like Lists, tuples are ordered and we can access their elements using their index values
We cannot update items to a tuple once it is created. 
Tuples cannot be appended or extended.
We cannot remove items from a tuple once it is created. 
'''

# Tuples
# t = (1, 2, 3)
# t[0] = 10  # This will raise a TypeError

# Lists
# l = [1, 2, 3]
# l[0] = 10  # Modifies the list
# print(l)   # Output: [10, 2, 3]

