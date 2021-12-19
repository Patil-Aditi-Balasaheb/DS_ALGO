#########
# Queue #
#########

'''
Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). 
A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.

Operations on Queue: 
Mainly the following four basic operations are performed on queue:
> Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition. 
> Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition. 
> Front: Get the front item from queue. 
> Rear: Get the last item from queue. 
'''

# Class Queue to represent a queue
class Queue:

    # constructor to initialize the class variables
    def __init__(self, capacity):
        self.front = self.size = 0  # initializing front=0 and size=0
        self.rear = capacity - 1    # initializing rear=capacity-1
        self.Q = [None] * capacity  # this array is used as a queue
        self.capacity = capacity
    
    # queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # queue is full when size becomes equal to the capacity
    def isFull(self):
        return self.size == self.capacity
    
    # function to add an item to the queue
    # it changes rear and size
    def enqueue(self, data):
        if self.isFull():
            return 'Queue Full'
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.Q[self.rear] = data
            self.size += 1
            return str(data) + ' enqueued to queue'
    
    # function to remove an item from queue
    # it changes front and size
    def dequeue(self):
        if self.isEmpty():
            return 'Queue Empty'
        else:
            data = self.Q[self.front]
            self.Q[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return str(data) + ' dequeued from queue'
    
    # Function to get front of queue
    def queue_front(self):
        if self.isEmpty():
            return 'Queue Empty'
        else:
            return 'Front item is ' + str(self.Q[self.front])

    # Function to get rear of queue
    def queue_rear(self):
        if self.isEmpty():
            return 'Queue Empty'
        else:
            return 'Rear item is ' + str(self.Q[self.rear])


def main():
    queue = Queue(5)
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
            print(*(queue.Q))
        elif choice == 6:
            break
        else:
            print("Invalid choice! Please enter a valid choice!")

            
if __name__ == "__main__":
    main()