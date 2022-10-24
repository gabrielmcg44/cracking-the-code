import time

# easily overflows
def majority_naive(int_array):
    n = len(int_array)
    product = 1
    for value in int_array:
        product *= value

    for value in int_array:
        exp = 0
        aux_product = product
        while aux_product % value == 0:
            aux_product /= value
            exp += 1

        if exp > n / 2:
            return value

    return -1


def is_majority(int_array, value, split_size):
    count = 0
    for i in range(split_size):
        if int_array[i] == value:
            count += 1

    return count > split_size / 2


def majority(int_array):
    n = len(int_array)

    while True:
        position = 0
        next_swap_position = 0
        while position + 2 <= n:
            if int_array[position] == int_array[position + 1]:
                aux = int_array[position]
                int_array[position] = int_array[next_swap_position]
                int_array[next_swap_position] = aux

                next_swap_position += 1

            position += 2

        if position != n:
            if is_majority(int_array, int_array[position], n):
                return int_array[position]

        if next_swap_position == 0:
            return -1

        n = next_swap_position


test = [1, 2, 5, 9, 5, 9, 5, 5, 5]

multiple = 50000000

start = time.time()
print(majority(test*multiple))
end = time.time()

print((end - start)/multiple)
