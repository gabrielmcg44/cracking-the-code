import math
import sys


def kth_multiple(k):
    sequences = [[0, 0, 0]]
    min_unclosed_seq = 0
    next_3_exp = 1

    final = 0
    for _ in range(k):
        min_next = sys.float_info.max
        seq_next = -1
        for i in range(min_unclosed_seq, len(sequences)):
            curr = math.pow(3, sequences[i][0]) * math.pow(5, sequences[i][1]) * math.pow(7, sequences[i][2])
            if curr < min_next:
                min_next = curr
                seq_next = i

        if min_next > math.pow(3, next_3_exp):
            final = math.pow(3, next_3_exp)
            sequences.append([next_3_exp-1, 1, 0])
            next_3_exp += 1
            continue

        final = min_next
        if sequences[seq_next][1] > 0:
            sequences[seq_next][1] -= 1
            sequences[seq_next][2] += 1
        elif sequences[seq_next][0] > 0:
            sequences[seq_next][0] -= 1
            sequences[seq_next][1] += 1
        else:
            min_unclosed_seq += 1
            if min_unclosed_seq == len(sequences):
                sequences.append([next_3_exp, 0, 0])
                next_3_exp += 1

    return final


for i in range(1, 30):
    print(kth_multiple(i))
