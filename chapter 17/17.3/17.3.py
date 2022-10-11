import random


def random_set(int_array, m):
    if len(int_array) < m:
        raise "Array smaller than wanted set"

    random_set = set([])
    for i in range(m):
        index = random.randint(i, len(int_array) - 1)
        random_set.add(int_array[index])

        aux = int_array[index]
        int_array[index] = int_array[i]
        int_array[i] = aux

    return random_set


print(random_set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
