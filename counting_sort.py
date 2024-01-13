##Count Sort

#Time Complexity: O(n)
'''
Counting sort is a sorting algorithm that sorts the elements of an array
by counting the number of occurrences of each unique element in the array.
The count is stored in an auxiliary array and the sorting is done
by mapping the count as an index of the auxiliary array.
'''


def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Create a count array to store the count of each element
    count = [0] * (max_element + 1)

    # Count the occurrences of each element
    for element in arr:
        count[element] += 1

    sorted_array = []
    for i in range(len(count)):
        sorted_array.extend([i] * count[i])

    return sorted_array

# Example usage:
numbers = [4, 2, 2, 8, 3, 3, 1]
sorted_numbers = counting_sort(numbers)
print("Original array:", numbers)
print("Sorted array:", sorted_numbers)



#Results 
'''
Original array: [4, 2, 2, 8, 3, 3, 1]
Sorted array: [1, 2, 2, 3, 3, 4, 8]
'''