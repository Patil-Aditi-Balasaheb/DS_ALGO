##################
# Selection sort #
##################

# time complexity = O(n^2) - bcoz there are 2 nested loops
# space complexity = O(1)

def selectionSort(arr, n):
    
    # traverse through all array elements
    for i in range(n):
        
        # find the minimum element in remaining unsorted array
        minIndex = i
        for j in range(i+1, n):
            if(arr[minIndex] > arr[j]):
                minIndex = j
        
        # swap the found minimum element with the first element
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


arr = [54, 32, 56, 18, 19, 5, 1]

selectionSort(arr, len(arr))

print("Sorted array:\n", arr)