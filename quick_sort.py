## Quick Sort

# Time Complexity: O(n log n) on average, O(n^2) in the worst case (with poor pivot choices)
#                  Quick Sort has an average-case time complexity of O(n log n),
#                  making it efficient for most practical cases. However, in the worst case,
#                  it can degrade to O(n^2).

'''
Quicksort is a sorting algorithm based on the divide and conquer approach where

An array is divided into subarrays by selecting a pivot element (element selected from the array).

While dividing the array,
the pivot element should be positioned in such a way that elements less than pivot are kept on the left side
and elements greater than pivot are on the right side of the pivot.
The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
At this point, elements are already sorted. Finally, elements are combined to form a sorted array.
'''

def quick_sort(arr):
    if len(arr)<= 1:
        return arr
    
    else:
        pivot = arr[0]
        lesser_num = [i for i in arr[1:] if i <= pivot] #used list comprehension
        greater_num = [i for i in arr[1:] if i > pivot]
    
        return quick_sort(lesser_num) + [pivot] + quick_sort(greater_num)
    


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)

sorted_numbers = quick_sort(numbers)

print("Sorted array:", sorted_numbers)
    
    
#Results
'''
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
'''