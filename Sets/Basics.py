# Create empty set
numbers = set()

# Add elements (duplicates ignored)
numbers.add(1)
numbers.add(2)
numbers.add(2)  # Duplicate, ignored
numbers.add(3)
numbers.add(1)  # Duplicate, ignored

print(numbers)  # {1, 2, 3}

# Check membership - O(1)
if 2 in numbers:
    print("Found 2")

# Remove element
numbers.remove(2)

a = {1, 2, 3}
b = {2, 3, 4}

# Union - all elements
print(a | b)  # {1, 2, 3, 4}

# Intersection - common elements
print(a & b)  # {2, 3}

# Difference - in a but not b
print(a - b)  # {1}

# Python sets support `|`, `&`, and `-` operators.
