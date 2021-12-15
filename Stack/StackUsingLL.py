#################################################
# Stack Implementation using singly linked list #
#################################################

class Node:
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    # head is default NULL
    def __init__(self):
        self.head = None
        self.count = 0
        
    # Returns the number of element in stack
    def size(self) :
        return self.count
     
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
     
    # Method to add data to the stack
    # adds to the start of the stack
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
        
        self.count += 1
     
    # Remove element that is the current head (start of the stack)
    def pop(self):
        if self.isempty():
            return 'Stack Underflow'
        else:
            # Removes the head node and makes
            # the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            self.count -= 1
            return 'Popped element is ' + str(poppednode.data)
     
    # Returns the head node data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
     
    # Prints out the stack    
    def display(self):
        iternode = self.head
        
        if self.isempty():
            print("Stack Underflow")
        else:
            while(iternode != None): 
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return


def main():
    
    MyStack = Stack()
    
    while(True):
        print("\nSTACK MENU")
        print("1. Push\t2. Pop\t3. Peek\t4. Display\t5. Size\t6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            d = int(input("Enter the data to insert: "))
            MyStack.push(d)
        elif choice == 2:
            print(MyStack.pop())
        elif choice == 3:
            print("Top element is", MyStack.peek())
        elif choice == 4:
            MyStack.display()
        elif choice == 5:
            print("Size : ", MyStack.size())
        elif choice == 6:
            break
        else:
            print("Invalid choice! Please enter a valid choice!")


if __name__ == "__main__":
    main()