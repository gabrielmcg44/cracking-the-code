
import time


def black_edges(matrix, top_left, side):
    return all([
        all([matrix[top_left[0]][top_left[1]+i] == 1 for i in range(side)]),
        all([matrix[top_left[0]+i][top_left[1]] == 1 for i in range(side)]),
        all([matrix[top_left[0]+side-1][top_left[1]+i] == 1 for i in range(side)]),
        all([matrix[top_left[0]+i][top_left[1]+side-1] == 1 for i in range(side)])
    ])


def get_indexes(edge, top_left, side, i):
    if edge == 0:
        return top_left[0], top_left[1]+i
    elif edge == 1:
        return top_left[0]+side-1, top_left[1]+i
    elif edge == 2:
        return top_left[0]+i, top_left[1]
    elif edge == 3:
        return top_left[0]+i, top_left[1]+side-1


def get_top(edge, x, y, side):
    if edge == 0:
        return x, y-side+1
    elif edge == 1:
        return x-side+1, y-side+1
    elif edge == 2:
        return x-side+1, y
    elif edge == 3:
        return x-side+1, y-side+1


def max_black_square(matrix, top_left=None, side=None, memo=None):
    if top_left is None:
        memo = {}
        top_left = [0, 0]
        side = len(matrix)

    if side <= 0:
        return [[], 0]

    key = str(top_left[0]) + "," + str(top_left[1]) + "," + str(side)
    if key in memo.keys():
        return memo[key]

    if black_edges(matrix, top_left, side):
        memo[key] = [top_left, side]
        return memo[key]

    edge_max = [[], 0]

    for edge in [0, 1, 2, 3]:
        last_black = None
        for i in range(side+1):
            x, y = get_indexes(edge, top_left, side, i)
            pixel = 0 if i == side else matrix[x][y]
            if pixel == 1:
                if last_black is None:
                    last_black = i

            elif last_black is not None:
                for idx1 in range(last_black, i):
                    for idx2 in range(idx1, i):
                        if idx1 == 0 and idx2 == side - 1:
                            continue
                        curr_side = idx2-idx1+1
                        x, y = get_indexes(edge, top_left, side, idx2)
                        topx, topy = get_top(edge, x, y, curr_side)
                        square = max_black_square(matrix, [topx, topy], curr_side, memo)
                        if square[1] > edge_max[1]:
                            edge_max = square

                last_black = None

    if edge_max[1] == side - 1:
        return edge_max

    internal_max = max_black_square(matrix, [top_left[0] + 1, top_left[1] + 1], side - 2, memo)

    return edge_max if edge_max[1] >= internal_max[1] else internal_max


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