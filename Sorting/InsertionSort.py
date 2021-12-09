##################
# Insertion sort #
##################

# time complexity = O(n^2) - insertion takes max time to sort if elements are sorted in reverse order and it takes min time O(n) when elements are already sorted
# space complexity = O(1)

def insertionSort(arr, n):
    
    # traverse through 1 to length of arr
    for i in range(1, n):
        key = arr[i]
        
        # move elements of arr[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key


arr = [54, 32, 56, 18, 19, 5, 1]

insertionSort(arr, len(arr))

print("Sorted array:\n", arr)