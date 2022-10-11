import time


def count_of_2s(n):
    if n < 0:
        return 0

    count_past_10 = 0
    mod_10 = n % 10
    if mod_10 >= 2:
        count_past_10 += 1

    num_2_digits = sum([1 for digit in str(n)[:-1] if digit == "2"])
    count_past_10 += int(num_2_digits * (mod_10 + 1))

    return int(count_past_10 + (n - n % 10) / 10 + 10 * count_of_2s(int((n - n % 10) / 10 - 1)))


def count_of_2s_naive(n):

    count = 0
    for number in range(n+1):
        count += sum([1 for digit in str(number) if digit == "2"])

    return count


n = 22332322

start = time.time()
print(count_of_2s(n))
end = time.time()
print(end - start)

start = time.time()
print(count_of_2s_naive(n))
end = time.time()
print(end - start)
