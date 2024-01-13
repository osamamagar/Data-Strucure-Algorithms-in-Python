## Linear Search

'''
Linear search is a simple search algorithm that checks each element in a list
or array until the target element is found or the end of the list is reached.
'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "Not Found Element"

numbers = [2, 3, 6, 4, 5]
target_element = 4  # Change this to the element you want to search for

result = linear_search(numbers, target_element)

if isinstance(result, int):
    print(f"Element {target_element} found at index {result}.")
else:
    print(result)
