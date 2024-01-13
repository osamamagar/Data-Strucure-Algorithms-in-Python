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


'''
General Recommendations:
Base Case Complexity:

If the problem naturally exhibits a recursive structure and can be easily broken down into smaller subproblems,
a recursive solution might be more elegant.
- Memory Efficiency:

If memory efficiency is crucial, especially for large inputs, an iterative solution might be preferred.

- Code Readability:

Consider the readability of the code. Some problems are more naturally expressed using recursion,
making the code more intuitive.

- Language and Stack Limitations:

Some programming languages have limitations on the maximum recursion depth,
and excessively deep recursion may lead to a stack overflow. In such cases,
an iterative solution might be necessary.

- Tail Recursion Optimization:

Some languages support tail call optimization, which can eliminate the memory overhead of recursive calls.
In such cases, the choice may depend on personal preference.
In many cases, it comes down to the specific problem,
the characteristics of the input data, and the context in which the code will be used.
It's also common for experienced programmers to use a mix of both approaches based on the specific needs of the task at hand.


'''
