def selection_sort(arr):
    n = len(arr)

    # Outer loop moves the boundary
    for i in range(n - 1):
        # Track index of minimum in unsorted portion
        min_index = i

        # Inner loop scans unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap minimum to boundary position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 64]
