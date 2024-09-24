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

    def addonsingle(self,list2):
        l1 = self.head
        l2 = list2.head
        result = []
        while l1 is not None:
            result.append(l1.value)
            l1 = l1.next
        while l2 is not None:
            result.append(l2.value)
            l2 = l2.next
        return sum(result)

    def addonwhole(self,list2):
        l1 = self.head
        l2 = list2.head
        result = []
        result2 = []
        while l1 is not None:
            result.append(l1.value)
            l1 = l1.next
        while l2 is not None:
            result2.append(l2.value)
            l2 = l2.next
        t1 = int(''.join(map(str,result)))
        t2 = int(''.join(map(str,result2)))
        return t1+t2

n1 = Linked()
n = int(input("list 1 ->"))
for i in range(n):
    lists1 = int(input("no list -"))
    n1.append(lists1)
n2 = Linked()
no2 = int(input("List 2 ->"))
for i in range(no2):
    lists2 = int(input("no List2"))
    n2.append(lists2)

print(n1.addonsingle(n2))
print(n1.addonwhole(n2))