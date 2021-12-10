##############
# Merge sort #
##############

# time complexity = O(nLogn) - in all 3 cases i.e worst, average and best as merge sort always divides the array into two halves and takes linear time to merge two halves.
# space complexity = O(n)

def mergeSort(arr, n):
    if(n > 1):
        
        # finding the mid of the array
        mid = n // 2
        
        # dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        
        # sorting the first half
        mergeSort(L, len(L))
        
        # sorting the second half
        mergeSort(R, len(R))
        
        i = j = k = 0
        
        # copy data to temp arrays l[] and R[]
        while(i < len(L) and j < len(R)):
            if(L[i] < R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # checking if any element was left
        while(i < len(L)):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while(j < len(R)):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [12, 11, 13, 5, 6, 7]

mergeSort(arr, len(arr))

print("Sorted array:\n", arr)