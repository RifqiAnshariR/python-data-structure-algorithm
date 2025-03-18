import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        if self.isEmpty():
            print("Priority queue is empty!")
        else:
            return heapq.heappop(self.elements)[0]

    def __str__(self):
        return str(self.elements)
    
pq = PriorityQueue()
