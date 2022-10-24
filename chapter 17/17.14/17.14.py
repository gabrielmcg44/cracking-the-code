import math
import random
import time


def partition(num_array, left, right):
    pivot = num_array[math.floor((right+left)/2)]
    while left <= right:
        while num_array[left] < pivot:
            left += 1

        while num_array[right] > pivot:
            right -= 1

        if left <= right:
            aux = num_array[right]
            num_array[right] = num_array[left]
            num_array[left] = aux
            left += 1
            right -= 1

    return left


def swap_k_to_beginning(num_array, k, start=None, end=None):
    if start is None:
        start = 0
        end = len(num_array) - 1

    index = partition(num_array, start, end)

    if index < k:
        swap_k_to_beginning(num_array, k, index, end)
    if index > k:
        swap_k_to_beginning(num_array, k, start, index-1)


def smallest_k(num_array, k):
    if len(num_array) < k:
        return -1

    aux_array = [num for num in num_array]
    swap_k_to_beginning(aux_array, k)
    return aux_array[:k]


def smallest_k_naive(num_array, k):
    if len(num_array) < k or k == 0:
        return -1

    aux_array = [num for num in num_array]
    aux_array.sort()
    # quickSort(aux_array, 0, len(aux_array)-1)
    return aux_array[:k]


size_array = 10000

numbers = [5,2,7,3,10,7,0,1,4,3,1,7,4,5,2,8,9,3,7,1,1,4,2,3,4,4,4,5,5,21,4,4,5,6]
# print(numbers)
# start = time.time()

for k in range(1, len(numbers)):
    start1 = time.time()
    smallest_k_opt_list = smallest_k(numbers, k)
    end1 = time.time()

    start2 = time.time()
    smallest_k_naive_list = smallest_k_naive(numbers, k)
    end2 = time.time()

    print(smallest_k_naive_list == sorted(smallest_k_opt_list))
#
# print("avg time opt", (end1-start1))
# print("avg time naive", (end2-start2))
