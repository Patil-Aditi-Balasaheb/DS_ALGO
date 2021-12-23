########################
# Complete Binary Tree #
########################

'''
A complete binary tree is a binary tree in which all the levels are completely filled except possibly the lowest one, which is filled from the left.

A complete binary tree is just like a full binary tree, but with two major differences
1. All the leaf elements must lean towards the left.
2. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

                1                       1
               / \                     / \
              /   \                   /   \
             2     3                 2     3
            / \   /                 / \
           4   5 6                 6   4
                  Complete Binary Tree

Complete Binary Tree Applications
- Heap-based data structures
- Heap sort
'''

# checking if a binary tree is a complete binary tree or not

# creating a node
class Node:
    def __init__(self, item):
        self.item = item
        self.left = self.right = None

# function to count the number of nodes
def countNodes(root):
    if root is None:
        return 0
    return (1 + countNodes(root.left) + countNodes(root.right))

# function to check if the tree is complete binary tree
def isCompleteTree(root, index, numberNodes):

    # tree is empty
    if root is None:
        return True
    
    if index >= numberNodes:
        return False
    
    return (isCompleteTree(root.left, 2 * index + 1, numberNodes) and isCompleteTree(root.right, 2 * index + 2, numberNodes))


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = countNodes(root)
index = 0

if isCompleteTree(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")