###############
# Bubble sort #
###############

# worst and best case time complexity = O(n^2) - worst case occurs when array is reversed sorted
# best case time complexity = O(n) - best case occurs when array is already sorted
# space complexity = O(1)

def bubbleSort(arr, n):
    
    # traversing through all array elements
    for i in range(n):
        swapped = False
        
        # last i elements are already in place
        for j in range(n-i-1):
            
            # traversing the array from 0 to n-i-1
            # Swaping if the element found is greater than the next element
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break


arr = [54, 32, 56, 18, 19, 5, 1]

bubbleSort(arr, len(arr))

print("Sorted array:\n", arr)