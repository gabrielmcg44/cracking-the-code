import math


def get_bit(number, i):
    return (number >> i) & 1


def missing_number(int_array):
    n = len(int_array)
    print(n)
    k = 1
    while n > math.pow(2, k):
        k += 1
    print(k)
    options = set(range(n))
    num_zeros, num_ones = math.ceil(n/2), math.floor(n/2)
    num = 0
    for i in range(k):
        index_bit = [[], []]
        for j in options:
            index_bit[get_bit(int_array[j], i)].append(j)

        bit_i = 0 if len(index_bit[0]) < num_zeros else 1
        num += bit_i * math.pow(2, i)
        options = index_bit[bit_i]
        num_zeros, num_ones = math.ceil((len(options)+1)/2), math.floor((len(options)+1)/2)

    return num


print(missing_number([14, 3, 10, 7, 13, 6, 1, 8, 9, 4, 11, 12, 2, 0]))

