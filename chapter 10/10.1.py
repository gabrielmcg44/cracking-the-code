
import sys


def merge_insert_array(a, b):
    index_a = 0
    index_b = 0
    size_b = len(b)
    aux = []
    index_aux = 0
    
    while index_b < size_b:
        aux_value = sys.float_info.max if index_aux == len(aux) else aux[index_aux]
        a_value = sys.float_info.max if a[index_a] is None else a[index_a]
        b_value = B[index_b]
        
        min_value = min([a_value, b_value, aux_value])
        
        if aux_value == min_value:
            if a[index_a] is not None:
                aux.append(a[index_a])
                
            a[index_a] = aux_value
            
            index_aux += 1
        elif b_value == min_value:
            if a[index_a] is not None:
                aux.append(a[index_a])
                
            a[index_a] = b_value
            index_b += 1
        
        index_a += 1
            
    while index_aux != len(aux):
        a[index_a] = aux[index_aux]
        index_aux += 1
        index_a += 1  

A = [1, 6, 7, 8, 8, 8, 12, 25, 27, None, None, None, None]

B = [3, 7, 5, 13]

merge_insert_array(A, B)

print(A)