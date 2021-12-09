#################
# binary search #
#################

# time complexity = O(logn)
# best case = O(1)
# worst case = O(logn)
# space complexity = O(1)

li = [10,20,30,40,50,60,70,80]
search = int(input("Enter a number to be searched: "))
low = 0
high = len(li) - 1

def binarySearch(li, low, high, search):
    if low >= high:
        return -1  # element is not present in the array
    
    mid = low + (high - low) // 2
    
    # if element is present at the middle itself
    if li[mid] == search:
        return mid
    
    # if element is greater than mid, then it can only be present in right subarray
    elif search > li[mid]:
        return binarySearch(li, mid+1, high, search)
    
    # else the element can only be present in left subarray
    else:
        return binarySearch(li, low, mid-1, search)


index = binarySearch(li, low, high, search)

if index == -1:
    print("Element not found")
else:
    print("Element found at position", index+1)