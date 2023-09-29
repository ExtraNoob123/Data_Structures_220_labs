# Parenthesis Balancing
# Implementation of array using stack

class StackUnderflow(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return self.stack == []

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if self.empty():
            raise StackUnderflow('Stack Underflow')
        return self.stack.pop()

    def peek(self):
        if self.empty():
            raise StackUnderflow('Stack Underflow')
        return self.stack[-1]

    def parenthesis(self, exp):
        openers = ['(', '{', '[']
        closers = [')', '{', ']']
        for i in exp:
            if i in openers:
                self.push(i)
            elif i in closers:
                if self.empty():
                    self.push(i)    # Just for making the stack non-empty
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
exp1 = Stack()
exp1.parenthesis(expression1)

expression2 = '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
exp2 = Stack()
exp2.parenthesis(expression2)

expression3 = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
exp3 = Stack()
exp3.parenthesis(expression3)
