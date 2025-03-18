class Stack:
    def __init__(self):
        self.stacks = []
    
    def isEmpty(self):
        return len(self.stacks) == 0

    def push(self, newItem):
        self.stacks.append(newItem)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            return self.stacks.pop()
            
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            return self.stacks[-1]

    def size(self):
        return len(self.stacks)
    
    def __str__(self):
        return f"Your stack is: {self.stacks}"
    
s = Stack()
