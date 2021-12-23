#######################
# Perfect Binary Tree #
#######################

'''
A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

             1
            / \
           /   \    
          2     3
         / \   / \
        4   5 6   7
     Perfect Binary Tree

All the internal nodes have a degree of 2.

Recursively, a perfect binary tree can be defined as:
1. If a single node has no children, it is a perfect binary tree of height h = 0,
2. If a node has h > 0, it is a perfect binary tree if both of its subtrees are of height h - 1 and are non-overlapping.

Perfect Binary Tree Theorems:
1. A perfect binary tree of height h has 2^(h + 1) - 1 node.
2. A perfect binary tree with n nodes has height log(n + 1) - 1 = Θ(ln(n)).
3. A perfect binary tree of height h has 2^h leaf nodes.
4. The average depth of a node in a perfect binary tree is Θ(ln(n)).
'''

# checking if a binary tree is a perfect binary tree or not

# creating a node
class Node:
    def __init__(self, item):
        self.item = item
        self.right = self.left = None

# calculating the depth
def calculateDepth(root):
    d = 0
    while(root is not None):
        d += 1
        root = root.left
    return d

# function to check if the tree is perfect binary tree
def isPerfectTree(root, d, level=0):

    # tree is empty
    if(root is None):
        return True
    
    # checking the presence of trees
    if(root.left is None and root.right is None):
        return (d == level + 1)
    
    if(root.left is None or root.right is None):
        return False
    
    return (isPerfectTree(root.left, d, level + 1) and isPerfectTree(root.right, d, level + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

if(isPerfectTree(root, calculateDepth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")