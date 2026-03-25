def bubble_sort(arr):
    n = len(arr)

    # Outer loop for each pass
    for i in range(n - 1):
        swapped = False

        # Inner loop for comparisons
        for j in range(n - 1 - i):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Early termination if no swaps
        if not swapped:
            break

    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
