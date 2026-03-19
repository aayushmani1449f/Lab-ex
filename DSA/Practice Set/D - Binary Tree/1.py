class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root):
    if not root:
        return
    q = [root]
    while q:
        cur = q.pop(0)
        print(cur.val, end=" ")
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)


root = Node("CEO")
root.left = Node("CTO")
root.right = Node("CFO")
root.left.left = Node("Dev1")
root.left.right = Node("Dev2")

level_order(root)