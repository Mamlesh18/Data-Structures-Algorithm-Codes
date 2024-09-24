class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,val):
        new = Node(val)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.length+=1

    def add
