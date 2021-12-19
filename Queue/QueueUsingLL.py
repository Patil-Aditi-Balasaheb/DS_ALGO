#################################################
# Queue Implementation using singly linked list #
#################################################

class Node:
    # Class to create nodes of linked list to store a queue entry
    # constructor initializes node automatically
    def __init__(self, data):
        self.data = data
        self.next = None


# class to represent a queue
class Queue:
    
    def __init__(self):
        self.front = self.rear = None
    
    def isEmpty(self):
        return self.front == None
    
    # function to add an item to the queue
    def enqueue(self, data):
        item = Node(data)
        if self.rear == None:
            self.front = self.rear = item
        else:
            self.rear.next = item
            self.rear = item
        
        return str(data) + ' enqueued to queue'
    
    # function to remove an item from queue
    def dequeue(self):
        if self.isEmpty():
            return 'Queue Empty'
        
        if self.front == None:
            self.rear = None

        item = self.front
        self.front = item.next
        return str(item.data) + ' dequeued from queue'
         
    # Function to get front of queue
    def queue_front(self):
        if self.isEmpty():
            return 'Queue Empty'
        else:
            return 'Front item is ' + str(self.front.data)

    # Function to get rear of queue
    def queue_rear(self):
        if self.isEmpty():
            return 'Queue Empty'
        else:
            return 'Rear item is ' + str(self.rear.data)

    # Prints out the queue    
    def display(self):
        iternode = self.front
        
        if self.isEmpty():
            print("Queue Empty")
        else:
            while(iternode != None): 
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return


def main():
    queue = Queue()
    while(True):
        print("\nQUEUE MENU")
        print("1. Enqueue\t2. Dequeue\t3. Front\t4. Rear\t5. Display\t6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            d = int(input("Enter the data to insert: "))
            print(queue.enqueue(d))
        elif choice == 2:
            print(queue.dequeue())
        elif choice == 3:
            print(queue.queue_front())
        elif choice == 4:
            print(queue.queue_rear())
        elif choice == 5:
            queue.display()
        elif choice == 6:
            break
        else:
            print("Invalid choice! Please enter a valid choice!")

            
if __name__ == "__main__":
    main()