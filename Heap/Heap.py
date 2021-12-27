########
# Heap #
########

'''
A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types:
1. Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
2. Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.

                 10                             100
                /  \                           /   \
             15      30                      40     50
            /  \    /  \                    /  \   /  \
           40  50  100 40                  10  15 50  40
               Min Heap                      Max Heap

Heap Operations:
1. Heapify: Heapify is the process of creating a heap data structure from a binary tree. It is used to create a Min-Heap or a Max-Heap.
2. Insert Element into Heap
3. Delete Element from Heap
4. Peek (Find max/min): Peek operation returns the maximum element from Max Heap or minimum element from Min Heap without deleting the node.
   For both Max heap and Min Heap - return rootNode
5. Extract-Max/Min: Extract-Max returns the node with maximum value after removing it from a Max Heap whereas Extract-Min returns the node with minimum after removing it from Min Heap.

Heap data structure applications:
- Heap is used while implementing a priority queue.
- Dijkstra's Algorithm
- Heap Sort
'''

# Max-Heap implementation

# heapify a subtree rooted with node i which is
# an index of arr[] and n is the size of heap
def heapify(arr, n, i):
    largest = i         # initializing largest as root
    left = 2 * i + 1    # left child
    right = 2 * i + 2   # right child

    # if left child is larger than root
    if left < n and arr[largest] < arr[left]:
        largest = left
    
    # if right child is larger than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # recursively heapify the affected subtree
        heapify(arr, n, largest)

# insert a node
def insert(arr, num):
    size = len(arr)
    if size == 0:
        arr.append(num)
    else:
        arr.append(num)
        # heapify the tree
        for i in range((len(arr)//2)-1, -1, -1):
            heapify(arr, len(arr), i)

# delete a node from heap
def delete(arr, num):
    size = len(arr)
    i = 0
    # find the element to be deleted
    for i in range(0, size):
        if num == arr[i]:
            break
    
    # replace the element to be deleted with root element
    arr[i], arr[size - 1] = arr[size - 1], arr[i]
    arr.remove(num)

    # heapify the tree
    for i in range((len(arr)//2)-1, -1, -1):
        heapify(arr, len(arr), i)

# peek operation retuns max or min element from a heap
def peek(arr):
    return arr[0]

arr = []
insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)
insert(arr, 100)
insert(arr, 50)

print("Max-Heap array:", *arr)
delete(arr, 4)
print("After deleting an element:", *arr)
print("Peek element:", peek(arr))

delete(arr, 100)
print("After deleting an element:", *arr)
print("Peek element:", peek(arr))