import time


def max_black_square(matrix):
    side = len(matrix)
    zeros_right_below = [[[0, 0] for _ in range(side)] for _ in range(side)]
    for i in range(side):
        for j in range(side):
            x, y = side-1-i, side-1-j
            if matrix[x][y] == 1:
                zeros_right_below[x][y][0] = (0 if y+1 == side else zeros_right_below[x][y+1][0]) + 1
                zeros_right_below[x][y][1] = (0 if x+1 == side else zeros_right_below[x+1][y][1]) + 1

    for N in [side - i for i in range(side)]:
        for i in range(side - N + 1):
            for j in range(side - N + 1):
                if all([
                    zeros_right_below[i][j][0] >= N,
                    zeros_right_below[i][j][1] >= N,
                    zeros_right_below[i+N-1][j][0] >= N,
                    zeros_right_below[i][j+N-1][1] >= N
                ]):
                    return [[i, j], N]

    return None


bw_square = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start = time.time()
print(max_black_square(bw_square))
end = time.time()

print(end - start)
