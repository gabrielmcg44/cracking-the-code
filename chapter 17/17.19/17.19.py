import math
# O(N) O(1) no integer overflow


def missing_one(int_array, maxN=None):
    if maxN is None:
        maxN = len(int_array) + 1

    N = 1
    sum = 0
    idx = 0
    while N <= maxN or idx < len(int_array):
        if sum <= 0 or idx == len(int_array):
            sum += N
            N += 1
        else:
            if int_array[idx] <= maxN:
                sum -= int_array[idx]
            idx += 1

    return sum


def missing_two(int_array):
    N = 1
    sum = 0
    idx = 0
    while N <= len(int_array) + 1 or idx < len(int_array):
        if sum > N + 2:
            print(sum)

        if sum <= 0 or idx == len(int_array):
            sum += N
            N += 1
        else:
            sum -= int_array[idx]
            idx += 1

    half = int(math.floor(sum / 2 + N / 2))
    first_missing = missing_one(int_array, half)
    second_missing = sum - first_missing + N

    return [first_missing, second_missing]


print(missing_two([1, 2, 3, 4, 5, 6, 7]))
