class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lca(root, a, b):
    if not root:
        return None
    if root.val == a or root.val == b:
        return root
    l = lca(root.left, a, b)
    r = lca(root.right, a, b)
    if l and r:
        return root
    return l if l else r


root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

res = lca(root, "D", "E")
print(res.val)