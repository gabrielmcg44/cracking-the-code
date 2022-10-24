
dictionary = ["damp", "lamp", "aacc", "camp", "lame", "lane", "limp", "lime", "aabb", "like", "luke", "puke", "pume", "tume", "tune", "love", "lite", "lune", "lust", "love", "dove", "move", "wolf",
              "long", "moon", "hunt", "fill", "bill", "beautiful", "somebody", "accc", "cccc", "cccb", "ccbb", "cabb", "altruist", "palindrome", "mike", "mire", "fire"]


def create_neighbors(dictionary, num_letters):
    graph = {}
    sub_dict = [word for word in dictionary if len(word) == num_letters]
    for word in sub_dict:
        for i in range(num_letters):
            letter = word[i]
            expression = word[:i] + "_" + word[i+1:]
            if expression not in graph.keys():
                graph[expression] = []

            graph[expression].append(letter)

    return graph


def create_nodes(dictionary, num_letters):
    nodes = {}
    sub_dict = [word for word in dictionary if len(word) == num_letters]
    for word in sub_dict:
        nodes[word] = {
            "visited": [False, False],
            "in_queue": [False, False],
            "previous": [None, None]
        }

    return nodes


class Graph:
    def __init__(self, dictionary, num_letters):
        self.neighbors = create_neighbors(dictionary, num_letters)
        self.nodes = create_nodes(dictionary, num_letters)

    def get_neighbors(self, word):
        neighbors = []
        for i in range(len(word)):
            letter = word[i]
            expression = word[:i] + "_" + word[i+1:]
            for l in self.neighbors[expression]:
                if l != letter:
                    neighbors.append(word[:i] + l + word[i+1:])

        return neighbors

    def print_path(self, word1, word2):
        queues = [[word1], [word2]]
        idx = [0, 0]
        curr = 0

        while True:
            if idx[curr] >= len(queues[curr]):
                return

            curr_word = queues[curr][idx[curr]]
            self.nodes[curr_word]["visited"][curr] = True
            if all(self.nodes[curr_word]["visited"]):
                break

            curr_neighbors = self.get_neighbors(curr_word)
            not_added = [neighbor for neighbor in curr_neighbors if not self.nodes[neighbor]["in_queue"][curr]]
            queues[curr].extend(not_added)
            for word in not_added:
                self.nodes[word]["in_queue"][curr] = True
                self.nodes[word]["previous"][curr] = curr_word

            idx[curr] += 1
            curr = (curr + 1) % 2

        match = queues[curr][idx[curr]]
        path1 = []

        curr_word = match
        while curr_word != word1:
            path1.append(curr_word)
            curr_word = self.nodes[curr_word]["previous"][0]

        path1.reverse()

        path2 = []
        curr_word = match
        while curr_word != word2:
            path2.append(curr_word)
            curr_word = self.nodes[curr_word]["previous"][1]

        path = [word1] + path1[:-1] + path2 + [word2]
        print(path)

        used_words = queues[0] + queues[1]

        for word in used_words:
            self.nodes[word] = {
                "visited": [False, False],
                "in_queue": [False, False],
                "previous": [None, None]
            }


graph = Graph(dictionary, 4)
graph.print_path("aacc", "aabb")
graph.print_path("damp", "like")
