def possible_lengths(K, shorter, longer):
    if shorter == longer:
        return [K * shorter]

    lengths = [shorter * K]
    diff = longer - shorter

    for i in range(K):
        lengths.append(lengths[i] + diff)

    return lengths


print(possible_lengths(10, 2, 3))