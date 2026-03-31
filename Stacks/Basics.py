# Using Python list as a stack
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)
# Stack: [10, 20, 30] (30 is on top)

# Pop element
top = stack.pop()  # Returns 30
# Stack: [10, 20]

# Peek at top
if stack:
    top_element = stack[-1]  # Returns 20 without removing


## Using deque
from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()  # 3
stack.pop()  # 2
# Key idea
# A deque supports fast operations on both ends, so:

# Queue uses opposite ends (append + popleft)
# Stack uses the same end (append + pop)


# Yes—you can get the size, but in Python it’s not a “method on the list”; it’s the built-in function len().

# List as stack/queue
stack = [1, 2, 3]
len(stack)  # 3
# collections.deque as stack/queue
deque also supports len():

from collections import deque

q = deque([1, 2, 3])
len(q)  # 3
# So for both list and deque, you use len(...) to get the current number of elements.

# what is the difference between method and built in function in python...are they same , could they be used interchangeably?

# A built-in function and a method are not the same, and they generally cannot be used interchangeably.

# Built-in function
# A function that’s available globally in Python (no import needed).
# You call it like: function_name(obj, ...) (often the object is passed in as an argument).
# Example:

len([1, 2, 3])   # built-in function
# Method
# A function that “belongs to” an object (it’s defined on the object’s type/class).
# You call it like: obj.method_name(...).
# Example:

lst = [1, 2, 3]
lst.append(4)    # method of list
# Are they interchangeable?
# Usually no, because the syntax and where they live are different:

# len(lst) works, but lst.len() does not:

lst = [1, 2, 3]
len(lst)     # OK
# lst.len()  # AttributeError
lst.append(4) works, but append(lst, 4) does not (there is no built-in append):

lst.append(4)   # OK
# append(lst, 4)  # NameError
# Why does Python use built-ins like len() instead of lst.len()?
# Some operations are designed as generic operations that work across many types (lists, strings, dicts, deques, custom classes). len() is one of these.

# Internally, len(x) typically calls a special method on the object (called a “dunder” method):

len(x) → x.__len__()
# But you normally use len(x) rather than calling __len__() directly.

# Quick rule
# If it’s something generic across many types: often a built-in (e.g., len, sorted, sum).
# If it’s something specific to that data structure: often a method (e.g., list.append, deque.popleft, dict.get).

## Checking if a stack is empty is a common operation:

Python: if stack: or len(stack) != 0  # check if stack is not empty


