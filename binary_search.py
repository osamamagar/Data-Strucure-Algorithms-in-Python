# Binary Search

'''
Binary Search is a searching algorithm that finds the position of a target value within a sorted array.

To do Binary Search, List or Array Must be sorted -i.e- we need to sort first.
- Binary Search Algorithm can be implemented in two ways which are discussed below.

1- Iterative Method
2- Recursive Method

'''


# Binary Search

def binary_search(arr, target):
    # Ensure the array is sorted
    arr.sort()

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "Not Found Element"

numbers = [2, 5, 4, 9, 6, 6, 9, 8, 5, 2, 1, 0]
target_element = 6
result = binary_search(numbers, target_element)

if isinstance(result, int):
    print(f"Element {target_element} is present at index {result}")
else:
    print("Element not found")
