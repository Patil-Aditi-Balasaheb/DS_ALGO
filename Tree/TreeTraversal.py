##################
# Tree Traversal #
##################

'''
Traversing a tree means visiting every node in the tree.
There are 3 types of traversal:
1. Inorder - left subtree -> root -> right subtree
2. Preorder - root -> left subtree -> right subtree
3. Postorder - left subtree -> right subtree -> root
'''

# Tree traversal
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        # traverse left
        inorder(root.left)

        # traverse root
        print(str(root.val) + " -> ", end='')

        # traverse right
        inorder(root.right)

def preorder(root):
    if root:
        # traverse root
        print(str(root.val) + " -> ", end='')

        # traverse left
        preorder(root.left)

        # traverse right
        preorder(root.right)

def postorder(root):
    if root:
        # traverse left
        postorder(root.left)

        # traverse right
        postorder(root.right)

        # traverse root
        print(str(root.val) + " -> ", end='')


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal: ", end='')
inorder(root)

print("\nPreorder Traversal: ", end='')
preorder(root)

print("\nPostorder Traversal: ", end='')
postorder(root)