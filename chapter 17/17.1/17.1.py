
def add_without_plus(a, b):
    counter = 0
    remainder = 0
    mask = 1
    result = 0
    while counter < 32:
        sum_without_remainder = (a & mask) ^ (b & mask)
        digit_result = sum_without_remainder ^ remainder
        remainder = mask << 1 if (remainder & sum_without_remainder) | ((a & mask) & b) == (1 << counter) else 0

        mask = mask << 1
        result = digit_result | result
        counter += 1

    return result


print(add_without_plus(10, -15))

