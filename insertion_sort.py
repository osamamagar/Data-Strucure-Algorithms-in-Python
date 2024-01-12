# Insertion Sort
####
# - Insertion sort works similarly as we sort cards in our hand in a card game.
# - We assume that the first card is already sorted then, we select an unsorted card.
# - If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left.
#   In the same way, other unsorted cards are taken and put in their right place.
#   A similar approach is used by insertion sort.
####

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f"pass {i} => {arr}")

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)

insertion_sort(numbers)

print("Sorted array:", numbers)




#Results
'''
Original array: [64, 34, 25, 12, 22, 11, 90]
pass 1 => [34, 64, 25, 12, 22, 11, 90]
pass 2 => [25, 34, 64, 12, 22, 11, 90]
pass 3 => [12, 25, 34, 64, 22, 11, 90]
pass 4 => [12, 22, 25, 34, 64, 11, 90]
pass 5 => [11, 12, 22, 25, 34, 64, 90]
pass 6 => [11, 12, 22, 25, 34, 64, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
'''