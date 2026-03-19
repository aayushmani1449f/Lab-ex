class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def vertical_order(root):
    d = {}
    q = [(root, 0)]
    while q:
        node, col = q.pop(0)
        if col not in d:
            d[col] = []
        d[col].append(node.val)
        if node.left:
            q.append((node.left, col - 1))
        if node.right:
            q.append((node.right, col + 1))
    for k in sorted(d):
        print(d[k])


root = Node(3)
root.left = Node(9)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(7)

vertical_order(root)