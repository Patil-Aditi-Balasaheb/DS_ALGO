########################
# Balanced Binary Tree #
########################

'''
A balanced binary tree, also referred to as a height-balanced binary tree, is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1.

Following are the conditions for a height-balanced binary tree:
1. difference between the left and the right subtree for any node is not more than one
2. the left subtree is balanced
3. the right subtree is balanced

                    1  df=1
                   / \
                  /   \    
          df=0   2     3   df=0
                / \ 
        df=0   4   5   df=0
Balanced Binary Tree with depth at each level


                    1  df=2
                   / \
                  /   \    
          df=1   2     3   df=0
                / \ 
        df=0   4   5   df=1
                  /
                 6  df=0
Unbalanced Binary Tree with depth at each level

df = height of left child - height of right child

Balanced Binary Tree Applications:
- AVL Tree
- Balanced Binary Search Tree
'''

# create a tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# class to pass height object
class Height:
    def __init__(self):
        self.height = 0

# function to find height of binary tree
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

# function to check if tree is height balanced or not    
def isHeightBalanced(root):

    # if tree is empty return true
    if root is None:
        return True
    
    # lh and rh to store height of left and right subtree
    lh = Height()
    rh = Height()

    # calculating height of left and right subtree
    lh.height = height(root.left)
    rh.height = height(root.right)

    # l and r are used to check if left and right subtree are balanced
    l = isHeightBalanced(root.left)
    r = isHeightBalanced(root.right)

    # height of tree is max of left subtree height
    # and right subtree height plus 1

    # allowed values for (lh - rh) are 1, -1, 0
    if abs(lh.height - rh.height) <= 1:
        return l and r
    
    # if we reach here means tree is not height balanced tree
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.left.left = Node(8)

if isHeightBalanced(root):
    print("The tree is a balanced binary tree")
else:
    print("The tree is not a balanced binary tree")