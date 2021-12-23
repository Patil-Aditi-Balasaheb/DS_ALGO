####################
# Full Binary Tree #
####################

'''
A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.
It is also known as a proper binary tree.

                    1
                   / \
                  2   3
                 / \
                4   5
                   / \
                  6   7
            Full Binary Tree

Full Binary Tree Theorems:
let, i = the no. of internal nodes
     n = be the total no. of nodes
     l = no. of leaves
     & = no. of levels

1. The number of leaves is i + 1.
2. The total number of nodes is 2i + 1.
3. The number of internal nodes is (n - 1) / 2.
4. The number of leaves is (n + 1) / 2.
5. The total number of nodes is 2l - 1.
6. The number of internal nodes is l - 1.
7. The number of leaves is at most 2 raise to (λ - 1).
'''

# checking if a binary tree is a full binary tree or not

# creating a node
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# function to check full binary tree
def isFullTree(root):

    # tree is empty
    if root is None:
        return True
    
    # checking whether child is present
    if root.left is None and root.right is None:
        return True
    
    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))
    
    return False


root = Node(1)
root.right = Node(3)
root.left = Node(2)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.right.left = Node(6)
root.left.right.right = Node(7)

if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")