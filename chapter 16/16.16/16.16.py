
import sys


def sub_sort(int_array):
    N = len(int_array)

    counter_asc = 0
    while counter_asc < N- 1 and int_array[counter_asc + 1] > int_array[counter_asc]:
        counter_asc += 1

    if counter_asc == N - 1:
        return 0, 0

    counter_desc = N - 1
    while counter_desc > 0 and int_array[counter_desc] > int_array[counter_desc - 1]:
        counter_desc -= 1

    min_sub = sys.float_info.max
    max_sub = -sys.float_info.max
    for i in range(counter_asc, counter_desc + 1):
        min_sub = min(min_sub, int_array[i])
        max_sub = max(max_sub, int_array[i])

    while int_array[counter_asc] > min_sub and counter_asc > 0:
        counter_asc -= 1

    while int_array[counter_desc] < max_sub and counter_desc < N - 1:
        counter_desc += 1

    return counter_asc + 1, counter_desc - 1


print(sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
