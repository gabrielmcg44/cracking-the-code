class Node:
    def __init__(self, key, next_node=None, previous=None, num_used=0):
        self.keys = {key}
        self.next_node = next_node
        self.previous_node = previous
        self.num_used = num_used


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.curr_size = 0
        self.values_dict = {}
        self.linked_list = None

    def insert(self, key, value):
        if key in self.values_dict.keys():
            return

        if len(self.values_dict.keys()) == 0:
            self.linked_list = Node(key)
        elif len(self.values_dict.keys()) < self.max_size:
            if self.linked_list.num_used == 0:
                self.linked_list.keys.add(key)
            else:
                self.linked_list = Node(key, self.linked_list)
                self.linked_list.next_node.previous_node = self.linked_list
        else:
            removed_key = self.linked_list.keys.pop()
            self.values_dict.pop(removed_key)
            if self.linked_list.num_used == 0:
                self.linked_list.keys.add(key)
            else:
                self.linked_list = Node(key, self.linked_list)

        self.values_dict[key] = {
            "value": value,
            "node": self.linked_list
        }

    def retrieve(self, key):
        if key not in self.values_dict.keys():
            return None

        self.values_dict[key]["node"].keys.remove(key)
        curr_node = previous_node = self.values_dict[key]["node"]

        new_num_used = curr_node.num_used + 1
        while curr_node.next_node is not None and curr_node.next_node.num_used <= new_num_used:
            curr_node = curr_node.next_node

        if curr_node.num_used == new_num_used:
            curr_node.keys.add(key)
            self.values_dict[key]["node"] = curr_node
        elif curr_node.next_node is None:
            curr_node.next_node = Node(key, None, curr_node, new_num_used)
            self.values_dict[key]["node"] = curr_node.next_node
        else:
            aux = curr_node.next_node
            curr_node.next_node = Node(key, aux, curr_node, new_num_used)
            aux.previous_node = curr_node.next_node
            self.values_dict[key]["node"] = curr_node.next_node

        if len(previous_node.keys) == 0:
            if previous_node.previous_node is None:
                self.linked_list = self.linked_list.next_node
                self.linked_list.previous_node = None
            else:
                previous_node.previous_node.next_node = previous_node.next_node
                previous_node.next_node.previous_node = previous_node.previous_node

        return self.values_dict[key]["value"]

    def print_cache_summary(self):
        print("Values Dict:")
        print(self.values_dict, "\n")
        curr_node = self.linked_list
        while curr_node is not None:
            print(
                "keys:", curr_node.keys,
                "num_used", curr_node.num_used,
                "previous_node", curr_node.previous_node,
                "next_node", curr_node.next_node
            )
            curr_node = curr_node.next_node
        print("\n\n")


lru = LRUCache(5)
lru.insert("a", 1)
lru.print_cache_summary()
lru.insert("b", 2)
lru.print_cache_summary()
lru.retrieve("b")
lru.print_cache_summary()
lru.retrieve("a")
lru.print_cache_summary()
lru.retrieve("a")
lru.print_cache_summary()
lru.retrieve("a")
lru.print_cache_summary()
lru.retrieve("b")
lru.print_cache_summary()
lru.insert("c", 3)
lru.print_cache_summary()
lru.retrieve("c")
lru.print_cache_summary()
lru.retrieve("c")
lru.print_cache_summary()
lru.retrieve("c")
lru.print_cache_summary()
lru.retrieve("c")
lru.print_cache_summary()
lru.retrieve("c")
lru.print_cache_summary()
lru.insert("d", 4)
lru.print_cache_summary()
lru.insert("e", 5)
lru.print_cache_summary()
lru.retrieve("e")
lru.print_cache_summary()
lru.retrieve("e")
lru.print_cache_summary()
lru.insert("f", 6)
lru.print_cache_summary()
lru.retrieve("f")
lru.print_cache_summary()
lru.retrieve("f")
lru.print_cache_summary()
lru.retrieve("f")
lru.print_cache_summary()
lru.insert("g", 7)
