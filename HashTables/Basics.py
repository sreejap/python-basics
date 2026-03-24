# Python's built-in hash function
key = "Alice"
hash_code = hash(key)
print(hash_code)  # Large number like 5789604752029982571

# Use hash code to find array index
capacity = 10
index = hash_code % capacity  # Index between 0-9


###################
# Create empty hash table
phone_book = {}

# Insert key-value pairs
phone_book["Alice"] = "555-1234"
phone_book["Bob"] = "555-5678"
phone_book["Carol"] = "555-9012"

# Lookup by key
print(phone_book["Alice"])  # "555-1234"

# Check if key exists
if "Bob" in phone_book:
    print("Found Bob")

# Delete a key
del phone_book["Carol"]

# Get with default value if key doesn't exist
number = phone_book.get("Dave", "Not found")

## method-based approach in Python, use pop:

phone_book.pop("Carol")          # deletes and returns the value (KeyError if missing)
phone_book.pop("Carol", None)  # safer approach
###########

## Iteration ###
phone_book = {"Alice": "555-1234", "Bob": "555-5678"}

# Iterate over keys
for name in phone_book:
    print(name)

# Iterate over key-value pairs
for name, number in phone_book.items():
    print(f"{name}: {number}")

## Iteration ##

## Remember ##
Python's dict uses [] for insert and lookup. Use in to check existence.

