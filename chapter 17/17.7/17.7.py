
def label_names(graph, label, start_name, real_names):
    if start_name not in real_names.keys():
        real_names[start_name] = label

        for synonym in graph[start_name]:
            label_names(graph, label, synonym, real_names)


def get_real_names(graph):
    real_names = {}

    for name in graph.keys():
        if name not in real_names.keys():
            label_names(graph, name, name, real_names)

    return real_names


class SynonymsGraph:
    def __init__(self, synonyms):
        self.nodes = {}
        for synonym in synonyms:
            if synonym[0] not in self.nodes.keys():
                self.nodes[synonym[0]] = set([])
            if synonym[1] not in self.nodes.keys():
                self.nodes[synonym[1]] = set([])

            self.nodes[synonym[0]].add(synonym[1])
            self.nodes[synonym[1]].add(synonym[0])


def real_frequencies(names, synonyms):
    names_graph = SynonymsGraph(synonyms)

    real_names = get_real_names(names_graph.nodes)
    print(real_names)
    real_frequencies_dict = {}
    for name in names:
        real_name = name[0] if name[0] not in real_names.keys() else real_names[name[0]]
        if real_name not in real_frequencies_dict.keys():
            real_frequencies_dict[real_name] = 0

        real_frequencies_dict[real_name] += name[1]

    return [[key, real_frequencies_dict[key]] for key in real_frequencies_dict.keys()]


names = [["John", 15], ["Jon", 12], ["Johnny", 3], ["Johnnie", 10], ["Chris", 13], ["Kris", 4], ["Christopher", 19]]
synonyms = [["Jon", "John"], ["Johnny", "Johnie"], ["John", "Johnny"],
            ["Jonn", "Johnn"], ["Johnnny", "Johnnie"], ["Johnn", "Johnnny"],
            ["Jon", "Jonn"],
            ["Chris", "Kris"], ["Chris", "Christopher"]]

print(real_frequencies(names, synonyms))
