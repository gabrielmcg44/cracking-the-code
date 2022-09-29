

def target_sum_pairs(int_array, target):
    int_set = set(int_array)
    int_used_set = set([])

    pairs = []

    for value in int_array:
        if value in int_used_set:
            continue

        if target - value in int_set:
            pairs.append([value, target - value])
            int_used_set.add(value)
            int_used_set.add(target-value)

    return pairs


print(target_sum_pairs([1, 4, 7, 11, 2, 18, 19, 5, 6, 3, 8, 9, 14, 15, 17, 12, 13, 10, 16], 20))
