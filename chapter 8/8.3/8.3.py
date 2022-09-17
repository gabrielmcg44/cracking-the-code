import math

A = [-7, -6, -4, -2, 0, 3, 5, 7, 9, 10, 12, 13]
B = [-7, -6, -6, -6, -6, -6, -6, 8, 8, 10, 12, 13]

def magic_index(A, start=0, end=None):
    if end is None:
        end = len(A) - 1
        
    if A[start] == start:
        return start
    
    if A[start] > start or A[end] < end:
        return -1
    
    middle = math.floor((start + end)/2)
    
    left_magic_index = magic_index(A, start, middle)
    if left_magic_index != -1:
        return left_magic_index
        
    right_magic_index = magic_index(A, middle + 1, end)
    if right_magic_index != -1:
        return right_magic_index
        
    return -1
    

def magic_index_follow_up(A, start=0, end=None):
    if end is None:
        end = len(A) - 1
        
    if A[start] == start:
        return start
    
    if A[start] > end or A[end] < start:
        return -1
    
    middle = math.floor((start + end)/2)
    
    left_magic_index = magic_index(A, start, middle)
    if left_magic_index != -1:
        return left_magic_index
        
    right_magic_index = magic_index(A, middle + 1, end)
    if right_magic_index != -1:
        return right_magic_index
        
    return -1
    
print(magic_index(A))
print(magic_index_follow_up(B))