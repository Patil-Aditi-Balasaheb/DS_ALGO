###################################
# Heap queue (or heapq) in Python #
###################################

'''
Heap data structure is mainly used to represent a priority queue. 
In Python, it is available using “heapq” module. 
The property of this data structure in Python is that each time the smallest of heap element is popped(min heap). 
Whenever elements are pushed or popped, heap structure in maintained. 
The heap[0] element also returns the smallest element each time.

Operations on heap:
- heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
- heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.
- heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.
- heappushpop(heap, ele) :- This function combines the functioning of both push and pop operations in one statement, increasing efficiency. Heap order is maintained after this operation.
- heapreplace(heap, ele) :- This function also inserts and pops element in one statement, but it is different from above function. In this, element is first popped, then the element is pushed.i.e, the value larger than the pushed value can be returned. heapreplace() returns the smallest value originally in heap regardless of the pushed element as opposed to heappushpop().
- nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from the iterable specified and satisfying the key if mentioned.
- nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the iterable specified and satisfying the key if mentioned.
'''

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is :", list(li))

# using heappush() to push elements into heap - pushes 4
heapq.heappush(li, 4)

# printing modified heap
print ("The modified heap after push is :", list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is :", heapq.heappop(li))

# printing modified heap
print ("The modified heap after push is :", list(li))

# using heappushpop() to push and pop items simultaneously - pops 2
print ("The popped item using heappushpop() is :", heapq.heappushpop(li, 2))

# printing modified heap
print ("The modified heap after push is :", list(li))

# using heapreplace() to push and pop items simultaneously - pops 3
print ("The popped item using heapreplace() is :", heapq.heapreplace(li, 2))

# printing modified heap
print ("The modified heap after push is :", list(li))

# using nlargest to print 3 largest numbers
# prints 9, 7 and 5
print("The 3 largest numbers in list are :", heapq.nlargest(3, li))

# using nsmallest to print 3 smallest numbers
# prints 2, 4 and 5
print("The 3 smallest numbers in list are :", heapq.nsmallest(3, li))