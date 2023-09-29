class ArrayQueue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def empty(self):
        return self.queue == []

    def enqueue(self, obj):
        self.queue.append(obj)
        self.rear += 1

    def dequeue(self):
        dq = self.queue[self.front]
        self.queue = self.queue[self.front + 1: self.rear]
        self.rear -= 1
        return dq

    def peek(self):
        return self.queue[self.front]

