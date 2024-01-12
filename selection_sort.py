#Selection Sort
###
# - Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.
# - Compare minimum with the third element. Again, if the third element is smaller,
#   then assign minimum to the third element otherwise do nothing. The process goes on until the last element.
###

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                
                print(f"Pass{i+1}:{arr}")


numbers=[-5,56,2,0,45,-10,20,0]
selection_sort(numbers)
print("Sorted array:", numbers)


#Results
'''
Pass1:[-10, 56, 2, 0, 45, -5, 20, 0]
Pass2:[-10, 2, 56, 0, 45, -5, 20, 0]
Pass2:[-10, 0, 56, 2, 45, -5, 20, 0]
Pass2:[-10, -5, 56, 2, 45, 0, 20, 0]
Pass3:[-10, -5, 2, 56, 45, 0, 20, 0]
Pass3:[-10, -5, 45, 56, 2, 0, 20, 0]
Pass3:[-10, -5, 0, 56, 2, 45, 20, 0]
Pass3:[-10, -5, 20, 56, 2, 45, 0, 0]
Pass4:[-10, -5, 20, 2, 56, 45, 0, 0]
Pass4:[-10, -5, 20, 45, 56, 2, 0, 0]
Pass4:[-10, -5, 20, 0, 56, 2, 45, 0]
Pass4:[-10, -5, 20, 0, 56, 2, 45, 0]
Pass5:[-10, -5, 20, 0, 2, 56, 45, 0]
Pass5:[-10, -5, 20, 0, 45, 56, 2, 0]
Pass5:[-10, -5, 20, 0, 0, 56, 2, 45]
Pass6:[-10, -5, 20, 0, 0, 2, 56, 45]
Pass6:[-10, -5, 20, 0, 0, 45, 56, 2]
Pass7:[-10, -5, 20, 0, 0, 45, 2, 56]
Sorted array: [-10, -5, 20, 0, 0, 45, 2, 56]

'''