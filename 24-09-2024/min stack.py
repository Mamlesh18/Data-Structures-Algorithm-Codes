class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def append(self,val):
        self.stack.append(val)
        self.length+=1

    def remove(self):
        if self.stack:
            self.stack.pop()
            self.length-=1
        else:
            print('empty')

    def top(self):
        if self.stack:
            return self.stack[-1]

    def displaY(self):
        if self.stack:
            return self.stack

s = Stack()
s.append(1)
s.append(2)
s.append(3)
print(s.displaY())
s.remove()
s.top()
print(s.displaY())