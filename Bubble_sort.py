#bubble_sort

# Time Complexity: O(n^2) in the worst case


# This algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# The pass through the list is repeated until no swaps are needed, indicating that the list is sorted.
#
#
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        print(f"Pass {i + 1}: {arr}")

# Example usage:
numbers = [5, 2, 9, 1, 5, 6]
print("Original array:", numbers)

bubble_sort(numbers)

print("Sorted array:", numbers)


#Results
'''
Original array: [5, 2, 9, 1, 5, 6]
Pass 1: [2, 5, 1, 5, 6, 9]
Pass 2: [2, 1, 5, 5, 6, 9]
Pass 3: [1, 2, 5, 5, 6, 9]
Pass 4: [1, 2, 5, 5, 6, 9]
Pass 5: [1, 2, 5, 5, 6, 9]
Pass 6: [1, 2, 5, 5, 6, 9]
Sorted array: [1, 2, 5, 5, 6, 9]
'''