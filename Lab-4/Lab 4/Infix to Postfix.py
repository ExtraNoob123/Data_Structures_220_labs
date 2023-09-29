class Stack:
    stack = []
    pointer = -1

    def push(self, element):
        self.stack.append(element)
        self.pointer += 1

    def pop(self):
        val = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return val

    def peek(self):
        return self.stack[self.pointer]

    def isEmpty(self):
        if self.pointer == -1:
            return True


def postToin(string):
    s = Stack()
    operators = "+-/*()[]{}"
    for i in string:
        if i.isalpha() or i.isnumeric():
            s.push(i)
        elif i in operators:
            r = s.pop()
            if s.isEmpty():
                print(r)
                break
            else:
                l = s.pop()
                val = "(" + l + i + r + ")"
                s.push(val)
    flag = s.isEmpty()
    if flag != True:
        print(s.pop())


st = "A B C D E/-*+"
postToin(st)
