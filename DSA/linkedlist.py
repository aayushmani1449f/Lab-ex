class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_start(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def insert_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head

def insert_at(self, data, pos):
    new_node = Node(data)

    curr = head
    for i in range(pos - 1):
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node

    return head


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

head = n1

head = insert_start(head, 4)
head = insert_end(head, 8)
head = insert_at(head, 9, 3)

current = head

while current is not None:
    print(current.data)
    current = current.next