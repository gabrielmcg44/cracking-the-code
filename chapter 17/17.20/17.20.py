class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.num_left = 0
        self.num_right = 0


def add_rec(root, value):
    if value > root.value:
        root.num_right += 1
        if root.right is None:
            root.right = Node(value)
        else:
            add_rec(root.right, value)
    elif value < root.value:
        root.num_left += 1
        if root.left is None:
            root.left = Node(value)
        else:
            add_rec(root.left, value)
    else:
        root.num_left += 1
        new_node = Node(value)
        new_node.left = root.left


class BST:
    def __init__(self):
        self.root = None

    def fix_median(self):
        if self.root.num_right - self.root.num_left > 1:
            right_root = self.root.right
            self.root.right = None
            self.root.num_right = 0
            curr = right_root
            while curr.left is not None:
                curr.num_left -= 1
                aux = curr.left
                if curr.num_left == 0:
                    curr.left = None

                curr = aux

            if curr is not right_root:
                num_add_nodes = right_root.num_right + 1
                aux_curr = curr
                while aux_curr.right is not None:
                    aux_curr.num_right += num_add_nodes
                    aux_curr = aux_curr.right

                aux_curr.right = right_root
                aux_curr.num_right += num_add_nodes

            curr.left = self.root
            curr.num_left = self.root.num_left + 1
            self.root = curr

        if self.root.num_right - self.root.num_left < -1:
            left_root = self.root.left
            self.root.left = None
            self.root.num_left = 0
            curr = left_root
            while curr.right is not None:
                curr.num_right -= 1
                aux = curr.right
                if curr.num_right == 0:
                    curr.right = None

                curr = aux

            if curr is not left_root:
                num_add_nodes = left_root.num_left + 1
                aux_curr = curr
                while aux_curr.left is not None:
                    aux_curr.num_left += num_add_nodes
                    aux_curr = aux_curr.left

                aux_curr.left = left_root
                aux_curr.num_left += num_add_nodes

            curr.right = self.root
            curr.num_right = self.root.num_right + 1
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

print(bst.root.right.value)
print(bst.root.left.left.left.left.left.left.right.value)