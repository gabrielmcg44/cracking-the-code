def measure_pond(i, j, land, visited, size=None):
    if size is None:
        size = [0]

    visited[i][j] = True
    size[0] += 1

    neighbors = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
    for neighbor in neighbors:
        x = i + neighbor[0]
        y = j + neighbor[1]
        if x < 0 or y < 0 or x >= len(land) or y >= len(land[0]):
            continue

        if land[x][y] == 0 and not visited[x][y]:
            measure_pond(x, y, land, visited, size)

    return size[0]


def pond_sizes(land):
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    sizes = []

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 0 and not visited[i][j]:
                pond_size = measure_pond(i, j, land, visited)
                sizes.append(pond_size)

            visited[i][j] = True

    return sizes


land = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

print(pond_sizes(land))

