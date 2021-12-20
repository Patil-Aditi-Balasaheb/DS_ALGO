######################
# Doubly Linked List #
######################

'''
A doubly linked list is a type of linked list in which each node consists of 3 components:
*prev - address of the previous node
data - data item
*next - address of next node

Insertion on a Doubly Linked list:
We can insert elements at 3 different positions of a DLL
1. Insert at the beginning
2. Insert in between nodes
3. Insert at the end

Deletion from a Doubly Linked list:
Similar to insertion, we can also delete a node from 3 different positions of a doubly linked list
1. Delete the first node of DLL
2. Delete the inner node
3. Delete the last node of DLL
'''

# A doubly linked list node
class Node:
    
    # constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# class to create a Doubly Linked List
class DoublyLinkedList:

    # constructor for empty Doubly linked list
    def __init__(self):
        self.head = None
    
    # insert a node at the beginning
    def insertStart(self, data):

        # allocate memory for new_node and assign data to new_node
        new_node = Node(data)

        # make next of new_node as head
        new_node.next = self.head

        # make prev of new_node as None (already None in constructor)

        # change prev of head node to new_node (now head is the second node)
        if self.head is not None:
            self.head.prev = new_node
        
        # move the head to point to the new_node
        self.head = new_node
    
    # insert a node after a specific node
    def insertAfter(self, prev_node, data):

        # check if prev_node is null
        if prev_node is None:
            print("The given previous node cannot be NULL")
            return
        
        # allocate memory for new_node and assign data to new_node
        new_node = Node(data)

        # make next of new_node as next of prev_node
        new_node.next = prev_node.next

        # make next of prev_node as new_node
        prev_node.next = new_node

        # make prev of new_node as prev_node
        new_node.prev = prev_node

        # change prev of new_node's next node to new_node
        if new_node.next:
            new_node.next.prev = new_node
    
    # insert a node at the end
    def insertEnd(self, data):

        # allocate memory for new_node and assign data to new_node
        new_node = Node(data)

        # make next of new_node as None (already None in constructor)

        # if the linked list is empty, then
        # make the new_node as head
        if self.head is None:
            self.head = new_node
            return

        # store the head node temporarily (for later use)
        temp = self.head

        # if the linked list is not empty, 
        # traverse to the end of the linked list
        while temp.next:
            temp = temp.next
        
        # make the next of last node(temp) as new_node
        temp.next = new_node

        # make the prev of new_node as last node(temp)
        new_node.prev = temp
    
    # prints contents of linked list starting from the given node
    # prints in both the direction i.e forward and backward
    def display(self, node):
        print("\nTraversal in forward direction")
        while node:
            print(node.data, end=" ->")
            last = node
            node = node.next

        print("\n\nTraversal in reverse direction")
        while last:
            print(last.data, end=" -> ")
            last = last.prev


def main():
    dll = DoublyLinkedList()

    while True:
        print("\nDOUBLY LINKED LIST MENU")
        print("1. Insert at the Beginning\t2. Insert After\t3. Insert at the End\t4. Display\t5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = input("Enter the data to insert: ")
            dll.insertStart(data)
        elif choice == 2:
            data = input("Enter the data to insert: ")
            pos = int(input("Enter the position at which the element is to be inserted: "))
            next1 = ['.next']*(pos - 2)
            next1 = "".join(next1)
            prev_node = 'dll.head' + next1      # prev_node = dll.head.next.next.next....
            dll.insertAfter(eval(prev_node), data)
        elif choice == 3:
            data = input("Enter the data to insert: ")
            dll.insertEnd(data)
        elif choice == 4:
            dll.display(dll.head)
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please enter a valid choice!")


if __name__ == "__main__":
    main()