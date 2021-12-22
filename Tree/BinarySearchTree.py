############################
# Binary Search Tree (BST) #
############################

'''
Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.
- It is called a binary tree because each tree node has a maximum of two children.
- It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.


The properties that separate a binary search tree from a regular binary tree is
1. All nodes of left subtree are less than the root node
2. All nodes of right subtree are more than the root node
3. Both subtrees of each node are also BSTs i.e. they have the above two properties


Operations that can be performed on a binary search tree:
1. Search Operation
2. Insert Operation
3. Delete Operation

Deletion Operation: There are 3 cases for deleting a node from a binary search tree.
Case 1: The node to be deleted is the leaf node. In such case, simply delete the node from the tree.
Case 2: The node to be deleted has a single child node. In such case follow the steps below:
        1. Replace that node with its child node.
        2. Remove the child node from its original position.
Case 3: The node to be deleted has two children. In such a case follow the steps below:
        1. Get the inorder successor of that node.
        2. Replace the node with the inorder successor.
        3. Remove the inorder successor from its original position.


Binary Search Tree Complexities
Time Complexity (n is the no. of nodes in the tree)
Operation   Best case   Avg case    Worst case
Search      O(log n)    O(log n)    O(n)
Insertion   O(log n)    O(log n)    O(n)
Deletion    O(log n)    O(log n)    O(n)

Space Complexity
The space complexity for all the opeartions is O(n)


Binary Search Tree Applications:
1. In multilevel indexing in the database
2. For dynamic sorting
3. For managing virtual memory areas in Unix kernel
'''

# create a node
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None
    
# Inorder traversal
def inorder(root):
    if root is not None:
        # traverse left
        inorder(root.left)
        # traverse root
        print(str(root.val) + " -> ", end='')
        # traverse right
        inorder(root.right)

# Search a node
def search(root, item):

    # if root is null or item is present ast root return root
    if root is None or root.val == item:
        return root
    
    # if item is greater than root's val
    if item > root.val:
        return search(root.right, item)
    
    # if item is smaller than root's val
    return search(root.left, item)

# Insert a node
def insert(root, item):

    # return a new node if the tree is empty
    if root is None:
        return Node(item)
    
    # traverse to the right place and insert the node
    if item < root.val:
        root.left = insert(root.left, item)
    else:
        root.right = insert(root.right, item)
    
    return root

# Find the inorder successor
def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left
    
    return current

# Deleting a node
def deleteNode(root, item):

    # return root if the tree is empty
    if root is None:
        return root
    
    # find the node to be deleted
    # if item to be deleted is smaller than the root's val then it lies in left subtree
    if item < root.val:
        root.left = deleteNode(root.left, item)

    # if item to be deleted is greater than the root's val then it lies in right subtree
    elif item > root.val:
        root.right = deleteNode(root.right, item)

    # if item is same as root's val, the this is the node to be deleted
    else:
        # if the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        # if the node has 2 children,
        # place the inorder successor(smallest in the right subtree) in position of the node to be deleted
        temp = minValueNode(root.right)

        # copy the inorder successor's content(val) to this node
        root.val = temp.val

        # delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)
