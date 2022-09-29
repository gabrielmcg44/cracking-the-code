
def sum_swap(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)

    if abs(sum2 - sum1) % 2 != 0:
        return None

    diff = (sum2 - sum1) / 2

    set2 = set(arr2)

    for value in arr1:
        if value + diff in set2:
            return [value, int(value + diff)]

    return None


print(sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))
