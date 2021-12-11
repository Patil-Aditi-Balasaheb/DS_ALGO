##############
# Quick sort #
##############

# worst case time complexity = O(n^2) - it occurs when the pivot element is either the greatest or the smallest. This condition leads to the case in which the pivot element lies in an extreme end of the sorted array. One subarray is always empty and another subarray contains n-1 elements. Thus, quicksort is called only on this subarray. However, this sort has better performance for scattered pivots.
# best and avg case time complexity = O(nLogn) - best case occurs when the pivot element is always the middle or near to the middle element. Avg case occurs when all the above conditions do not occur.
# space complexity = O(Logn)

def partition(arr, start, end):
    
    # initializing pivot's index to start
    pivot_index = start
    pivot = arr[pivot_index]
    
    # this loop runs till start pointer crosses end pointer, and when it does 
    # we swap the pivot with element on end pointer
    while(start < end):
        
        # increment the start pointer till it finds an element greater than pivot
        while(start < len(arr) and arr[start] <= pivot):
            start += 1
        
        # decrement the end pointer till it finds an element less than pivot
        while(arr[end] > pivot):
            end -= 1
        
        # if start and end have not crossed each other, swap the numbers on start and end
        if(start < end):
            arr[start], arr[end] = arr[end], arr[start]
    
    # swap pivot element with element on end pointer
    # this puts pivot on its correct sorted place
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    
    # returning end pointer to divide the array into 2
    return end


def quickSort(arr, start, end):
    if(start < end):
        
        # p is partitioning index, arr[p] is at right place
        p = partition(arr, start, end)
        
        # sort elements before partition and after partition
        quickSort(arr, start, p - 1)
        quickSort(arr, p + 1, end)


arr = [10, 7, 8, 9, 1, 5]

quickSort(arr, 0, len(arr)-1)

print(f"Sorted array:\n{arr}")