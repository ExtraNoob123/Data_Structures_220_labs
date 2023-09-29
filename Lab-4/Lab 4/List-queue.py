class Node:
    def __init__(self, val, nxt=None):
        self.value = val
        self.next = nxt


class ListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def empty(self):
        return self.front is None

    def enqueue(self, element):
        nq = Node(element)
        if self.rear is None:
            self.front = nq
            self.rear = nq
        else:
            self.rear.next = nq
            self.rear = nq

    def dequeue(self):
        dq = self.front
        self.front = self.front.next
        dq.next = None
        if self.front is None:
            self.rear = None

    def peek(self):
        return self.front.value

