import sys


def max_submatrix(matrix):
    side = len(matrix)
    aux_sum = matrix
    for i in range(side):
        cum_sum = 0
        for j in range(side):
            cum_sum += matrix[i][j]
            aux_sum[i][j] = cum_sum

    general_max_sum, top_left, bottom_right = -sys.float_info.max, None, None
    for i in range(side):
        for j in range(i, side):
            max_sum, max_start, max_end = - sys.float_info.max, None, None
            start_row = 0
            cum_sum = 0
            for k in range(side):
                start_sum = 0 if i == 0 else aux_sum[k][i - 1]
                end_sum = aux_sum[k][j]
                line_sum = end_sum - start_sum
                cum_sum += line_sum
                if cum_sum > max_sum:
                    max_sum = cum_sum
                    max_start = start_row
                    max_end = k

                if cum_sum <= 0:
                    cum_sum = 0
                    start_row = k + 1

            if max_sum > general_max_sum:
                general_max_sum = max_sum
                top_left = [max_start, i]
                bottom_right = [max_end, j]

    return general_max_sum, top_left, bottom_right


matrix = [
    [0, 0, 2, -1, -3],
    [0, -1, 4, 4, -2],
    [7, -8, 0, 5, -1],
    [3, -2, 1, -3, 0],
    [1, 4, -2, 5, -3],
]

print(max_submatrix((matrix)))
