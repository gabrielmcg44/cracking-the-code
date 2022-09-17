grid = [
    [0 , 1, 0, 0, 0],
    [0 , 1, 0, 0, 0],
    [0 , 0, 0, 0, 0],
    [0 , 1, 1, 0, 1],
    [0 , 0, 1, 0, 0]
]

def find_path(grid):
    rows = len(grid)
    columns = len(grid[0])
    
    if grid[0][0] == 1 or grid[rows-1][columns-1] == 1:
        return -1
    
    if rows == columns and rows == 1: # erro: coloquei 0 no lugar de 1
        return ["ARRIVED"]
    
    reverse_path = find_reverse_path(grid, rows, columns)
    return -1 if reverse_path == -1 else reverse_path[::-1] # erro: tentei usar reverse(reverse_path) 
    

reverse_paths = {}
def memo_paths(key, value): # lacuna: faltou a memoização
    if key not in reverse_paths.keys():
        reverse_paths[key] = value
    
    return reverse_paths[key]


def find_reverse_path(grid, rows, columns, start=[0,0]):
    if start[0] >= rows or start[1] >= columns or grid[start[0]][start[1]] == 1: # erro: faltaram as duas primeiras verificações
        return -1
        
    if start == [rows-1, columns-1]:
        return ["ARRIVED"]
           
    path_right = find_reverse_path(grid, rows, columns, [start[0], start[1]+1])
    if path_right != -1:
        path_right.append("RIGHT") # erro: tinha tentado retornar isso
        return path_right 

    path_down = find_reverse_path(grid, rows, columns, [start[0]+1, start[1]]) 
    
    if path_down != -1:
        path_down.append("DOWN") # erro: tinha tentado retornar isso
        return path_down
         
    return memo_paths(str(start), -1)


print(find_path(grid))