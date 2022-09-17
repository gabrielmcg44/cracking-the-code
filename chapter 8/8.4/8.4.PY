
def subsets(A):
    subsets = []
    subsets_write(A, subsets)
    return subsets

def subsets_write(A, subsets_list):
    if len(A) == 0:
        subsets_list.append(A)
    else:
        first = A[0]
        subsets_write(A[1:] if len(A) > 1 else [], subsets_list)
        subsets_with_first = [[i for i in subset] for subset in subsets_list] # erro: REFERÊNCIAAA
        
        for subset in subsets_with_first:
            subset.append(first)
        
        subsets_list.extend(subsets_with_first)
    
    
A = [1, 2, 3, 4, 5]
print(len(subsets(A)))