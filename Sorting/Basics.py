# Built-in sorting
numbers = [42, 17, 83, 29, 56, 73]

# Sort in place
numbers.sort()
print(numbers)  # [17, 29, 42, 56, 73, 83]

# Create new sorted list
original = [42, 17, 83, 29, 56, 73]
sorted_numbers = sorted(original)
print(sorted_numbers)  # [17, 29, 42, 56, 73, 83]
print(original)  # [42, 17, 83, 29, 56, 73] (unchanged)

# Binary search on sorted data
import bisect

sorted_list = [17, 29, 42, 56, 73, 83]
index = bisect.bisect_left(sorted_list, 73)
if index < len(sorted_list) and sorted_list[index] == 73:
    print(f"Found at index {index}")  # Found at index 4
