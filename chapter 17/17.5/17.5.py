numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def is_number(character):
    return character in numbers


def longest_equal(char_and_nums):
    sum = 0
    sum_values = {}
    index = 0
    over = False
    while not over:
        if sum not in sum_values.keys():
            sum_values[sum] = []

        sum_values[sum].append(index)
        index += 1
        if index > len(char_and_nums):
            over = True
            continue
        sum += 1 if is_number(char_and_nums[index - 1]) else -1

    max = 0
    start, end = 0, 0
    for key in sum_values.keys():
        if len(sum_values[key]) > 1 and sum_values[key][-1] - sum_values[key][0] > max:
            print(sum_values[key])
            max = sum_values[key][-1] - sum_values[key][0]
            start, end = sum_values[key][0], sum_values[key][-1]
            print(start, end)

    return char_and_nums[start:end]


print(longest_equal("abc1d2ef345g61b2z96c7rcj"))
