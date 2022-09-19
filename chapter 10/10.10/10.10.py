
class Node:
    def __init__(self, value, num_ocurrences=0, left=None, num_left=0, right=None, num_right=0, parent=None):
        self.value = value
        self.num_ocurrences = num_ocurrences
        self.left = left
        self.num_left = num_left
        self.right = right
        self.num_right = num_right
        self.parent = parent
        
class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value, 1)
        
        # this dict is used to not insert duplicates, but increment the num of ocurrences O(log(n))
        self.values = {}
        self.values[self.root.value] = self.root
    
    def track(self, value):
        if value in self.values.keys():
            self.increment(value)
        else:
            self.insert(value)
    
    def increment(self, value):
        self.values[value].num_ocurrences += 1
        curr = self.values[value]
        while curr.parent is not None:
            left_child = curr.parent.left is not None and curr.parent.left.value == curr.value
            if left_child:
                curr.parent.num_left += 1
            else:
                curr.parent.num_right += 1
            curr = curr.parent
        
    def insert(self, value):
        curr = self.root
        inserted = False
        while not inserted:
            if curr.value < value and curr.right is None:
                curr.right = Node(value)
                curr.right.parent = curr
                self.values[value] = curr.right
                self.increment(value)
                inserted = True
            elif curr.value > value and curr.left is None:
                curr.left = Node(value)
                curr.left.parent = curr
                self.values[value] = curr.left
                self.increment(value)
                inserted = True
            elif curr.value < value:
                curr = curr.right
            elif curr.value > value:
                curr = curr.left

    def get_rank(self, value):
        if value not in self.values.keys():
            return -1
        
        curr = self.root
        rank = 0
        while curr.value != value:
            if value > curr.value:
                rank += curr.num_left + curr.num_ocurrences
                curr = curr.right
            else:
                curr = curr.left
        
        rank += curr.num_left + curr.num_ocurrences - 1
        return rank
        

tracker = Tree(5)
tracker.track(1)
tracker.track(4)
tracker.track(4)
tracker.track(5)
tracker.track(9)
tracker.track(7)
tracker.track(13)
tracker.track(3)

print(tracker.get_rank(13))
