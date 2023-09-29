# Parenthesis Balancing
# Implementation of linked list using stack

class StackUnderflow(Exception):
    pass


class Node:
    def __init__(self, val, nxt=None):
        self.value = val
        self.next = nxt


class StackList:    # Singly Linked List
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def push(self, obj):
        if self.head is None:
            self.head = Node(obj)
        else:
            new_node = Node(obj)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.empty():
            raise StackUnderflow('Stack Underflow')
        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            return pop_node.value

    def peek(self):
        if self.empty():
            raise StackUnderflow('Stack Underflow')
        else:
            return self.head.value

    def parenthesis(self, exp):
        openers = ['(', '{', '[']
        closers = [')', '{', ']']
        for i in exp:
            if i in openers:
                self.push(i)
            elif i in closers:
                if self.empty():
                    self.push(i)  # Just for making the stack non-empty
                    idx = [a for a in range(len(exp)) if exp[a] == i]
                    print('This expression is NOT correct.')
                    print("Error at character #", idx[0] + 1, ".'", i, "'- not opened.")
                    break
                else:
                    x = self.pop()
                    if (x == '(' and i != ')') or (x == '{' and i != '}') or (x == '[' and i != ']'):
                        idx = [a for a in range(len(exp)) if exp[a] == x]
                        print('This expression is NOT correct.')
                        print("Error at character #", idx[0] + 1, ".'", x, "'- not closed.")
                        break
        if self.empty():
            print('This expression is correct.')


# ------------------------------------------------------------------------------------------------------------------

expression1 = '1+2*(3/4)'
exp1 = StackList()
exp1.parenthesis(expression1)

expression2 = '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
exp2 = StackList()
exp2.parenthesis(expression2)

expression3 = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
exp3 = StackList()
exp3.parenthesis(expression3)
