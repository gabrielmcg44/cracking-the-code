class Node:
    def __init__(self, value):
        self.value = value
        self.left_right = [None, None]
        self.num_left_right = [0, 0]


def add_rec(root, value):
    if value == root.value:
        root.num_left += 1
        new_node = Node(value)
        new_node.left = root.left
        return

    side = 1 if value > root.value else 0

    root.num_left_right[side] += 1
    if root.left_right[side] is None:
        root.left_right[side] = Node(value)
    else:
        add_rec(root.left_right[side], value)


class BST:
    def __init__(self):
        self.root = None

    def fix_median(self):
        branch, opposite = None, None
        if self.root.num_left_right[1] - self.root.num_left_right[0] > 1:
            branch, opposite = 1, 0
        elif self.root.num_left_right[1] - self.root.num_left_right[0] < -1:
            branch, opposite = 0, 1

        if branch is None:
            return

        branch_root = self.root.left_right[branch]
        self.root.left_right[branch] = None
        self.root.num_left_right[branch] = 0
        curr = branch_root
        while curr.left_right[opposite] is not None:
            curr.num_left_right[opposite] -= 1
            aux = curr.left_right[opposite]
            if curr.num_left_right[opposite] == 0:
                curr.left_right[opposite] = None

            curr = aux

        if curr is not branch_root:
            num_add_nodes = branch_root.num_left_right[branch] + 1
            aux_curr = curr
            while aux_curr.left_right[branch] is not None:
                aux_curr.num_left_right[branch] += num_add_nodes
                aux_curr = aux_curr.left_right[branch]

            aux_curr.left_right[branch] = branch_root
            aux_curr.num_left_right[branch] += num_add_nodes

        curr.left_right[opposite] = self.root
        curr.num_left_right[opposite] = self.root.num_left_right[opposite] + 1
        self.root = curr

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        add_rec(self.root, value)
        self.fix_median()


bst = BST()
bst.add(3)
print(bst.root.value)
bst.add(1)
print(bst.root.value)
bst.add(5)
print(bst.root.value)
bst.add(9)
print(bst.root.value)
bst.add(-2)
print(bst.root.value)
bst.add(4)
print(bst.root.value)
bst.add(10)
print(bst.root.value) # new median

bst.add(7)
print(bst.root.value)
bst.add(2)
print(bst.root.value)
bst.add(4.5)
print(bst.root.value)
bst.add(3.9)
print(bst.root.value)
bst.add(8)
print(bst.root.value)
bst.add(3.8)
print(bst.root.value)
bst.add(11)
print(bst.root.value)
bst.add(3.7)
print(bst.root.value)
bst.add(3.6)
print(bst.root.value)
bst.add(3.5)
print(bst.root.value)

print(bst.root.left_right[1].value)
print(bst.root.left_right[0].left_right[0].left_right[0].left_right[0].left_right[0].left_right[0].left_right[1].value)
