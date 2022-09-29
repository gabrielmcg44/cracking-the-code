def contiguous_sequence(int_array):
    actual_sum = 0
    max_sum = 0
    for value in int_array:
        actual_sum = max(0, actual_sum + value)
        max_sum = max(max_sum, actual_sum)

    return max_sum


print(contiguous_sequence([2, -8, 3, -2, 4, -10]))
