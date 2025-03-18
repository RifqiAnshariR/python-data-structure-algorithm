#enqueue = add item to end of queue
#dequeue = remove item and return the item at the front of queue

class Queue:
    def __init__(self):
        self.queues = []
        
    def isEmpty(self):
        return len(self.queues) == 0

    def enqueue(self, newItem):
        self.queues.append(newItem)
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            return self.queues.pop(0)
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            return self.queues[0]

    def size(self):
        return len(self.queues)

    def __str__(self):
        return f"Your queue is: {self.queues}"
    
q = Queue()
