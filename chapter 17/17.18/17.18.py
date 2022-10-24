
def shortest_supersequence(shorter, longer):
    shorter_quantities = {}
    shorter_set = set(shorter)
    zero_values = set(shorter)
    marker1 = -1
    marker2 = 0

    shortest = None
    while True:
        if len(zero_values) > 0:
            marker1 += 1
            if marker1 >= len(longer):
                break

            if longer[marker1] in shorter_set:
                if longer[marker1] not in shorter_quantities.keys():
                    shorter_quantities[longer[marker1]] = 0
                    zero_values.remove(longer[marker1])

                shorter_quantities[longer[marker1]] += 1

        if len(zero_values) == 0:
            if shortest is None or marker1 - marker2 < shortest[1] - shortest[0]:
                shortest = [marker2, marker1]

            if longer[marker2] in shorter_set:
                shorter_quantities[longer[marker2]] -= 1
                if shorter_quantities[longer[marker2]] == 0:
                    del shorter_quantities[longer[marker2]]
                    zero_values.add(longer[marker2])

            marker2 += 1

    return shortest


print(shortest_supersequence([1,5,9], [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7,1,5,9]))
