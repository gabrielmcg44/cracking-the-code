# needed to see solution

import sys


def re_spaced(document, dictionary):
    memo = [None] * len(document)
    result = re_space(document, dictionary, 0, memo)
    return result.parsed


def re_space(document, dictionary, start, memo):
    if start == len(document):
        return ResultParse("", 0)
    elif memo[start] is not None:
        return memo[start]

    best_invalid = sys.float_info.max
    best_parse = None
    current_parse = ""
    for i in range(start, len(document)):
        current_parse += document[i]
        invalid = 0 if current_parse in dictionary else i + 1 - start
        if invalid < best_invalid:
            remain_re_spaced = re_space(document, dictionary, i + 1, memo)
            new_invalid = invalid + remain_re_spaced.invalid
            if new_invalid < best_invalid:
                best_parse = current_parse + " " + remain_re_spaced.parsed
                best_invalid = new_invalid

    memo[start] = ResultParse(best_parse, best_invalid)
    return memo[start]


class ResultParse:
    def __init__(self, parsed, invalid):
        self.parsed = parsed
        self.invalid = invalid


dictionary = {"looked", "just", "like", "her", "brother", "i", "in", "an", "island", "is", "land"}
document = "jesslookedjustliketimherbrotherinanisland"

result = re_spaced(document, dictionary)
print(result)
