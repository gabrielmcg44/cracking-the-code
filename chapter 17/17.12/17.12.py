class BiNode:
    def __init__(self, data, node1=None, node2=None):
        self.data = data
        self.node1 = node1
        self.node2 = node2


# this function considers the case where there are repeated values on the bst
def bst_to_dll(root):
    if root is None:
        return None, None

    start_left, end_left = bst_to_dll(root.node1)
    start_right, end_right = bst_to_dll(root.node2)

    if root.node1 is not None and root.data == root.node1.data:
        if root.node1.node2 is not None:
            root.node2 = root.node1.node2
            root.node1.node2.node1 = root
            root.node1.node2 = root
            end_left.node2 = start_right
            if start_right is not None:
                start_right.node1 = end_left
        else:
            root.node2 = start_right
            root.node1.node2 = root
            if start_right is not None:
                start_right.node1 = root

    else:
        root.node1 = end_left
        if end_left is not None:
            end_left.node2 = root
        root.node2 = start_right
        if start_right is not None:
            start_right.node1 = root

    return start_left if start_left is not None else root, \
        end_right if end_right is not None else root


node1 = BiNode(1)
node3 = BiNode(3)
node21 = BiNode(2, node1, node3)
node4 = BiNode(4)
node6 = BiNode(6)
node5 = BiNode(5, node4, node6)
node22 = BiNode(2, node21, node5)
node81 = BiNode(8)
node9 = BiNode(9)
node82 = BiNode(8, node81, node9)
node11 = BiNode(11)
node13 = BiNode(13)
node12 = BiNode(12, node11, node13)
node10 = BiNode(10, node82, node12)
node7 = BiNode(7, node22, node10)

root = node7
print(root.node1.data)
start, end = bst_to_dll(root)
print(start.node2)
curr = start

while curr is not None:
    print(curr.data)
    curr = curr.node2
