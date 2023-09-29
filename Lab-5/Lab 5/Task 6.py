# Task 6
# Adding all elements of a SLL

class Node:
    def __init__(self, val, nxt=None):
        self.value = val
        self.next = nxt


def formation(ar):
    head = None
    tail = None
    for i in ar:
        node = Node(i)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

def addition(head):
    s = 0
    if head is None:
        return
    else:
        addition(head.next)
        s += head.value
