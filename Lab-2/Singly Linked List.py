# Lab 2
# Task 1 (i)

class Node:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt


# Task 1 (ii)
class MyList:

    def __init__(self, arr=None):

        # Task 2 (1.a)
        if arr is None:
            self.head = None
            print("Empty list created")

        # Task 2 (1.b)
        elif isinstance(arr, list):
            self.head = None
            tail = None
            for i in arr:
                node = Node(i, None)
                if self.head is None:
                    self.head = node
                    tail = node
                else:
                    tail.next = node
                    tail = node

        # Task 2 (1.c)
        elif isinstance(arr, MyList):
            self.head = None
            tail = None
            node = arr.head
            while node is not None:
                new_node = Node(node.value, None)
                if self.head is None:
                    self.head = new_node
                    tail = new_node
                else:
                    tail.next = new_node
                    tail = new_node
                node = node.next
        else:
            print("Wrong datatype passed in the constructor. An empty MyList created")

    # Task 2 (2)
    def showList(self):
        node = self.head
        if self.head is None:
            print("Empty list")
        else:
            while node is not None:
                print(node.value, end=" ")
                node = node.next
        print()

    # Essential
    def show(self):
        node = self.head
        if self.head is None:
            print("Empty list")
        else:
            while node is not None:
                print(node.value, end="->")
                node = node.next
        print()

    # Task 2 (3)
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # Task 2 (4)
    def clear(self):
        if self.head is not None:
            self.head = None

    # Task 2 (5)
    def insert(self, newElement):
        node = self.head
        while node is not None:
            if node.value == newElement:
                print("The key already exists")
                break
            node = node.next
        new_node = Node(newElement, None)
        if self.head is None:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node

    # Task 2 (6)
    def insertAtIndex(self, newElement, index):
        if index < 0:
            print("Invalid index")
        i = 0
        node = self.head
        while node is not None:
            if node.value == newElement:
                print("The key already exists")
                break
            if i == index:
                node.value = newElement
            i += 1
            node = node.next

    # Essential
    def nodeAt(self, index):
        if index < 0:
            return None
        node = self.head
        for i in range(0, index):
            node = node.next
        return node

    # Task 2 (7)
    def remove(self, deleteKey):
        i = 0
        node = self.head
        while node is not None:
            if i == deleteKey:
                print(node.value, 'is removed')
                node.value = None
                if deleteKey == 0:
                    node.next = self.head
                else:
                    prev_node = self.nodeAt(deleteKey - 1)
                    prev_node.next = node.next
            i += 1
            node = node.next

    # Task 3 (1)
    def even(self):
        node = self.head
        evens = []
        i = 0
        while node is not None:
            if node.value % 2 == 0:
                evens.append(node.value)
            node = node.next
            i += 1
        new_list = MyList(evens)
        return new_list.show()

    # Task 3 (2)
    def isThere(self, element):
        node = self.head
        there = False
        while node is not None:
            if node.value == element:
                there = True
            node = node.next
        return there

    # Task 3 (3)
    def reverse(self):
        prev_node = None
        node = self.head
        while node is not None:
            nxt_node = node.next
            node.next = prev_node
            prev_node = node
            node = nxt_node
        self.head = prev_node

    # Task 3 (4)
    def sorting(self):
        i_node = self.head
        while i_node is not None:
            j_node = i_node.next
            while j_node is not None:
                if i_node.value > j_node.value:
                    temp = i_node.value
                    i_node.value = j_node.value
                    j_node.value = temp
                j_node = j_node.next
            i_node = i_node.next

    # Task 3 (5)
    def summation(self):
        node = self.head
        s = 0
        while node is not None:
            s += node.value
            node = node.next
        print(s)

    # Task 3 (6)
    def rotating(self, direction, k):
        if direction == 'left':
            for i in range(k):
                old_head = self.head
                self.head = self.head.next
                tail = self.head
                while tail.next:
                    tail = tail.next
                tail.next = old_head
                old_head.next = None
        if direction == 'right':
            for i in range(k):
                old_head = self.head
                self.head = self.head.next
                tail = self.head
                pre_tail = None
                while tail.next is not None:
                    pre_tail = tail
                    tail = tail.next
                tail.next = old_head
                new_tail = pre_tail
                new_tail.next = None
                self.head = tail


lst = MyList()
lst1 = MyList([5, 6, 7, 8])
lst2 = MyList(lst1)

lst.showList()
lst1.showList()
lst2.showList()

print(lst1.isEmpty())

lst2.clear()
lst2.showList()

lst1.insert(10)
lst1.showList()

lst1.insertAtIndex(9, 3)
lst1.showList()

lst1.remove(2)
lst1.showList()

lst3 = MyList([1, 2, 5, 3, 8])
lst3.even()

lst4 = MyList([101, 120, 25, 91, 87, 1])
print(lst3.isThere(7))
print(lst4.isThere(87))

lst3.reverse()
lst3.show()

lst3 = MyList([10, 6, 9, 5])
lst3.sorting()
lst3.show()

lst3.summation()

lst5 = MyList([3, 2, 5, 1, 8])
lst5.rotating('left', 2)
lst5.show()

lst6 = MyList([3, 2, 5, 1, 8])
lst6.rotating('right', 2)
lst6.show()
