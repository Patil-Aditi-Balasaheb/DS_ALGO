#########
# Stack #
#########

'''
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 
In stack, a new element is added at one end and an element is removed from that end only. 
The insert and delete operations are often called push and pop.
'''

class Stack:
    def __init__(self, d = None):
        if d == None:
            self.data = list()
        else:
            self.data = d
    
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False
    
    def push(self, d):
        self.data.append(d)
        
    def pops(self):
        if self.isEmpty():
            return 'Stack is empty'
        else:
            return 'Popping element: ' + str(self.data.pop())
    
    def display(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            print('Stack content:')
            for i in range(len(self.data) - 1, -1, -1):
                print(self.data[i])


def main():
    stack = Stack()
    while(True):
        print("\nSTACK MENU")
        print("1. Push\t2. Pop\t3. Display\t4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            d = int(input("Enter the data to insert: "))
            stack.push(d)
        elif choice == 2:
            print(stack.pops())
        elif choice == 3:
            stack.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please enter a valid choice!")

            
if __name__ == "__main__":
    main()