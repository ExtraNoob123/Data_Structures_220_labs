# Lab 3

# Task 1 (i)
class Node:
    def __init__(self, value, nxt, prv):
        self.value = value
        self.next = nxt
        self.prev = prv


# Essential function
def nodeRemover(n):
    n.prev.next = n.next
    n.next.prev = n.prev
    n.next = None
    n.value = None
    n.prev = None


# Task 1 (ii)
class DoublyList:
    def __init__(self, arr=None):
        # Task 2 (1)
        if arr is not None and isinstance(arr, list):
            head = Node(None, None, None)
            self.head = head
            tail = self.head
            new_arr = []
            for i in arr:
                if i not in new_arr:
                    new_arr.append(i)
                    new_node = Node(i, None, None)
                    tail.next = new_node
                    new_node.prev = tail
                    tail = tail.next
                tail.next = head
                head.prev = tail

    # Task 2 (2)
    def showList(self):
        head = self.head
        node = self.head.next
        if node is None:
            print('Empty list')
        else:
            print('x', end=' ')
            while node is not head:
                print(node.value, end=' ')
                node = node.next
            print()

    # Task 2 (3)
    def insert(self, newElement):
        head = self.head
        tail = self.head.prev
        node = head.next
        while node is not head:
            if node.value == newElement:
                print('This element already exists')
                break
            node = node.next
        if node.value != newElement:
            new_node = Node(newElement, None, None)
            tail.next = new_node
            new_node.prev = tail
            tail = new_node
            tail.next = head
            head.prev = new_node

    # Task 2 (4)
    def insertAt(self, newElement, index):
        if index < 0:
            print('Invalid index')
        head = self.head
        if head.next is None:
            print('The array is empty')
        else:
            i = 0
            node = head.next
            while node is not head:
                if node.value == newElement:
                    print('This element already exists')
                    break
                elif i == index:
                    node.value = newElement
                i += 1
                node = node.next

    # Task 2 (5)
    def removeNode(self, index):
        head = self.head
        node = head.next
        if node is None:
            print('The array is empty')
        else:
            i = 0
            while node is not head:
                if i == index:
                    nodeRemover(node)
                    break
                i += 1
                node = node.next

    # Task 2 (6)
    def removeKey(self, deleteKey):
        head = self.head
        node = head.next
        if node is None:
            print('The array is empty')
        else:
            while node is not head:
                if node.value == deleteKey:
                    print(node.value, 'is deleted')
                    nodeRemover(node)
                    break
                node = node.next


lst = DoublyList([5, 6, 7, 8, 9, 10])
lst.showList()

lst.insert(11)
lst.showList()

lst.insertAt(12, 6)
lst.showList()

lst.removeNode(6)
lst.showList()

lst.removeKey(5)
lst.showList()
