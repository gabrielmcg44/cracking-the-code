def bisect_line(square_1, square_2):
    centroid_2 = [(square_1[0][0] + square_1[1][0]) / 2, (square_1[0][1] + square_1[1][1]) / 2]
    centroid_1 = [(square_2[0][0] + square_2[1][0]) / 2, (square_2[0][1] + square_2[1][1]) / 2]

    if centroid_1[0] == centroid_2[0] and centroid_1[1] == centroid_2[1]:
        return [[0, 0], centroid_1]

    return [centroid_1, centroid_2]


square1 = [[3, 4], [5, 6]]
square2 = [[10, 2], [13, 5]]

print(bisect_line(square1, square2))