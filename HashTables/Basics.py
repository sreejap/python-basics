# Python's built-in hash function
key = "Alice"
hash_code = hash(key)
print(hash_code)  # Large number like 5789604752029982571

# Use hash code to find array index
capacity = 10
index = hash_code % capacity  # Index between 0-9
