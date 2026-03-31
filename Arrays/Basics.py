# Python `list` can hold mixed types (`[1, "a", None]`).
# create an array
numbers = [10, 20, 30, 40, 50] 

# Read elements by index
first = numbers[0]   # 10
third = numbers[2]   # 30
last = numbers[4]    # 50

print(f"Third element: {third}")  # Third element: 30

# Update elements by index
numbers[0] = 100   # Change first element

print(numbers)  # [100, 20, 300, 40, 500] 

# Iteration

numbers = [10, 20, 30, 40, 50]

# Method 1: For loop with index
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# Method 2: For-each loop (more Pythonic)
for num in numbers:
    print(num)

# Append: adding to the end
numbers = [10, 20, 30]
numbers.append(40)

# building arrays incrementally
arr = [] # empty array
   for i in range (len(values)): # values is an input array
        arr.append(values[i])
    return len(arr)

# Pop: removing from the end
numbers = [10, 20, 30, 40]
last = numbers.pop()
print(last)     # 40
print(numbers)  # [10, 20, 30]

# Check if empty before popping
if len(numbers) > 0:
    numbers.pop()
    # Safe!

# Pop is O(1) - always fast

# reverse traversal
for i in range(len(arr) - 1, index, -1):

# ### What `range(len(arr) - 1, index, -1)` means

# - starting at `start = len(arr) - 1` (the **last valid index**),
# - stopping **just after** `stop = index` (so it **does not include** `index`),
# - moving by `step = -1` (so it goes **backwards**).

# insert at position

def insert_at_position(arr: list[int], index: int, value: int) -> list[int]:    
    if index < 0 or index > len(arr):
        return arr 

    arr.append(0) # add an empty value
    for i in range (len(arr)-1,index,-1): # this is reverse traversal
        arr[i] = arr[i-1]

    arr[index] = value
    return arr
    

# Python list (dynamic array)
arr = []          # size=0, initial capacity varies
arr.append(1)     # size=1


# shallow copy
arr[:] returns a shallow copy of the list.

arr = [1, 2, 3]
copy = arr[:]

copy is arr        # False (different objects)
copy == arr        # True (same contents)

# If your list contains mutable objects (like other lists), those inner objects are not copied, just referenced:
arr = [[1, 2], [3, 4]]
copy = arr[:]

copy[0][0] = 99

print(arr)  # [[99, 2], [3, 4]] ← original is affected
