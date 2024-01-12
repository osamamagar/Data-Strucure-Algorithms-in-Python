## Merge Sort
'''
Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.

Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually.
Finally, sub-problems are combined to form the final solution.
'''




def merge_sort(arr):
    if len(arr) > 1:

        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing array elements
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0  
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(f"Merge: {arr}")


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)

merge_sort(numbers)

print("Sorted array:", numbers)



#Results

'''
Original array: [64, 34, 25, 12, 22, 11, 90]
Merge: [25, 34]
Merge: [25, 34, 64]
Merge: [12, 22]
Merge: [11, 90]
Merge: [11, 12, 22, 90]
Merge: [11, 12, 22, 25, 34, 64, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
'''