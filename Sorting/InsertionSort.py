def insertion_sort(arr):
    n = len(arr)

    # Start from second element
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements right until correct position found
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at correct position
        arr[j + 1] = key

    return arr

# Example usage
numbers = [12, 11, 13, 5, 6]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)  # [5, 6, 11, 12, 13]
