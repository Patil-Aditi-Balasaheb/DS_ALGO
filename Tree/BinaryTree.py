###############
# Binary Tree #
###############

'''
A binary tree is a tree data structure in which each parent node can have at most two children. 
Each node of a binary tree consists of three items:
- data item
- address of left child
- address of right child

Binary Tree applications:
1. for easy and quick access to data
2. in router algorithms
3. to implement heap data structure
4. syntax tree
'''

# Binary Tree
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item
    
    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' -> ')

        if self.left:
            self.left.traversePreOrder()
        
        if self.right:
            self.right.traversePreOrder()
    
    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        
        print(self.val, end=' -> ')

        if self.right:
            self.right.traverseInOrder()
    
    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        
        if self.right:
            self.right.traversePostOrder()
        
        print(self.val, end=' -> ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Inorder Traversal: ", end='')
root.traverseInOrder()

print("\nPreorder Traversal: ", end='')
root.traversePreOrder()

print("\nPostorder Traversal: ", end='')
root.traversePostOrder()