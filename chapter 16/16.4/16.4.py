
# 0: move row by row
# 1: move columb by column
# 2: move diagonal down by diagonal down
# 3: move diagonal up by diagonal up

def first_dim(opt, N):
    if opt in [0, 1]:
        return N
    if opt in [2, 3]:
        return 2*N - 1   

def second_dim(opt, N, i):
    if opt in [0, 1]:
        return N
    if opt in [2, 3]:
        return N - abs(i + 1 - N)

def indexes(opt, N, i, j):
    if opt == 0:
        return i, j
    if opt == 1:
        return j, i
    if opt == 2:
        return min(N-1, i)-j, max(0, i-(N-1))+j
    if opt == 3:
        return (N-1)-min(N-1, i)+j, max(0, i-(N-1))+j

def tic_tac_win(board):
    N = len(board)
    
    for opt in [0, 1, 2, 3]:
        for i in range(first_dim(opt, N)):
            counter = 0
            current_player = 0
            for j in range(second_dim(opt, N, i)):
                x, y = indexes(opt, N, i, j)
                value = board[x][y]
                if value != current_player:
                    counter = 0
                    current_player = value
                    
                if value != 0:
                    counter += 1
                    if counter == 3:
                        return current_player
    
    
board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0]
]

print(tic_tac_win(board))
