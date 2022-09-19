import math

def find_element(matrix, value):
    M = len(matrix)
    N = len(matrix[0])
    
    left = 0
    right = M*N - 1
    mid = math.floor(right/2)
    
    while right >= left:
        i, j = math.floor(mid/N), mid % N
        print(value, matrix[i][j], left, mid, right)
        if value > matrix[i][j]:
            left = mid + 1
        elif value < matrix[i][j]:
            right = mid - 1
        else:
            return i, j
        
        mid = math.floor((left + right)/2)
    
    return -1
    
matrix = [
    [0, 4, 7, 11],
    [15, 16, 27, 38],
    [49, 57, 63, 75],
    [78, 83, 95, 99]
]

print(find_element(matrix, 97))