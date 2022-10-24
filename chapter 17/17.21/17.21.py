def histogram_volume(histogram):
    idx = -1
    max = -1
    for i in range(len(histogram)):
        if histogram[i] > max:
            max = histogram[i]
            idx = i

    total = max * len(histogram)
    water = total - sum(histogram)

    greater_left = 0
    idx_greater_left = 0
    for i in range(idx + 1):
        if histogram[i] > greater_left:
            water -= (max - greater_left) * (i - idx_greater_left)
            greater_left = histogram[i]
            idx_greater_left = i

        if greater_left == max:
            break

    greater_right = 0
    idx_greater_right = len(histogram) - 1
    for i in range(len(histogram) - idx):
        if histogram[len(histogram) - 1 - i] > greater_right:
            water -= (max - greater_right) * (idx_greater_right - len(histogram) + 1 + i)
            greater_right = histogram[len(histogram) - 1 - i]
            idx_greater_right = len(histogram) - 1 - i

        if greater_right == max:
            break

    return water


print(histogram_volume([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]))
