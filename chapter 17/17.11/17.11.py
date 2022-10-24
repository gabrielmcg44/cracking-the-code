import sys

book = ["once", "upon", "a", "time", "there", "was", "a", "history", "book", "with", "a", "history", "of", "another", "book"]

words_positions = {}
for i in range(len(book)):
    if book[i] not in words_positions.keys():
        words_positions[book[i]] = []

    words_positions[book[i]].append(i)


def words_distance(word1, word2):
    if word1 == word2:
        return 0

    word1_positions = words_positions[word1]
    word2_positions = words_positions[word2]

    i1 = 0
    i2 = 0
    min_distance = sys.float_info.max
    while i1 < len(word1_positions) and i2 < len(word2_positions):
        min_distance = min(min_distance, abs(word1_positions[i1] - word2_positions[i2]))
        if word1_positions[i1] < word2_positions[i2]:
            i1 += 1
        else:
            i2 += 1

    return min_distance


print(words_positions)
print(words_distance("upon", "book"))
