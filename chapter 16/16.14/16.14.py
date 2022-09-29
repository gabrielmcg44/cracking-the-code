def get_line_key_from_points(point1, point2):
    if point1[0] == point2[0]:
        return str(point1[0])

    slope = (point1[1] - point2[1]) / (point1[0] - point2[0])
    slope = slope if slope != 0 else 0

    y_intercept = (point2[1] * point1[0] - point1[1] * point2[0]) / (point1[0] - point2[0])
    y_intercept = y_intercept if y_intercept != 0 else 0

    return str(slope) + "," + str(y_intercept)


def get_line_from_key(line_key):
    params = line_key.split(",")
    if len(params) == 1:
        return {"x_intercept": float(params[0])}

    return {
        "slope": float(params[0]),
        "y_intercept": float(params[1])
    }


def best_line(points):
    lines = {}
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j or (points[i][0] == points[j][0] and points[i][1] == points[j][1]):
                continue

            line_key = get_line_key_from_points(points[i], points[j])
            print(i, j, line_key)
            if line_key in lines.keys():
                lines[line_key] += 1
            else:
                lines[line_key] = 1

    print(lines)

    max_count, best_line_key = 0, None
    for line in lines.keys():
        if lines[line] > max_count:
            max_count, best_line_key = lines[line], line

    return get_line_from_key(best_line_key)


points = [
    [0, 1],
    [2, 3],
    [-1, -1],
    [-2, -2],
    [2, 4],
    [1, 6],
    [3, 3],
    [4, 4],
    [4, 6],
    [4, 0],
    [4, -1],
    [4, -2]
]

print(best_line(points))
