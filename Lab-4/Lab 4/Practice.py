class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev=None
class DoublyList:
    #1
    def __init__(self,a=None):
        if a!=None:
            if isinstance(a,list):
                head= Node(None,None,None)
                self.head = head
                tail= self.head
                unq=[]
                for i in a:
                    if i not in unq:
                        unq=unq+[i]
                        newNode=Node(i,None,None)
                        tail.next = newNode
                        newNode.prev = tail
                        tail = tail.next
                    tail.next=head
                    head.prev=tail

            if isinstance(a, DoublyList):
                head = Node(None, None, None)
                self.head = head
                tail = self.head
                unq = []
                for i in a:
                    if i not in unq:
                        unq = unq + [i]
                        newNode = Node(i, None, None)
                        tail.next = newNode
                        newNode.prev = tail
                        tail = tail.next
                    tail.next = head
                    head.prev = tail
        else:
            print("Wrong input. The given array is empty!")

    #2
    def showList(self):
        head = self.head
        n = self.head.next
        if self.head.next==None:
            print("Empty List")
        else:
            n = self.head.next
            while n != self.head:
                print(n.data, end=" ")
                n = n.next
            print()

    def empty(self):
        return self.head.next is None

    def enqueue(self, newElement):
        head = self.head
        tail = self.head.prev
        if tail.data == newElement:
            print("This element already exists.")

        else:
            newNode = Node(newElement, None, None)
            tail.next = None
            tail.next = newNode
            newNode.prev = tail
            tail = newNode
        tail.next = head
        head.prev = None
        head.prev = newNode

    def dequeue(self):
        dq = self.head.next
        self.head.next = self.head.next.next
        dq.next = None
        dq.prev=None
        if self.head.next is None:
            self.head = None
    def peek(self):
        n=self.head.next
        print(n.data)

list1=[10,20,30,40]
lst=DoublyList(list1)
lst.showList()
lst.enqueue(50)
lst.showList()
lst.dequeue()
lst.showList()
lst.peek()