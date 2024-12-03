'''
 _______  __   __  _______  __   __  _______  __    _    ___      ___   _______  _______  _______ 
|       ||  | |  ||       ||  | |  ||       ||  |  | |  |   |    |   | |       ||       ||       |
|    _  ||  |_|  ||_     _||  |_|  ||   _   ||   |_| |  |   |    |   | |  _____||_     _||  _____|
|   |_| ||       |  |   |  |       ||  | |  ||       |  |   |    |   | | |_____   |   |  | |_____ 
|    ___||_     _|  |   |  |       ||  |_|  ||  _    |  |   |___ |   | |_____  |  |   |  |_____  |
|   |      |   |    |   |  |   _   ||       || | |   |  |       ||   |  _____| |  |   |   _____| |
|___|      |___|    |___|  |__| |__||_______||_|  |__|  |_______||___| |_______|  |___|  |_______|

Notes prepared by Codex Club, Quantum University – "Code, Collaborate, Create – Building a Better Tomorrow, One Line of Code at a Time."
'''
'''
### Summary 
Python lists are highly versatile and support a variety of operations like concatenation, repetition, 
indexing, slicing, and more. They can store elements of any type, and their mutable nature allows modification of items or slices directly.

These operations demonstrate common ways to manipulate Python lists. Here's a summary of their functions:
-  append() : Adds an element to the end of the list.
-  pop() : Removes and returns an element (default: last element).
-  insert() : Adds an element at a specific position.
-  reverse() : Reverses the list in place.
-  sort() : Sorts the list in place.

'''

'''
###Python lists Key Points:
1.Flexible Arrays, Not Lisp-like Linked Lists
   - Python lists are dynamic arrays, meaning their size can change.
   - Unlike linked lists (used in Lisp), Python lists store elements in contiguous memory, making access and updates faster in most cases.
'''
#Example List:
# a = [99, "bottles of beer", ["on", "the", "wall"]]
# - Python lists can hold elements of different data types, including nested lists.
'''
2. Same Operators as Strings
   - Lists support similar operations to strings:
'''
# - Concatenation ( + ):
# a = [1, 2, 3]
# b = [4, 5]
# print(a + b)  # Output: [1, 2, 3, 4, 5]

# - Repetition ( * ):
# print(a * 3)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# - Indexing ( a[0] ,  a[-1] ):
# print(a[0])  # Output: 1
# print(a[-1]) # Output: 3

# - Slicing ( a[1:] ):
# print(a[1:])  # Output: [2, 3]

# - Length ( len() ):
# print(len(a))  # Output: 3

'''
3. Item and Slice Assignment
   - Lists are mutable, so you can modify their elements or slices.
'''
# - Item Assignment:
# a = [99, "bottles of beer", ["on", "the", "wall"]]
# a[0] = 98
# print(a)  # Output: [98, "bottles of beer", ["on", "the", "wall"]]

# - Slice Assignment:
# a[1:2] = ["bottles", "of", "beer"]
# print(a)  # Output: [98, "bottles", "of", "beer", ["on", "the", "wall"]]

'''
4. Deleting Elements
   - Use  'del'  to remove elements from a list:
'''
# del a[-1]
# print(a)  # Output: [98, "bottles", "of", "beer"]



### More List Operations

'''
1.  a = range(5) 
   - Creates a sequence of numbers from 0 to 4 ( [0, 1, 2, 3, 4] ).
   - Note: In Python 3,  range(5)  creates a  range  object, so it needs to be converted to a list using  list(range(5)) :
'''
a = list(range(5))
# print(a)  # Output: [0, 1, 2, 3, 4]
      
'''
2.  a.append(5) 
   - Adds the element  5  to the end of the list.
   - Example:
'''    
# a.append(5)
# print(a)  # Output: [0, 1, 2, 3, 4, 5]
      
'''
3.  a.pop() 
   - Removes and returns the last element of the list.
   - Example:
'''    
popped_item = a.pop()
print(a)            # Output: [0, 1, 2, 3, 4]
print(popped_item)  # Output: 5
      
'''
4.  a.insert(0, 42) 
   - Inserts the value  42  at index  0  (the beginning of the list).
   - Example:
'''  
# a.insert(0, 42)
# print(a)  # Output: [42, 0, 1, 2, 3, 4]
      
'''
5.  a.pop(0) 
   - Removes and returns the element at index  0 .
   - Example:
'''     
# removed_item = a.pop(0)
# print(a)            # Output: [0, 1, 2, 3, 4]
# print(removed_item) # Output: 42
      
'''
6.  a.reverse() 
   - Reverses the order of the list in place.
   - Example:
'''     
# a.reverse()
# print(a)  # Output: [4, 3, 2, 1, 0]
      
'''
7.  a.sort() 
   - Sorts the list in ascending order.
   - Example:
'''     
# a.sort()
# print(a)  # Output: [0, 1, 2, 3, 4]
