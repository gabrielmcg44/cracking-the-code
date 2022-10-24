

def sparse_similarity(documents_list):
    docs_containing = {}
    for i in range(len(documents_list)):
        for value in documents_list[i]:
            if value not in docs_containing.keys():
                docs_containing[value] = []
            
            docs_containing[value].append(i)

    documents_intersection = {}
    for value in docs_containing.keys():
        num_docs = len(docs_containing[value])
        for i in range(num_docs):
            for j in range(i+1, num_docs):
                key = ",".join(sorted([str(docs_containing[value][i]), str(docs_containing[value][j])]))
                if key not in documents_intersection.keys():
                    documents_intersection[key] = 0
                documents_intersection[key] += 1
                
    for key in documents_intersection:
        docs = key.split(",")
        intersection = documents_intersection[key]
        union = len(documents_list[int(docs[0])]) + len(documents_list[int(docs[1])])
        similarity = intersection / (union - intersection)
        print(key, similarity)
                

documents = [
    {14, 15, 100, 9, 3},
    {32, 1, 9, 3, 5},
    {15, 29, 2, 6, 8, 7},
    {7, 10}
]

print(sparse_similarity(documents))