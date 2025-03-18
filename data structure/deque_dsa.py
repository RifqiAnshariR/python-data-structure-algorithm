class Deque:
    def __init__(self):
        self.deques = []

    def addFront(self, newItem):
        self.deques.insert(0, newItem)

    def addRear(self, newItem):
        self.deques.append(newItem)

    def removeFront(self):
        if self.isEmpty():
            print("Deque is empty!")
        else:
            return self.deques.pop(0)

    def removeRear(self):
        if self.isEmpty():
            return self.deques.pop()
        else:
            print("Deque is empty!")

    def isEmpty(self):
        return len(self.deques) == 0

    def __str__(self):
        return f"Your deque is: {self.deques}"
    
dq = Deque()
