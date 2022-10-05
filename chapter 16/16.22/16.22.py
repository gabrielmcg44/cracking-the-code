
import matplotlib.pyplot as plt


def print_k_moves(K):
    pos = [0, 0]
    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    curr_direction_index = 0
    board_spaces = {}

    steps = 0
    while steps < K:
        key = str(pos[0]) + "," + str(pos[1])
        if key not in board_spaces.keys():
            board_spaces[key] = 1

        curr_direction_index = (curr_direction_index + board_spaces[key]) % 4
        board_spaces[key] *= -1

        pos = [pos[i] + directions[curr_direction_index][i] for i in range(2)]

        min_x = min(min_x, pos[0])
        max_x = max(max_x, pos[0])
        min_y = min(min_y, pos[1])
        max_y = max(max_y, pos[1])

        steps += 1

    M, N = max_x - min_x + 1, max_y - min_y + 1
    X = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            key = str(j + min_x) + "," + str(N-1-i+min_y)
            X[i][j] = -1
            if key in board_spaces.keys():
                X[i][j] *= board_spaces[key]

    plt.imshow(X, cmap='Greys')
    plt.show()


print_k_moves(11000)

