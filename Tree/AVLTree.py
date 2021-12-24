############
# AVL Tree #
############

'''
AVL tree is a self-balancing binary search tree in which each node maintains extra information called a balance factor whose value is either -1, 0 or +1.
AVL tree got its name after its inventor Georgy Adelson-Velsky and Landis.

Balance Factor:
Balance factor of a node in an AVL tree is the difference between the height of the left subtree and that of the right subtree of that node.
Balance Factor = (Height of Left Subtree - Height of Right Subtree) or (Height of Right Subtree - Height of Left Subtree)
The self balancing property of an avl tree is maintained by the balance factor. The value of balance factor should always be -1, 0 or +1.


Operations on an AVL tree
1) Rotating the subtrees in an AVL Tree
   In rotation operation, the positions of the nodes of a subtree are interchanged.
   There are two types of rotations:
   1. Left Rotate:
      In left-rotation, the arrangement of the nodes on the right is transformed into the arrangements on the left node.

        BF=2      (50)        |   BF=0     (60)
                      \       |           /    \
        BF=-1        (60)     |   BF=0  (50)  (70)   BF=0
                         \    |
        BF=0            (70)  |

   2. Right Rotate:
      In right-rotation, the arrangement of the nodes on the left is transformed into the arrangements on the right node.
    
        BF=2         (50)     |   BF=0     (40)
                    /         |           /    \
        BF=1      (40)        |   BF=0  (30)  (50)   BF=0
                  /           |
        BF=0    (30)          |

   3. Left Right Rotate:
      In left-right rotation, the arrangements are first shifted to the left and then to the right.

        BF=2         (50)     |   BF=2        (50)    |   BF=0        (45)
                    /         |              /        |              /    \
        BF=1      (40)        |   BF=1     (45)       |   BF=0     (40)  (50)   BF=0
                      \       |            /          |
        BF=0          (45)    |   BF=0   (40)         |   

   4. Right Left Rotate:
      In right-left rotation, the arrangements are first shifted to the right and then to the left.

        BF=2     (50)         |   BF=2   (50)         |   BF=0        (55)
                     \        |              \        |              /    \
        BF=1        (60)      |   BF=1       (55)     |   BF=0     (50)  (60)   BF=0
                   /          |                 \     |
        BF=0    (55)          |   BF=0         (60)   |   


2) Insertion Operation in AVL Tree:
   A newNode is always inserted as a leaf node with balance factor equal to 0.


3) Deletion Operation in AVL Tree:
   A node is always deleted as a leaf node. After deleting a node, the balance factors of the nodes get changed. In order to rebalance the balance factor, suitable rotations are performed.


Complexities of Different operations on an AVL Tree
Insertion       Deletion        Search
O(log n)        O(log n)        O(log n)


AVL Tree Application
- For indexing large records in databases
- For searching in large databases
'''

import sys

# create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    
class AVLTree:
    # function to insert a node
    def insertNode(self, root, key):

        # find the correct location and insert the node
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insertNode(root.left, key)
        else:
            root.right = self.insertNode(root.right, key)
        
        # update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)

        # if the node is unbalanced
        if balanceFactor > 1:
            # left left
            if key < root.left.key:
                return self.rightRotate(root)
            
            # left right
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balanceFactor < -1:
            # right right
            if key > root.right.key:
                return self.lRotate(root)
            
            # right left
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root
    
    # function to delete a node
    # returns root of the modified subtree
    def deleteNode(self, root, key):

        # find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.deleteNode(root.left, key)
        elif key > root.key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.deleteNode(root.right, temp.key)
        
        # if tree has only one node, simply return it
        if root is None:
            return root
        
        # update the height of the ancestor nodes
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # update the balance factor and balance the tree 
        balanceFactor = self.getBalance(root)

        # if the node is unbalanced
        if balanceFactor > 1:
            # left left
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)

            # left right
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balanceFactor < -1:
            # right right
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            
            # right left
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root
    
    # function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # perform rotation
        y.left = z
        z.right = T2

        # update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # return the new root
        return y
    
    # function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # perform rotation
        y.right = z
        z.left = T3

        # update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # return the new root
        return y
    
    # function to get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        
        return root.height
    
    # function to get the balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    # print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
    

Tree = AVLTree()
root = None

nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = Tree.insertNode(root, num)

print("After Insertion: ")
Tree.printHelper(root, "", True)

print("\nPreorder traversal of the AVL tree is")
Tree.preOrder(root)

key = 13
root = Tree.deleteNode(root, key)

print("\n\nAfter Deletion: ")
Tree.printHelper(root, "", True)

print("\nPreorder traversal of the AVL tree is")
Tree.preOrder(root)