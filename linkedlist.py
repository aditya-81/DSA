class Node:
    def __init__(self,value = None, next = None):
        self.value = value
        self.next = next

class LL:
    def __init__(self):
        self.head =None

    def insert(self):
        pos= 2
        first = self.head
        for _ in range(pos-1):
            first = first.next
        n4 = Node(6)
        n4.next = first.next
        first.next = n4
        list  = first
    def transvese(self):
        first = self.head
        while(first!=None):
            print(f"{first.value}->" ,end="")
            first = first.next
        print()

n1 = Node(1)
n2 = Node(4)
n3 =Node(3)

list = LL()
list.head = n1

n1.next = n2

list.transvese()
list.insert()
list.transvese()