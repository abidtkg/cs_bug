class Node:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.val = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.previous = self.head
            self.tail = node
            self.size += 1

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in values)}]"


my_list = DoubleLinkedList()

my_list.add(10)
my_list.add(5)
my_list.add(7)

print(my_list)
